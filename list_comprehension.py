# super_heroes = [
#     "batman",
#     "superman",
#     "iron man",
#     "shazam",
#     "thor",
#     "black adam",
#     "captain america",
#     "spiderman",
# ]
# super_heroes = [heroes.upper() for heroes in super_heroes]
# print(super_heroes)

# bits = [True, False, True, True, False, True, False, False, True, False, False, False]
# new_bits = [1 if b == True else 0 for b in bits]
# print(bits)
# print(new_bits)

strg = "HiMyNameIsDastagirAndILovePython"
strg = "".join(
    [i if i.islower() else " " + i.lower() if i in ["M","N","I","A","L"] else " " + i for i in strg]
    )[1:]
print(strg)