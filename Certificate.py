
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import rsa
import random
import base64

def hash(text):
    hash_obj = hashlib.sha256()

    hash_obj.update(text.encode())

    hash_hex = hash_obj.digest()
    #print(hash_hex)
    return hash_hex

with open("input.txt","r") as file:
    text=file.read()

h=hash(text)
print(f"Original hash:{h}")

def encrypt(text):
    with open('private_key.pem', 'r') as private_key_file:
        private_key_text = private_key_file.read()
    print(private_key_text)
    private_key = RSA.import_key(private_key_text)
    cipher = PKCS1_OAEP.new(private_key)
    # text_bytes = bytes.fromhex(text)
    # text=text_bytes.decode("utf-8")
    encrypted_hash = cipher.encrypt(text)
    print(encrypted_hash)
    #encrypted_hash=encrypted_hash.decode("utf-8")
    return encrypted_hash.hex()


sign=encrypt(h)

with open("input.txt","a") as file:
    file.write(f"\nSignature:{sign}")

with open("output.txt","w") as file:
    file.write(sign)
