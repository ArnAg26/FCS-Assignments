import socket
import hashlib

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.56.121', 80))
    message = "Hello, Server!"
    client_socket.send(message.encode())
    response = client_socket.recv(512).decode()
    if(response=="Hello, Client!"):
        print("Server says:", response)

    else:
        print(f"Server ran into an error: {response}")
except ConnectionError as e:
    print(f"Error Connecting: {e}")
except socket.error as e:
    print(f"We encountered a socket error:{e}")
except Exception as e:
    print(e)
finally:
    try:
        client_socket.close()
    except socket.error as e:
        print(f"We encountered a socket error trying to close the socket:{e}")

