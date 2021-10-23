import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = ''
port = 8888
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode("""Welcome to the CTF Server
If you forgot password rockyou will help you to remind \n"""))
    while True:
        data = connection.recv(2048)
        if str("".join(data.decode('utf-8').split())) != str("naruto"):
            print(data.decode('utf-8'))
            reply = 'Server Says: The password is wrong, Try again\n' 
        else:
            reply = "ctfUTM{s1mp1e_brut84rc8""}""\n"
            connection.sendall(str.encode(reply))
            break
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()