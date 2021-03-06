from socket import *

serverAddress = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = bytes(input('Input sentence: '), 'UTF-8')

    clientSocket.sendto(message, (serverAddress, serverPort))

    serverMessage, _ = clientSocket.recvfrom(2048)
    print(serverMessage.decode('UTF-8'))

    if serverMessage == b'QUIT':
        break

clientSocket.close()
