# Created by William La - williamla0907@gmail.com
# at 10:54 PM 11-30-2016
# This program is an simple example of client-server communication through
# socket.
# In this server.py file, I am going to create a basic server that will
# listen for connections and print out clients and send welcome messages
# to client. A maximum of 5 concurrent clients can connect at a time.
import socket # Standard Python library for socket programming

# Innitialize an server-to-be object
s = socket.socket()

# Define the server's address and port
Server = 'localhost'
Port = 8001

#Bind the address and port to the innitialized socket object
s.bind((Server,Port))

# Active the server with maximum of 5 connecting clients at a time
s.listen(5)

# Print out clients' info and send a welcome message
while True:
    c,address = s.accept()
    print("We got connect from", address)
    # For python3, the sending package must be encode, and the receiving
    # package must be decoded.
    c.send("You are connected".encode())
    c.close()
