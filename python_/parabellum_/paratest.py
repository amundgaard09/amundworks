
# client.py
import socket

SERVER_IP = '192.168.50.138'  # IP = Server PC IP
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("[CLIENT] Tilkoblet til serveren.")

while True:
    msg = input("Send melding: ")
    client.sendall(msg.encode())
    data = client.recv(1024).decode()
    print(f"[SERVER SVAR] {data}")
