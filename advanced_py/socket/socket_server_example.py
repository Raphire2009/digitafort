# Python Socket Server Example
import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Establish a connection
    clientsocket, addr = serversocket.accept()
    print(f"Got a connection from {addr}")

    msg = 'Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
