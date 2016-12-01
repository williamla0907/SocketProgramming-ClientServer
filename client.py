# Created by William La - williamla0907@gmail.com
# at 10:54 PM 11-30-2016
# This program is an simple example of client-server communication through
# socket.
# In this client.py file, I am going to create a simple client that will
# connect to my defined server in server.py file.
import socket

# Innitialize an server-to-be object
s = socket.socket()

# Define the address and port that my client will connect to
server = "127.0.0.1"
port = 8001

# Connect to the server and print the received message
s.connect((server,port))
print(s.recv(1024).decode())
s.close()
