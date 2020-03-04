from socket import socket, AF_INET, SOCK_DGRAM, timeout
import sys
import os
import platform

#Variavel que recebe o IP do servidor
global server_ip
#Variavel que recebe a PORTA
global porta
#Variavel que recebe a quantidade de mensagens a serem enviadas
global qtd_msg


#https://www.cybrary.it/blog/0p3n/ping-using-python-script/
#Função que recebe o IP e dá o PING de acordo com o sistema operacional
def ip_servidor():	
	while True:
		#Guarda na variável server_ip o IP digitado
		server_ip = input('Digite o IP do servidor : ')

		#Se o sistema operacional for Windows, dá o ping e guarda na variavel rep
		if platform.system() == "Windows":	
			rep = os.system('ping ' + server_ip +' -n 1')
			print ("Servidor Ok!!!")
			break
		#Se o sistema operacional for Linux, dá o ping e guarda na variavel rep
		else:
			rep = os.system('ping -c 1 ' + server_ip)
			print ("Servidor Ok!!!")
			break
		#Se o Ping não receber mensagem, pede para digitar novamente um IP válido
		while rep != 0:
			print ("Servidor não encontrado...")
			server_ip = input('Digite novamente o IP do servidor : ')
			if platform.system() == "Windows":	
				rep = os.system('ping ' + server_ip +' -n 1')
			else:
				rep = os.system('ping -c 1 ' + server_ip)
	return server_ip

#Função que recebe a PORTA
def porta_servidor():
	while True:
		#Guarda na variável porta a PORTA digitada
		porta = int(input('Digite a porta desejada entre 10001 e 11000: '))
		#Verifica se a PORTA está no range desejado, caso não solicita para digitar novamente
		while (porta < 10001) or (porta > 11000):
			print("A porta deve ser entre 10001 - 11000")
			porta = int(input('Digite a porta desejada entre 10001 e 11000: '))
		print ("Porta válida")
		break
	return porta

#Função que recebe a quantidade de mensagens a serem enviadas
def num_msgs():
	while True:
		#Guarda na variável quantidade de mensagens digitada
		qtd_msg = int(input('Digite a quantidade de mensagens entre 1 e 9: '))
		#Verifica se a quantidade de mensagem é menor que 9,  caso não solicita para digitar novamente
		while (qtd_msg > 9):
			print("O valor deve ser um numero inteiro entre 1 e 9")
			qtd_msg = int(input('Digite novamente a quantidade de mensagens entre 1 e 9: '))
		print ("Valor valido")
		break
	return qtd_msg	

#Função que enviad as mensagens para o servidor
def sender():
	 #Guarda na variavel o valor obtido da função que recebe o IP
	server_ip = ip_servidor()
	#Guarda na variavel o valor obtido da função que recebe a PORTA
	porta = porta_servidor() 
	#Guarda na variavel o valor obtido da função que recebe a quantidade de mensagens a serem enviadas
	qtd_msg = num_msgs() 
	#Coloca na variável o IP e PORTA para transmissão
	dest = (server_ip,porta) 
	#Abre o socket
	client_socket = socket(AF_INET, SOCK_DGRAM) 

	#Variavel que conta a quantidade de mensagens que foram enviadas
	count = 1
	#Variavel sequencial das mensagens enviadas
	seqno = 0
	#Variavel que envia começando em 1 até ser igual a quantidade de mensagem
	data = 1

	#Loop para envio da mensagem enquanto o valor do contador for menos ou igual a quantidade de mensagens
	while (count <= qtd_msg):
		#Verifica se o sequencial 0 é igual ao valor ACK0
		if seqno == 0:
			#Concatena a mensagem para ser enviada ao servidor
			mensagem = str(seqno) + str(data) + str(qtd_msg)
			#Envia a mensagem para o servidor
			client_socket.sendto(mensagem.encode(), dest)
			#Printa no terminal a mensagem concatenada
			print("SENT: " + str(seqno) + str(data) + str(qtd_msg))
			try:
				#Configura o timeout em 1 segundo
				client_socket.settimeout(1)
				#Recebe o ack do servidor e guarda na variavel
				resp, server_ip = client_socket.recvfrom(2048)
				resp = resp.decode()
				#Guarda na variavel o valor vindo após a palavra ACK
				ack = resp[3]
				#Se o ACK for ACK0, muda o sequencial para 1, incremente o valor da mensagem e soma +1 ao contador
				if ack == "0":
					print("RECV: " + resp + "\n")
					seqno = 1
					data = data + 1
					count += 1
			#Caso não recebe o ACK, printa no terminal TIMEOUT		
			except timeout:
				print("RECV: Timeout")

		#Verifica se o sequencial 1 é igual ao valor ACK1
		elif seqno == 1:
			mensagem = str(seqno) + str(data) + str(qtd_msg)				
			client_socket.sendto(mensagem.encode(), dest)
			print("SENT: " + str(seqno) + str(data) + str(qtd_msg))
			try:
				#Configura o timeout em 1 segundo
				client_socket.settimeout(1)
				#Recebe o ack do servidor e guarda na variavel
				resp, server_ip = client_socket.recvfrom(2048)
				resp = resp.decode()
				#Guarda na variavel o valor vindo após a palavra ACK
				ack = resp[3]
				#Se o ACK for ACK1, muda o sequencial para 0, incremente o valor da mensagem e soma +1 ao contador
				if ack == "1":
					print("RECV: " + resp + "\n")
					seqno = 0
					data = data + 1
					count += 1
			#Caso não recebe o ACK, printa no terminal TIMEOUT
			except timeout:
				print("RECV: Timeout")
	#Fecha o socket				
	client_socket.close()

sender()
