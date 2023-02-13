import socket

def run_server(host='127.0.0.1', port=2606):
  sock = socket.socket()
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind((host, port))
  sock.listen()
  while True:
    client_sock, addr = sock.accept()
    print("Connection from", addr)
    handle_client(client_sock)

def handle_client(sock: socket.socket):
  while True:
    received_data = sock.recv(4096)
    if not received_data:
      break
    sock.sendall(received_data)
  print("Client disconnected:", sock.getpeername())
  sock.close()

if __name__ == "__main__":
  run_server()
