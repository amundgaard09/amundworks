
import socket
from durapy import uniCLI

SERVER_IP = '192.168.0.107'
PORT = 5000

def connect_to_server(ip: str, port: int) -> socket.socket | None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip, port))

    except (ConnectionRefusedError, TimeoutError) as e:
        uniCLI.console_print("CLIENT", "blue", f"Failed to connect: {e}", "red")
        return None

    else:
        uniCLI.console_print("CLIENT", "blue", "Connected", "green")
        return client

def connection_loop(client: socket.socket) -> None:
    while True:
        message = str(uniCLI.console_input("TO SERVER", "blue", " "))

        try:
            client.sendall(message.encode())

        except Exception as e:
            uniCLI.console_print("SERVER", "red", f"An error occured: {e}")
            break

        data = client.recv(1024).decode()
        uniCLI.console_print(f"SERVER: {SERVER_IP}", "green", data)

client = connect_to_server(SERVER_IP, PORT)

if client:
    connection_loop(client)
