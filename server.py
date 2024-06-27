import socket
import threading

def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message from client: {message}")
                broadcast(message, client_socket, clients)
        except Exception as e:
            print(f"Error handling client: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, client_socket, clients):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    clients = []

    print("Server started on port 5555...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, clients)).start()

if __name__ == "__main__":
    start_server()
