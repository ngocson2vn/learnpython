import socket
import selectors

selector = selectors.DefaultSelector()

def setup_listening_socket(host="127.0.0.1", port=2606):
  sock = socket.socket()
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind((host, port))
  sock.listen()
  selector.register(sock, selectors.EVENT_READ, accept)

def accept(sock: socket.socket):
  client_sock, addr = sock.accept()
  print("Connection from", addr)
  selector.register(client_sock, selectors.EVENT_READ, recv_and_send)

def recv_and_send(sock: socket.socket):
  received_data = sock.recv(4096)
  if received_data:
    sock.sendall(received_data)
  else:
    print("Client disconnected:", sock.getpeername())
    selector.unregister(sock)
    sock.close()

def run_event_loop():
  while True:
    for key, _ in selector.select():
      callback = key.data
      sock = key.fileobj
      callback(sock)

if __name__ == "__main__":
  setup_listening_socket()
  run_event_loop()
