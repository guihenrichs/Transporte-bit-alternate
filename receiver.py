from socket import socket, AF_INET, SOCK_DGRAM, timeout

#Função que recebe a mensagem do sender
def rec():
	#Guarda na variável porta a PORTA digitada
	porta = int(input('Digite a porta desejada entre 10001 e 11000: '))
	#Verifica se a PORTA está no range desejado, caso não solicita para digitar novamente
	while (porta < 10001) or (porta > 11000):
		print("A porta deve ser entre 10001 - 11000")
		porta = int(input('Digite a porta desejada entre 10001 e 11000: '))
	print ("Porta válida")

	#Abre o socket
	server_socket = socket(AF_INET, SOCK_DGRAM)
	server_socket.bind(('', porta))

	print("Esperando pela mensagem... ")

	#Variavel que recebe a mensagem que será sequencial
	msg = 0
	#Variavel que recebe a quantidade de mensagens que iremos receber
	qtd_msg = 1

	#Verifica se a quantidade de mensagens recebidas é diferente da mensagem recebida.
	#Quando a mensagem recebida for igual a quantidade de mensagens que iremos receber
	while msg != qtd_msg:
		#Coloca na variavel a mensagem recebido do sender
		received, client_address = server_socket.recvfrom(2048)
		message = received.decode()
		#Variavel que guarda a mensagem recebida localizada no 2 digito
		msg = message[1]
		#Variavel que guarda a quantidade de mensagens que iremos receber localizada no 3 digito
		qtd_msg = message[2]

		print("REC: " + message)
		#Se o sequencial for igual 0, o receiver mandará o mensagem ACK0
		if message[0] == "0":
			server_socket.sendto("ACK0".encode(), client_address)
			print("SENT: ACK0 \n")
		#Se o sequencial for igual 1, o receiver mandará o mensagem ACK1
		elif message[0] == "1":
			server_socket.sendto("ACK1".encode(), client_address)
			print("SENT: ACK1 \n")
	server_socket.close()

rec()
