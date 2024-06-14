import socket

# Define the IP address and port to listen on
UDP_IP = "127.0.0.1"
UDP_PORT = 8000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data from the socket (buffer size is 1024 bytes)
    data, addr = sock.recvfrom(1024)
    
    # Print the received data
    print(f"Received message from {addr}: {data.decode('utf-8', 'ignore')}")
