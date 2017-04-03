import hashlib

salt = "AhBaik4auv3Seihu"

def encode(clearString):
    return hashlib.sha512(str.encode(salt + clearString)).hexdigest()
