import socket
import threading
import os

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("FILE:"):
                filename, filesize = message.split(":")[1], int(message.split(":")[2])
                receive_file(client_socket, filename, filesize)
            else:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def receive_file(client_socket, filename, filesize):
    with open(f"received_{filename}", 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            bytes_read = client_socket.recv(1024)
            if not bytes_read:
                break
            f.write(bytes_read)
            bytes_received += len(bytes_read)
    print(f"Received file {filename}")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter the server IP address: ")
    client_socket.connect((server_ip, 5555))

    name = input("Enter your name: ")
    
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input()
        if message.startswith("sf "):
            filepath = message.split("sf ")[1].strip()
            if os.path.isfile(filepath):
                send_file(client_socket, filepath, name)
            else:
                print(f"File {filepath} does not exist")
        else:
            try:
                client_socket.send(f"{name}: {message}".encode())
            except Exception as e:
                print(f"Error sending message: {e}")
                break

def send_file(client_socket, filepath, name):
    filesize = os.path.getsize(filepath)
    filename = os.path.basename(filepath)
    try:
        client_socket.send(f"FILE:{filename}:{filesize}".encode())
        with open(filepath, 'rb') as f:
            while True:
                bytes_read = f.read(1024)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
        print(f"Sent file {filename}")
    except Exception as e:
        print(f"Error sending file: {e}")

if __name__ == "__main__":
    start_client()
