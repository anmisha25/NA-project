# To import the socket module
import socket
HOST = socket.gethostbyname(HOST)

# To initiate port number above 1024
PORT = 8000
# To create socket object called 'client'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# To connect to the server
client.connect((HOST, PORT))
while True:
    msg = str(
        input("Do you want to send  a message to the server?(y/n) : ")).lower()
    if(msg == "y"):
        # To enter the message to be sent to server
        client_msg = input("Enter your message : ")
        # To send the message to server
        client.send(client_msg.encode())
    else:
        client.send("exit".encode())
        # To close the connection with server
        client.close()
        # Print statement
        print("connection closed with server")
        break
