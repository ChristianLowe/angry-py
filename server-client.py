from socket import *
from multiprocessing import Process
import sys
import os
import threading

def clientProcessFunction(fd, serverProcess, serverSocket):
	sys.stdin = os.fdopen(fd) # Read from STDIN

	while True:
		message = bytes(input('Input sentence (or quit): '), 'UTF-8')

		serverSocket.send(message)
	
		serverMessage = serverSocket.recv(2048).decode('UTF-8')
		print(serverMessage)

def serverProcessFunction(clientProcess, serverSocket):
	while True:
		messageBuffer = serverSocket.recv(2048).upper()

		serverSocket.send(messageBuffer)

		if messageBuffer == b'QUIT':
			break

if __name__ == '__main__':

	serverSocket = socket(AF_INET, SOCK_STREAM)

	if len(sys.argv) == 3:
		serverName = sys.argv[1]
		connectionPort = int(sys.argv[2])
		serverSocket.connect((serverName, connectionPort))
	elif len(sys.argv) == 2:
		port = int(sys.argv[1])
		serverSocket.bind(('', port))
		serverSocket.listen(1)
		serverSocket, clientAddress = serverSocket.accept()
	else:
		print("Usage for first client: python server-client.py <port>")
		print("Usage for second client: python server-client.py localhost <port>")
		sys.exit(0)

	clientProcess = None
	serverProcess = Process(target = serverProcessFunction, args=(clientProcess, serverSocket))
	clientProcess = Process(target = clientProcessFunction, args=(sys.stdin.fileno(), serverProcess, serverSocket))

	serverProcess.start()
	clientProcess.start()

	serverProcess.join()
	clientProcess.terminate()

	serverSocket.close()