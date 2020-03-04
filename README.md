# Tansporte-bit-alternate
Neste projeto foi implementado o protocolo de transferência confiável de dados. Foi criado um arquivo sender e um receiver baseados na máquina de estados do protocolo em sua última variação rtd3.0. Neste projeto não foi implementado o checksum.

## Guia de Introdução 
Para executar o projeto, será necessário os seguintes programas:
- Python 3.8.2
- Prompt de Comando do Windows
- Terminal do Linux

## Descrição do programa
O protocolo foi implementado sobre sockets UDP. Ele possui um nível de aplicação  a transferência de dados que não está disponível neste protocolo de transporte.  
O projeto contem dois aquivos escritos na linguagem python: sender.py e receiver.py. Estes arquivos rodam tanto no sistema operacional Linux quanto em Windows.  
O arquivo **SENDER** recebe três argumentos de linha de comando: IP do receiver aonde fará um ping no servidor para saber se o host existe. Porta no receiver que deverá ser um numero inteiro entre 10001 e 11000. E quantidade de mensagens a serem enviadas podendo ser qualquer numero inteiro. Qualquer argumento que não seja valido o programa exibe um erro ao usuário.  
O sender usa um único socket UDP para enviar as mensagens no seguinte formato SEQNO DATA MSGS, aonde:  
1. SEQNO é o número de sequência do pacote tendo o valor 0 ou 1.  
2. DATA são números começando em um e incrementando até a quantidade definida pelo usuário em MSGS.  
3. MSGS que é o número todal de até 9 mensagens a serem enviadas.  

Este programa usa um timeout de 1 segundo para retransmissão de mensagens caso o sender não receba o ACK de identificação da mensagem.  
O programa é encerrado quando o ACK para a última mensagem é recebido.  
Para cada mensagem trocada, o sender imprime as seguintes mensagens no terminal:  
SENT: mensagem que foi enviada  
RECV: mensagem que foi recebida ou timeout  
O arquivo **RECEIVER** recebe um argumento que é o número da porta onde ele espera pela mensagem. Este arquivo deverá ser um numero inteiro entre 10001 e 11000.  
O receiver envia uma mensagem de ACK no formato ACK ACKno, onde ACKno é o número da mensagem sendo reconhecida.  
O receiver identifica o número de mensagens únicas que irá tratar através do campo MSGS no pacote enviado pelo sender.  
O receiver encerra a execução quando recebe a última mensagem do sender.  
O receiver imprime as seguintes mensagens no terminal:  
RECV: mensagem recebida  
SENT: mensagem enviada

## Instação
- Para Windows:  
Inicialmente deverá fazer o download da versão mais recente do Python acessando a página https://www.python.org/downloads/  
Em seguida, você precisa executar o instalador baixado.  
A primeira tela do instalador, nos oferece a opção de adicionar o python 3.7 na variável de ambiente PATH.  
Marcar essa opção significa que o comando python poderá ser executado pela linha de comandos. 
Após marcar essa opção clicar na opção Install Now.  
Após a instalação concluir, basta clicar no botão Close e acabou! O python já estará instalado no seu Windows.  
Para verificar se a instalação do Python foi bem-sucedida, pesquise no menu iniciar por "cmd" e clique duas vezes para abri-lo.  
Digite o seguinte comando: python --version  
Este comando retornará a versão do python que está instalada em sua máquina.

- Para Linux:  
Neste sistema operacional o python já vem habilitado não necessitando de instalação.

## Rodando os testes
### No Windows
Copie e cole o arquivo sender.py e receiver.py na sua Área de Trabalho. O arquivo receiver.py pode ser enviado para uma máquina virtualizada ou até mesmo para outra máquina desde que estas estejam conectadas na internet.  
Pesquise no menu iniciar por "cmd" e clique duas vezes para abri-lo.  
Digite o seguinte comando: ipconfig. Este comando irá fornecer o IP desta máquina.  
Agora, digite o seguinte comando: cd Desktop. Isto irá direcionar a pasta Desktop no seu prompt de comando.  
Abra outra tela do prompt de comando. Nesta outra tela digite o comando: cd Desktop. Caso seja feita em outro servidor, cole o arquivo receiver.py no desktop deste servidor. Abra o prompt de comando e solicite o ip enviando o comando ipconfig e anote o IP desta máquina.  
Na tela do servidor, digite o comando: receiver.py. Em seguida escolha a porta. Este valor deverá ser entre 10001 e 11000.  
Pronto, o servidor estará aguardando pela mensagem recebida.  
Na tela do sender, digite o seguinte comando: sender.py. Em seguida, digite o IP do seu servidor, você irá vizualizar o ping no servidor para saber se o host existe. Após o IP, digite a porta (esta deverá ter o mesmo valor escolhido no servidor. Valor deverá ser entre 10001 e 11000). Agora digite a quantidade de mensagens que o sender enviará para o receiver.  
Após feito isto, você irá vizualizar o sender enviando a mensagem e recebendo o ACK até a quantidade escolhida, caso o servidor não esteje com o prompt aberto ou não ter perdido a conexão, você irá perceber a mensagem de TIMEOUT até que a conexão seja restabelecida.  
Na tela do servidor, você irá vizualizar o receiver recebendo e enviando o ACK da mensagem.  

### No Linux
Copie e cole o arquivo sender.py e receiver.py na sua Área de Trabalho. O arquivo receiver.py pode ser enviado para uma máquina virtualizada ou até mesmo para outra máquina desde que estas estejam conectadas na internet.  
Abra o terminal do Linux.  
Digite o seguinte comando: ifconfig. Este comando irá fornecer o IP desta máquina.  
Agora, digite o seguinte comando: cd Desktop. Isto irá direcionar a pasta Desktop no seu terminal.  
Abra outra tela do terminal. Nesta outra tela digite o comando: cd Desktop. Caso seja feita em outro servidor, cole o arquivo receiver.py no desktop deste servidor. Abra o terminal e solicite o ip enviando o comando ifconifg e anote o IP desta máquina.  
Na tela do servidor, digite o comando: python receiver.py. Em seguida escolha a porta. Este valor deverá ser entre 10001 e 11000.  
Pronto, o servidor estará aguardando pela mensagem recebida.  
Na tela do sender, digite o seguinte comando: python sender.py. Em seguida, digite o IP do seu servidor, você irá vizualizar o ping no servidor para saber se o host existe. Após o IP, digite a porta (esta deverá ter o mesmo valor escolhido no servidor. Valor deverá ser entre 10001 e 11000). Agora digite a quantidade de mensagens que o sender enviará para o receiver.  
Após feito isto, você irá vizualizar o sender enviando a mensagem e recebendo o ACK até a quantidade escolhida, caso o servidor não esteje com o terminal aberto ou não ter perdido a conexão, você irá perceber a mensagem de TIMEOUT até que a conexão seja restabelecida.  
Na tela do servidor, você irá vizualizar o receiver recebendo e enviando o ACK da mensagem. 

## Autor
Guilherme Henrichs
