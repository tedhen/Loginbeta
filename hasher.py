import hashlib

salt = 'AhBaik4auv3Seihu'


def encode(clear_string):
    return hashlib.sha512(str.encode(salt + clear_string)).hexdigest()
