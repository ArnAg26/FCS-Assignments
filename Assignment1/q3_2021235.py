import base64
import hmac
import hashlib
import json

validKey=[]
from itertools import product




def verifyJwt(token, secret):
    L=token.split('.')
    if(len(L)!=3):
        raise Exception(f"{token} is invalid")
    header_b64, payload_b64, provided_signature =L
    #print(header_b64.encode('utf-8'))
    header = json.loads(base64.urlsafe_b64decode(header_b64+'===').decode('utf-8'))
    payload = json.loads(base64.urlsafe_b64decode(payload_b64+'===').decode('utf-8'))
    #print(header)
    algorithm = header['alg']
    

    data_to_verify = f"{header_b64}.{payload_b64}".encode('utf-8')

    if algorithm == 'HS256':
        sign=hmac.new(secret.encode('utf-8'), data_to_verify, hashlib.sha256).digest()
        #print(sign)
        expected_signature = base64.urlsafe_b64encode(sign).rstrip(b'=').decode('utf-8')
    elif algorithm == 'HS512':
        sign=hmac.new(secret.encode('utf-8'), data_to_verify, hashlib.sha512).digest()
        #print(sign)
        expected_signature = base64.urlsafe_b64encode(sign).rstrip(b'=').decode('utf-8')
    else:
        raise Exception(f"{algorithm} is unsupported")


    if expected_signature == provided_signature:
        validKey.append(secret)
        return payload
    else:
        return f"{secret} is Invalid JWT signature or token has been tampered with"


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDIxMjM1IiwibmFtZSI6IkFybmF2IEFnYXJ3YWwiLCJpYXQiOjE1MTYyMzkwMjJ9.OXNIctlVP0iQTKJf-stDW2fNo4KgEQ-_ZUDkt180eRk"

secret = "adwidwiijdwiajdpppiwjdpwaljlsjdowijkkjksjwswdjawp"

try:
    decoded_payload = verifyJwt(token, secret)
    print("Decoded Payload:", decoded_payload)
except Exception as e:
    print(e)


    



def makeToken(secret):
    header={"alg":"HS256","typ":"JWT"}
    payload={"rollno":2021235,"emailid":"arnav21235@iiitd.ac.in"}
    header=json.dumps(header).encode("utf-8")
    payload=json.dumps(payload).encode("utf-8")
    header=base64.urlsafe_b64encode(header).rstrip(b'=')
    payload=base64.urlsafe_b64encode(payload).rstrip(b'=')
    token=header+b"."+payload
    #print(token)
    secret=secret.encode("utf-8")
    signature = hmac.new(key=secret,msg=token,digestmod=hashlib.sha256).digest()
    signature=base64.urlsafe_b64encode(signature).rstrip(b'=')
    token=token+b'.'+signature
    token=token.decode("utf-8")
    return token

    

secretToken="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE3MDQwNjcyMDAsInJvbGxfbm8iOiIyMHh4eHh4IiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.5RcJW1ZV5gsCmV-3mufIieogVoAqr_xdyUbvLJh49dQ"

l="abcdefghijklmnopqrstuvwxyz1234567890"

    # k=0
    # permutation_list=[]
    #for perm_indices in product(range(len(l)), repeat=5):
    #     permutation = ''.join(l[i] for i in perm_indices)

    #     print(permutation)
    #     verifyJwt(secretToken,permutation)
    #     if len(validKey)>0:
    #         break
    
    
    #print(validKey)
s=makeToken("gg476")
print("We encoded the following payload using gg746 and created a JWT token")
print("The algorithm followed was HS256")
print(f"The token we created using the secret gg476 is :{s}")
#Verify if the token n was created correctly
print(verifyJwt(s,"gg476"))
#key found is gg476


