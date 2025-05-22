# server.py
import socket
import threading

HOST = '0.0.0.0'   # Lytt på alle nettverkskort
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"[+] Tilkoblet: {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[{addr}] {data}") # Mottatt data fra klient
            # Send svar tilbake hvis ønsket
            conn.sendall(f"ACK: {data}".encode()) # Bekreftelse til klient
        except:
            break
    print(f"[-] Frakoblet: {addr}")
    conn.close()
    clients.remove(conn)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Lytter på {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
