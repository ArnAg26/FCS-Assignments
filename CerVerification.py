import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

with open("output.bin","rb") as text_file:
    text=text_file.read()
    text=text.decode("utf-8")

text=text.split("\n")
text=text[:-1]
a=""
for i in text:
    a+=i+"\n"
text=a.rstrip('\n')
def hash(text):
    hash_obj = hashlib.sha256()
    hash_obj.update(text.encode())
    hash_hex = hash_obj.hexdigest()
    return hash_hex
print(text)
h = hash(text)


with open("input.txt","r") as signature_file:
    p=signature_file.readlines()
p=p[-1]
p=p.split(":")[1]
signature=p

signature_bytes=bytes.fromhex(signature)

def decrypt(signature_bytes):
    with open("input.txt","r") as file:
        p=file.readlines()
    p=p[5:-1]
    a=""
    for i in p:
        a+=i
    public_key_text=a
    public_key = RSA.import_key(public_key_text)
    cipher = PKCS1_OAEP.new(public_key)

    decrypted_hash = cipher.decrypt(signature_bytes)
    return decrypted_hash.hex()
decrypted_signature = decrypt(signature_bytes)
print(decrypted_signature)
print(h)
if(h==decrypted_signature):
    print("The certificate is valid")
else:
    print("Someone has tampered with this certificate")
# with open("output.txt", "w") as file:
#     file.write(f"Decrypted Signature: {decrypted_signature}")


