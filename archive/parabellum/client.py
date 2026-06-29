
import socket
from durapy import uniCLI

SERVER_IP = '192.168.0.107'
PORT = 5000

def initialize_server_connection(ip: str, port: int) -> tuple[socket.socket | None, bool]:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
        uniCLI.console_print("CLIENT", "blue", "Connected.", "green")
        return (client, True)
    except (ConnectionRefusedError, TimeoutError) as e:
        uniCLI.console_print("CLIENT", "blue", f"Failed to connect: {e}", "red")
        return (None, False)

def connection_loop() -> None:
    while True:
        message = uniCLI.console_input("TO SERVER", "blue", " ")
        client.sendall(message.encode())
        data = client.recv(1024).decode()
        uniCLI.console_print(f"SERVER: {SERVER_IP}", "green", data)

client, connected = initialize_server_connection(SERVER_IP, PORT)
    
if connected and client:  
    connection_loop()  
    
    
