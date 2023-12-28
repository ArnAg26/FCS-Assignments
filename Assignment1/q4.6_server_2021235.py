import socket
import hashlib

try:
    server_address = ('192.168.56.121', 80) 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server is listening for incoming connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        data = client_socket.recv(1024).decode()
        message, received_hash = data.split('|')
        computed_hash = hashlib.sha256(message.encode("utf-8")).hexdigest()

        if received_hash == computed_hash and message=="Hello, Server!":
            response = "Hello, Client!"
        else:
            if(received_hash != computed_hash):
                response = "Hash values do not match. Message may be corrupted."
            else:
                response=f"Message sent may be wrong: {message}"
        client_socket.send(response.encode())
        print("Response sent to client.")
except Exception as e:
    print(e)
finally:

    server_socket.close()