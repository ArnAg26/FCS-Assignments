import socket


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
except Exception as e:
    print(e)
finally:

    server_socket.close()