# Netchat

Netchat is a simple client-server chat application built using Python's socket programming and threading capabilities.

## Features

- Allows multiple network clients to connect to a central server and chat in real-time.
- Basic message broadcasting to all connected clients.
- Simple command-line interface for both client and server components.

## Files

- **server.py**: Contains the server-side implementation.
- **client.py**: Contains the client-side implementation.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <https://github.com/phenguapo/netchat>
   cd netchat

2. **No Dependencies Required!**

3. **Run the Server:**
- Open a terminal window.
- Navigate to the directory containing **server.py**.
- Start the server by running the following command:
    ```bash
   python server.py

- The server will start listening for incoming connections on port 5555.
- Note: Run this in a singular machine. You can still run the client on the same machine as the server.

4. **Run the Client on all machines:**
- Open a terminal window.
- Navigate to the directory containing **client.py**.
- Start a client by running the following command:
    ```bash
   python client.py
- Check the ip address of the machine running the server.
- Enter the server's IP address when prompted.
- Enter your name as prompted to begin chatting.

5. **Chatting:**
- Once connected, you can start sending messages from the client.
- For sending files, simply use 'sf < filepath >' (remove<>)
- Messages and files will be displayed on the server and broadcasted to all connected clients.
- Use Ctrl+C to exit both the server and client.

## Notes
Ensure proper network configuration (firewall settings, etc.) to allow communication between the server and clients. This is a basic implementation and lacks advanced features like message encryption, user authentication, etc. Handle exceptions and errors gracefully, especially in real-world scenarios where network conditions can be unpredictable.
