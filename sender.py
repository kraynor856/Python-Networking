import socket
import os


h_name = os.uname()

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);



# Connect to the server

clientSocket.connect(("192.168.1.96",9090));

 

# Send data to server

data = "hello";
data2 = h_name;
clientSocket.send(data.encode());
clientSocket.send(data2.encode());



# Receive data from server


 