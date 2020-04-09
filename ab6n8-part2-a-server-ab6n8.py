# To import the socket module
import socket
HOST = socket.gethostbyname(HOST)

# To initiate port number above 1024
PORT = 8000
# To create socket object called 'server'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# To bind the IP Address and Port number to the server
server.bind((HOST, PORT))
# To configure the number of clients the server can listen to simultaneously
server.listen(1)
print("Server waiting for connection from the client on port:", PORT)
# To accept new connection from the client
conn, address = server.accept()
# To print the address of the connected client to server
print("Connection established with: " + str(address))
while True:
    # To receive data stream from the connected client
    data = conn.recv(1024).decode()
    if(data == "exit"):
        # To print the data received from the client
        print("Message received from client: " + str(data))
        # To close the connection with server
        conn.close()
        print("connection closed with client")               # Print statement
        break
    else:
        print("Message received from client: " + str(data))  # Print statement
