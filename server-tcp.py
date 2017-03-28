from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server Ready")
connection, clientAddress = serverSocket.accept()

while True:
    messageBuffer = connection.recv(2048).upper()

    connection.send(messageBuffer)

    if messageBuffer == b'QUIT':
        break

connection.close()
serverSocket.close()
