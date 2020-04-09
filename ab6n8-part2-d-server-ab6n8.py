import socket
import json
import requests

HOST = ''
PORT = 8000
API_KEY = 'f5290b022644121eea08a712ba8b9bc4'
BASE_URL = 'https://api.darksky.net/forecast/'
params = '37.8267,-122.4233?units=si&exclude=currently,flags,hourly,minutely'


def server_connect():
    sock = socket.socket()
    server = sock.bind((HOST, PORT))
    sock.listen(1)
    print("Server is Listening on ", PORT)
    conn, addr = sock.accept()
    return conn


def server_messages(con):
    while True:
        msg = str(con.recv(1024).decode())
        msg = msg.lower()
        if msg == "bye":
            print(msg)
            con.send(str.encode("Server connection is closed"))
            con.close()
            next_con = server_connect()
            server_messages(next_con)
        elif msg == "weather":
            api_url = BASE_URL + API_KEY + '/' + params
            response = requests.get(api_url)
            json_response = response.json()
            repository = json_response['daily']['data']
            message = ''
            for i in range(3):
                message += str(repository[i]['temperatureLow']) + 'c/'
            message = 'Next Consecutive three days temperature : ' + message
            c.send(str.encode(message))
        else:
            print(msg)
            c.send(str.encode(msg))


def main():
    connection = server_connect()
    server_messages(connection)


if __name__ == '__main__':
    main()
