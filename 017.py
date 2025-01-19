# import ssl
# import json
# import asyncio
# import websockets
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# def generate_tags(input_data):
#     tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
#     model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
#     inputs = tokenizer.encode(input_data, max_length=2048, truncation=True, padding="longest", return_tensors="pt")
#     outputs = model.generate(inputs, num_beams=10, num_return_sequences=1, max_length=64, early_stopping=True)
#     decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
#     return decoded_outputs

# ddd = """In this modified implementation, the method will keep waiting for responses until the remaining timeout is greater than zero. If a response with a matching request ID is received, it will be returned, and the client's status will be updated to 'idle'. If the timeout is reached without receiving a matching response, None will be returned."""

# async def connect_to_webapp():
#     # Disable SSL certificate verification (for troubleshooting purposes)
#     ssl_context = ssl.create_default_context()
#     ssl_context.check_hostname = False
#     ssl_context.verify_mode = ssl.CERT_NONE


#     client_id = '12345678902'
#     async with websockets.connect('wss://vocalhost.reiserx.com/ws/?client_id=' + client_id, ping_interval=60, ping_timeout=60, ssl=ssl_context) as websocket:
#         # Perform any necessary handshake or authentication process
#         # Once the connection is established, you can start listening for messages
#         try:
#             while True:
#                 message = await websocket.recv()
#                 # Process the received message from the web app
#                 # Handle the request and send a response back, if required
#                 print(f"Received message: {message}")

#                 tags = ', '.join(set(generate_tags(ddd)[0].strip().split(", ")))

#                 print(tags)

#                 data = {
#                     'data': tags,
#                 }

#                 print(data)
#                 # Serialize the data to JSON
#                 data_str = json.dumps(data)
#                 print(data_str)

#                 # Send the JSON data to the web app
#                 await websocket.send(data_str)
#         except asyncio.TimeoutError as e:
#             # Handle timeout here (e.g., send a keepalive message to prevent connection closure)
#             await websocket.ping()
#             print(e)
#         except websockets.ConnectionClosed as e:
#             # Handle connection closure here
#             print(e)
#             pass

# if __name__ == '__main__':
#     asyncio.run(connect_to_webapp())









import ssl
import json
import asyncio
import websockets
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_tags(input_data):
    tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    inputs = tokenizer.encode(input_data, max_length=2048, truncation=True, padding="longest", return_tensors="pt")
    outputs = model.generate(inputs, num_beams=10, num_return_sequences=1, max_length=64, early_stopping=True)
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded_outputs

ddd = """In this modified implementation, the method will keep waiting for responses until the remaining timeout is greater than zero. If a response with a matching request ID is received, it will be returned, and the client's status will be updated to 'idle'. If the timeout is reached without receiving a matching response, None will be returned."""

async def connect_to_webapp():
    # Disable SSL certificate verification (for troubleshooting purposes)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    client_id = '12345678902'
    async with websockets.connect('wss://vocalhost.reiserx.com/ws/?client_id=' + client_id, ping_interval=60, ping_timeout=60, ssl=ssl_context) as websocket:
        # Perform any necessary handshake or authentication process
        # Once the connection is established, you can start listening for messages
        try:
            while True:
                message = await websocket.recv()
                # Process the received message from the web app
                # Handle the request and send a response back, if required
                print(f"Received message: {message}")

                tags = ', '.join(set(generate_tags(ddd)[0].strip().split(", ")))

                print(tags)

                data = {
                    'data': tags,
                }

                print(data)
                # Serialize the data to JSON
                data_str = json.dumps(data)
                print(data_str)

                # Send the JSON data to the web app
                await websocket.send(data_str)
        except asyncio.TimeoutError as e:
            # Handle timeout here (e.g., send a keepalive message to prevent connection closure)
            await websocket.ping()
            print("Timeout occurred:", e)
        except websockets.ConnectionClosed as e:
            # Handle connection closure here
            print("Connection closed:", e)
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", e)

if __name__ == '__main__':
    asyncio.run(connect_to_webapp())




import ssl
import json
import asyncio
import websockets
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_tags(input_data):
    tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    inputs = tokenizer.encode(input_data, max_length=2048, truncation=True, padding="longest", return_tensors="pt")
    outputs = model.generate(inputs, num_beams=10, num_return_sequences=1, max_length=64, early_stopping=True)
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded_outputs

ddd = """In this modified implementation, the method will keep waiting for responses until the remaining timeout is greater than zero. If a response with a matching request ID is received, it will be returned, and the client's status will be updated to 'idle'. If the timeout is reached without receiving a matching response, None will be returned."""

async def connect_to_webapp(client_id):
    # Disable SSL certificate verification (for troubleshooting purposes)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect('wss://vocalhost.reiserx.com/ws/?client_id=' + client_id, ping_interval=60, ping_timeout=60, ssl=ssl_context) as websocket:
        # Perform any necessary handshake or authentication process
        # Once the connection is established, you can start listening for messages
        while True:
            message = await websocket.recv()
            # Process the received message from the web app
            # Handle the request and send a response back, if required
            print(f"Received message: {message}")

            # Check if the message is a request for tags
            if message == "get_tags":
                # Generate tags for the given input data
                tags = ', '.join(set(generate_tags(ddd)[0].strip().split(", ")))

                # Send the tags to the web app
                await websocket.send(json.dumps({'data': tags}))
            else:
                # Handle other requests here
                print("Unrecognized message:", message)

        # Handle connection closure here
        await websocket.close()

if __name__ == '__main__':
    client_id = input("Enter your client ID: ")
    asyncio.run(connect_to_webapp(client_id))




import ssl
import json
import asyncio
import websockets
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_tags(input_data):
    tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\zeeshan\PycharmProjects\djangoProject1\Models/Tags")
    inputs = tokenizer.encode(input_data, max_length=2048, truncation=True, padding="longest", return_tensors="pt")
    outputs = model.generate(inputs, num_beams=10, num_return_sequences=1, max_length=64, early_stopping=True)
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded_outputs

ddd = """In this modified implementation, the method will keep waiting for responses until the remaining timeout is greater than zero. If a response with a matching request ID is received, it will be returned, and the client's status will be updated to 'idle'. If the timeout is reached without receiving a matching response, None will be returned."""

async def connect_to_webapp(client_id):
    # Disable SSL certificate verification (for troubleshooting purposes)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect('wss://vocalhost.reiserx.com/ws/?client_id=' + client_id, ping_interval=60, ping_timeout=60, ssl=ssl_context) as websocket:
        # Perform any necessary handshake or authentication process
        # Once the connection is established, you can start listening for messages
        try:
            while True:
                message = await websocket.recv()
                # Process the received message from the web app
                # Handle the request and send a response back, if required
                print(f"Received message: {message}")

                # Check for common errors
                if message == "PING":
                    await websocket.pong()
                elif message == "CLOSE":
                    await websocket.close()
                else:
                    # Generate tags for the input text
                    tags = ', '.join(set(generate_tags(ddd)[0].strip().split(", ")))

                    # Send the tags to the web app
                    await websocket.send(json.dumps({'data': tags}))
        except asyncio.TimeoutError as e:
            # Handle timeout here (e.g., send a keepalive message to prevent connection closure)
            await websocket.ping()
            print(e)
        except websockets.ConnectionClosed as e:
            # Handle connection closure here
            print(e)
            pass

if __name__ == '__main__':
    client_id = input("Enter your client ID: ")
    asyncio.run(connect_to_webapp(client_id))
