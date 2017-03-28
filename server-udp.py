from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server Ready")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    serverSocket.sendto(message.upper(), clientAddress)
