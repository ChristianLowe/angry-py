from socket import *

serverAddress = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

message = bytes(input('Input sentence: '), 'UTF-8')
clientSocket.send(message)

serverMessage = clientSocket.recv(2048)

print(serverMessage.decode('UTF-8'))
clientSocket.close()
