import base64

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

from Cryptodome.Cipher import AES


def b64(msg):
    # base64 encoding helper function
    return base64.encodebytes(msg).decode("utf-8").strip()


def hkdf(inp, length):
    # use HKDF on an input to derive a key
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=length,
        salt=b"",
        info=b"",
        backend=default_backend(),
    )
    return hkdf.derive(inp)


def pad(msg):
    # pkcs7 padding
    num = 16 - (len(msg) % 16)
    return msg + bytes([num] * num)


def unpad(msg):
    # remove pkcs7 padding
    return msg[: -msg[-1]]


class SymmRatchet(object):
    def __init__(self, key):
        self.state = key

    def next(self, inp=b""):
        # turn the ratchet, changing the state and yielding a new key and IV
        output = hkdf(self.state + inp, 80)
        self.state = output[:32]
        outkey, iv = output[32:64], output[64:]
        return outkey, iv


class Bob(object):
    def __init__(self):
        # generate Bob's keys
        self.IKb = X25519PrivateKey.generate()
        self.SPKb = X25519PrivateKey.generate()
        self.OPKb = X25519PrivateKey.generate()
        self.DHratchet = X25519PrivateKey.generate()

    def x3dh(self, alice):
        # perform the 4 Diffie Hellman exchanges (X3DH)
        dh1 = self.SPKb.exchange(alice.IKa.public_key())
        dh2 = self.IKb.exchange(alice.EKa.public_key())
        dh3 = self.SPKb.exchange(alice.EKa.public_key())
        dh4 = self.OPKb.exchange(alice.EKa.public_key())
        # the shared key is KDF(DH1||DH2||DH3||DH4)
        self.sk = hkdf(dh1 + dh2 + dh3 + dh4, 32)
        print("Shared key:", b64(self.sk))
        # print("[Bob]Shared key:", b64(self.sk))

    def init_ratchets(self):
        # initialise the root chain with the shared key
        self.root_ratchet = SymmRatchet(self.sk)
        # initialise the sending and recving chains
        self.recv_ratchet = SymmRatchet(self.root_ratchet.next()[0])
        self.send_ratchet = SymmRatchet(self.root_ratchet.next()[0])

    def dh_ratchet(self, alice_public):
        # perform a DH ratchet rotation using Alice's public key
        dh_recv = self.DHratchet.exchange(alice_public)
        shared_recv = self.root_ratchet.next(dh_recv)[0]
        # use Alice's public and our old private key
        # to get a new recv ratchet
        self.recv_ratchet = SymmRatchet(shared_recv)
        print("Recv ratchet seed:", b64(shared_recv))
        # print("[Bob]Recv ratchet seed:", b64(shared_recv))
        # generate a new key pair and send ratchet
        # our new public key will be sent with the next message to Alice
        self.DHratchet = X25519PrivateKey.generate()
        dh_send = self.DHratchet.exchange(alice_public)
        shared_send = self.root_ratchet.next(dh_send)[0]
        self.send_ratchet = SymmRatchet(shared_send)
        print("Send ratchet seed:", b64(shared_send))
        # print("[Bob]Send ratchet seed:", b64(shared_send))

    def send(self, alice, msg):
        key, iv = self.send_ratchet.next()
        cipher = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(msg))
        print("Sending ciphertext to Alice:", b64(cipher))
        # print("[Bob]Sending ciphertext to Alice:", b64(cipher))
        # send ciphertext and current DH public key
        alice.recv(cipher, self.DHratchet.public_key())

    def recv(self, cipher, alice_public_key):
        # receive Alice's new public key and use it to perform a DH
        self.dh_ratchet(alice_public_key)
        key, iv = self.recv_ratchet.next()
        # decrypt the message using the new recv ratchet
        msg = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cipher))
        print("Decrypted message:", msg)
        # print("[Bob]Decrypted message:", msg)


class Alice(object):
    def __init__(self):
        self.IKa = X25519PrivateKey.generate()
        self.EKa = X25519PrivateKey.generate()
        self.DHratchet = None

    def x3dh(self, bob):
        dh1 = self.IKa.exchange(bob.SPKb.public_key())
        dh2 = self.EKa.exchange(bob.IKb.public_key())
        dh3 = self.EKa.exchange(bob.SPKb.public_key())
        dh4 = self.EKa.exchange(bob.OPKb.public_key())
        self.sk = hkdf(dh1 + dh2 + dh3 + dh4, 32)
        print("Shared key:", b64(self.sk))
        # print("[Alice]Shared key:", b64(self.sk))

    def init_ratchets(self):
        # initialise the root chain with the shared key
        self.root_ratchet = SymmRatchet(self.sk)
        # initialise the sending and recving chains
        self.send_ratchet = SymmRatchet(self.root_ratchet.next()[0])
        self.recv_ratchet = SymmRatchet(self.root_ratchet.next()[0])

    def dh_ratchet(self, bob_public):
        # perform a DH ratchet rotation using Bob's public key
        if self.DHratchet is not None:
            # the first time we don't have a DH ratchet yet
            dh_recv = self.DHratchet.exchange(bob_public)
            shared_recv = self.root_ratchet.next(dh_recv)[0]
            # use Bob's public and our old private key
            # to get a new recv ratchet
            self.recv_ratchet = SymmRatchet(shared_recv)
            print("Recv ratchet seed:", b64(shared_recv))
            # print("[Alice]Recv ratchet seed:", b64(shared_recv))
        # generate a new key pair and send ratchet
        # our new public key will be sent with the next message to Bob
        self.DHratchet = X25519PrivateKey.generate()
        dh_send = self.DHratchet.exchange(bob_public)
        shared_send = self.root_ratchet.next(dh_send)[0]
        self.send_ratchet = SymmRatchet(shared_send)
        print("Send ratchet seed:", b64(shared_send))
        # print("[Alice]Send ratchet seed:", b64(shared_send))

    def send(self, bob, msg):
        key, iv = self.send_ratchet.next()
        cipher = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(msg))
        print("Sending ciphertext to Bob:", b64(cipher))
        # print("[Alice]Sending ciphertext to Bob:", b64(cipher))
        # send ciphertext and current DH public key
        bob.recv(cipher, self.DHratchet.public_key())

    def recv(self, cipher, bob_public_key):
        # receive Bob's new public key and use it to perform a DH
        self.dh_ratchet(bob_public_key)
        key, iv = self.recv_ratchet.next()
        # decrypt the message using the new recv ratchet
        msg = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cipher))
        # print("[Alice]Decrypted message:", msg)
        print("Decrypted message:", msg)


# alice = Alice()
# bob = Bob()

# # Alice performs an X3DH while Bob is offline, using his uploaded keys
# alice.x3dh(bob)

# # Bob comes online and performs an X3DH using Alice's public keys
# bob.x3dh(alice)

# # Initialize their symmetric ratchets
# alice.init_ratchets()
# bob.init_ratchets()

# # Initialise Alice's sending ratchet with Bob's public key
# alice.dh_ratchet(bob.DHratchet.public_key())

# # Alice sends Bob a message and her new DH ratchet public key
# alice.send(bob, b"rgf2t74f35rtvby1dncfubunvi!")

# # Bob uses that information to sync with Alice and send her a message
# bob.send(alice, b"4ufbgy438r29u43jgr0ebmgn3rub9gr3gn0vf")

import time

alice = Alice()
bob = Bob()

# Alice performs an X3DH while Bob is offline, using his uploaded keys
alice.x3dh(bob)

# Bob comes online and performs an X3DH using Alice's public keys
bob.x3dh(alice)

# Initialize their symmetric ratchets
alice.init_ratchets()
bob.init_ratchets()

while True:
    print(" ")
    # Alice's sending ratchet is initialized with Bob's public key
    alice.dh_ratchet(bob.DHratchet.public_key())
    
    # Alice sends Bob a message along with her new DH ratchet public key
    alice.send(bob, b"rgf2t74f35rtvby1dncfubunvi!")
    
    # Wait for 3 seconds before the next step
    time.sleep(3)
    
    # Bob uses Alice's information to sync and send her a message
    bob.send(alice, b"4ufbgy438r29u43jgr0ebmgn3rub9gr3gn0vf")
    
    # Wait for another 3 seconds before the next round
    time.sleep(3)
