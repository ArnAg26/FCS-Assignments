import socket


try:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    client_socket.connect(('192.168.56.121', 80))


    message = "Hello, Server!"

    client_socket.send(message.encode())
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
