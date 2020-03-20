import socket
def client():
    host = socket.gethostbyname('192.168.1.26')  # as both code is running on same pc
    port = 5000  # socket server port number

    sock = socket.socket()  # instantiate
    sock.connect((host, port))  # connect to the server

    message = input(" -> \n")  # take input
    while True:  
            if message == "Bye from Client Anmisha":
                          sock.send(message.encode())
                          data = sock.recv(1024).decode()
                          print(data)
                          if(data == "Bye from Server Anmisha"):
                                  break
                          else:
                                  message=input("Take another input \n")
            elif message == "Hello from Client Anmisha":
                           sock.send(message.encode())
                           data= sock.recv(1024).decode()
                           print(data)
                           message=input("Take another input \n")
            else:
                           sock.send(message.encode())
                           data = sock.recv(1024).decode()
                           print(data)
                           message = input("Enter message \n")

    sock.close()  # close the connection
if __name__ == '__main__':
    client()
