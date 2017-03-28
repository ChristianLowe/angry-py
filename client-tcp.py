from socket import *

serverAddress = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

while True:
    message = bytes(input('Input sentence (or quit): '), 'UTF-8')

    clientSocket.send(message)
    
    serverMessage = clientSocket.recv(2048).decode('UTF-8')
    print(serverMessage)

    if serverMessage == 'QUIT':
        break

clientSocket.close()
