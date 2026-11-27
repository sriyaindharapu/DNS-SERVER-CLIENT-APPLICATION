import socket

host = "127.0.0.1"
port = 5000

while True:
    domain = input("\nEnter domain name (or 'exit'): ")

    if domain.lower() == "exit":
        print("Client disconnected.")
        break

    # Create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to DNS server
    client.connect((host, port))

    # Send domain name to server
    client.send(domain.encode())

    # Receive IP address from server
    response = client.recv(1024).decode()

    print("Server Response:", response)

    client.close()