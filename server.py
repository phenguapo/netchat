import socket
import threading
import os

def handle_client(client_socket, clients, addr):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("FILE:"):
                filename, filesize = message.split(":")[1], int(message.split(":")[2])
                handle_file(client_socket, filename, filesize, clients)
            else:
                print(f"Received message from client {addr}: {message}")
                broadcast(message, client_socket, clients)
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

def handle_file(client_socket, filename, filesize, clients):
    with open(filename, 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            bytes_read = client_socket.recv(1024)
            if not bytes_read:
                break
            f.write(bytes_read)
            bytes_received += len(bytes_read)
        print(f"Received file {filename} from client")
    broadcast_file(filename, client_socket, clients)

def broadcast(message, client_socket, clients):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.remove(client)

def broadcast_file(filename, client_socket, clients):
    filesize = os.path.getsize(filename)
    for client in clients:
        if client != client_socket:
            try:
                client.send(f"FILE:{filename}:{filesize}".encode())
                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(1024)
                        if not bytes_read:
                            break
                        client.sendall(bytes_read)
                print(f"Broadcasted file {filename} to clients")
            except Exception as e:
                print(f"Error broadcasting file: {e}")
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
        threading.Thread(target=handle_client, args=(client_socket, clients, addr)).start()

if __name__ == "__main__":
    start_server()
