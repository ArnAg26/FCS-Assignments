import socket
import hashlib

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.56.121', 80))
    message = "Hello, Server!"
    message_hash = hashlib.sha256(message.encode("utf-8")).hexdigest()
    data_to_send = f"{message}|{message_hash}"
    print(f"THe data sent is: {data_to_send}")
    client_socket.send(data_to_send.encode())
    response = client_socket.recv(512).decode()
    if(response=="Hello, Client!"):

        print("Server says:", response)
        print("Server received message successfully")
    else:
        print(f"Server ran into an error: {response}")

except ConnectionError as e:
    print(f"Error Connecting: {e}")
except socket.error as e:
    print(f"Some error in socket {e}")
except Exception as e:
    print(e)
finally:
    try:
        client_socket.close()
    except Exception as e:
        print(e)