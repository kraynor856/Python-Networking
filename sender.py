import socket
 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Connect to the server

clientSocket.connect(("127.0.0.1",9090));

 

# Send data to server

data = "hello";

clientSocket.send(data.encode());



# Receive data from server


 