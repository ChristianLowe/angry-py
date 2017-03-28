from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server Ready")

while True:
    connection, clientAddress = serverSocket.accept()

    messageBuffer = connection.recv(2048)
    connection.send(messageBuffer.upper())
    connection.close()
