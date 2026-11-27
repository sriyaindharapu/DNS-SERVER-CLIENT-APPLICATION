import socket

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP and port
host = "127.0.0.1"
port = 5000

server.bind((host, port))
server.listen(5)

print("DNS Server is running...")
print(f"Listening on {host}:{port}")

while True:
    conn, addr = server.accept()
    print("Connected to client:", addr)

    # Receive domain name from client
    domain = conn.recv(1024).decode().strip()

    try:
        # Resolve domain name into IP address
        ip_address = socket.gethostbyname(domain)
        response = f"IP Address of {domain}: {ip_address}"

    except socket.gaierror:
        response = "Error: Domain name could not be resolved."

    # Send result back to client
    conn.send(response.encode())

    print("Request:", domain)
    print("Response:", response)

    conn.close()