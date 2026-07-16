
import ssl
import socket

HOST = '0.0.0.0'
PORT = 65432
CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'
BUFFER_SIZE = 1024

def create_server_socket(host: str, port: int) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    return server_socket

def create_ssl_context(certfile: str, keyfile: str) -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)
    return context

def handle_client(ssl_socket: ssl.SSLSocket) -> None:
    data = ssl_socket.recv(BUFFER_SIZE).decode('utf-8')
    print(f"Received: {data}")
    ssl_socket.close()

def secure_server_kernel(host: str, port: int, certfile: str, keyfile: str) -> None:
    bind_socket = create_server_socket(host, port)
    ssl_context = create_ssl_context(certfile, keyfile)

    print(f"Secure server is listening on port {port}...")

    while True:
        try:
            newsocket, _ = bind_socket.accept()
            ssl_socket = ssl_context.wrap_socket(newsocket, server_side=True)
            handle_client(ssl_socket)

        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == '__main__':
    secure_server_kernel(HOST, PORT, CERT_FILE, KEY_FILE)
