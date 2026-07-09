
import ssl
import socket
from typing import Optional

def create_context(cafile: str = "server.crt") -> ssl.SSLContext:
	"""Create and return an SSL context for a client."""
	ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
	ctx.load_verify_locations(cafile=cafile)
	ctx.check_hostname = False  # self-signed certs in this example
	return ctx

def connect(host: str, port: int, context: ssl.SSLContext) -> ssl.SSLSocket:
	"""Create a TCP socket, wrap it with SSL and connect."""
	raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssl_sock = context.wrap_socket(raw, server_hostname=host)
	ssl_sock.connect((host, port))
	return ssl_sock

def send_message(ssl_sock: ssl.SSLSocket, message: str) -> None:
	"""Send a UTF-8 encoded message over the SSL socket."""
	ssl_sock.sendall(message.encode("utf-8"))

def close(ssl_socket: Optional[ssl.SSLSocket]) -> None:
	"""Close the SSL socket if open."""
	if ssl_socket:
		try:
			ssl_socket.shutdown(socket.SHUT_RDWR)
		except Exception:
			pass
		ssl_socket.close()

def main(host_ip: str = "192.168.X.X", port: int = 65432, cafile: str = "server.crt") -> None:
	ctx = create_context(cafile=cafile)
	socket = None
	try:
		socket = connect(host_ip, port, ctx)
		send_message(socket, "Hello from the secure client!")
	finally:
		close(socket)

if __name__ == "__main__":
	main()
