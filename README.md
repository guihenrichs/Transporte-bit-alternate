# Tansporte-bit-alternate
Neste projeto foi implementado o protocolo de transferência confiável de dados. Foi criado um arquivo sender e um receiver baseados na máquina de estados do protocolo em sua última variação rtd3.0. Neste projeto não foi implementado o checksum.

## Guia de Introdução 
Para executar o projeto, será necessário os seguintes programas:
- Python 3.8.2
- Prompt de Comando do Windows
- Terminal do Linux

### Instação
- Para Windows:  
Inicialmente deverá fazer o download da versão mais recente do Python acessando a página https://www.python.org/downloads/  
Em seguida, você precisa executar o instalador baixado.  
A primeira tela do instalador, nos oferece a opção de adicionar o python 3.7 na variável de ambiente PATH.  
Marcar essa opção significa que o comando python poderá ser executado pela linha de comandos. 
Após marcar essa opção clicar na opção Install Now.  
Após a instalação concluir, basta clicar no botão Close e acabou! O python já estará instalado no seu Windows.  
Para verificar se a instalação do Python foi bem-sucedida, pesquise no menu iniciar por "cmd" e clique duas vezes para abri-lo.  
Digite o seguinte comando: python -- version  
Este comando retornará a versão do python que está instalada em sua máquina.

- Para Linux:  
Neste sistema operacional o python já vem habilitado não necessitando de instalação.

## Rodando os testes
### No Windows
Copie e cole o arquivo sender.py e receiver.py na sua Área de Trabalho. O arquivo receiver.py pode ser enviado para uma máquina virtualizada ou até mesmo para outra máquina desde que estas estejam conectadas na internet.  
Pesquise no menu iniciar por "cmd" e clique duas vezes para abri-lo.  
Digite o seguinte comando: ipconfig. Este comando irá fornecer o IP da sua máquina caso rode o arquivo sender.py nela ou o IP do servidor. Anote a IP do servidor no campo Endereço IPv4.  
Agora, digite o seguinte comando: cd Desktop. Isto irá direcionar o pasta Desktop no seu prompt de comando.  
Abra outra tela do prompt de comando. Nesta outra tela digite o comando: cd Desktop. Caso seja feita em outro servidor, cole o arquivo receiver.py no desktop deste servidor. Abra o prompt de comando e solicite o ip enviando o comando ipconfig e anote o IP deste servidor.  
Na tela do servidor, digite o comando: receiver.py. Em seguida escolha a porta. Este valor deverá ser entre 10001 e 11000.  
Pronto, o servidor estará aguardando pela mensagem recebida.  
Na tela do sender, digite o seguinte comando: sender.py. Em seguida, digite o IP do seu servidor, você irá vizualizar o ping no servidor para saber se o host existe. Após o IP, digite a porta (esta deverá ter o mesmo valor escolhido no servidor. Valor deverá ser entre 10001 e 11000). Agora digite a quantidade de mensagens que o sender enviará para o receiver.  
Após feito isto, você irá vizualizar o sender enviando a mensagem e recebendo o ACK até a quantidade escolhida. Caso o servidor não esteje com o prompt aberto ou não ter perdido a conexão, você irá perceber a mensagem de TIMEOUT até que a conexão seja restabelecida.  
Na tela do servidor, você irá vizualizar o receiver recebendo e enviando o ACK da mensagem.  

### No Linux
Copie e cole o arquivo sender.py e receiver.py na sua Área de Trabalho. O arquivo receiver.py pode ser enviado para uma máquina virtualizada ou até mesmo para outra máquina desde que estas estejam conectadas na internet.  
Abra o terminal do linux.  
Digite o seguinte comando: ifconfig. Este comando irá fornecer o IP da sua máquina caso rode o arquivo sender.py nela ou o IP do servidor. Anote a IP do servidor no campo inet addr:.  
Agora, digite o seguinte comando: cd Desktop. Isto irá direcionar o pasta Desktop no seu terminal.  
Abra outra tela do terminal. Nesta outra tela digite o comando: cd Desktop. Caso seja feita em outro servidor, cole o arquivo receiver.py no desktop deste servidor. Abra o terminal e solicite o ip enviando o comando ifconfig e anote o IP deste servidor.  
Na tela do servidor, digite o comando: python receiver.py. Em seguida escolha a porta. Este valor deverá ser entre 10001 e 11000.  
Pronto, o servidor estará aguardando pela mensagem recebida.  
Na tela do sender, digite o seguinte comando: python sender.py. Em seguida, digite o IP do seu servidor, você irá vizualizar o ping no servidor para saber se o host existe. Após o IP, digite a porta (esta deverá ter o mesmo valor escolhido no servidor. Valor deverá ser entre 10001 e 11000). Agora digite a quantidade de mensagens que o sender enviará para o receiver.  
Após feito isto, você irá vizualizar o sender enviando a mensagem e recebendo o ACK até a quantidade escolhida. Caso o servidor não esteje com o prompt aberto ou não ter perdido a conexão, você irá perceber a mensagem de TIMEOUT até que a conexão seja restabelecida.  
Na tela do servidor, você irá vizualizar o receiver recebendo e enviando o ACK da mensagem.
