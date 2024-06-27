import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter the server IP address: ")
    client_socket.connect((server_ip, 5555))

    name = input("Enter your name: ")
    
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input()
        if message:
            try:
                client_socket.send(f"{name}: {message}".encode())
            except Exception as e:
                print(f"Error sending message: {e}")
                break

if __name__ == "__main__":
    start_client()
