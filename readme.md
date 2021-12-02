
# Desafio moorse
Desenvolvido com o intuito de enviar e responder mensagens enviadas no whatsapp

<br>

Tópicos importantes
===================
<!--ts-->
   * Sobre
   * Instalação
   * Como usar
   * Funcionalidades
   * Exemplo de utilização
<!--te-->

<br>

## 1. Sobre

O programa é dividido em duas partes básicas, um programa simples de terminal que envia mensagens livremente a partir de um login na conta do moorse, e outro que apenas recebe requisições HTTP na porta 8080 do localhost (estas requisições são enviadas pela API da moorse e redirecionadas para o localhost pelo ngrok), verifica se a requisição foi uma mensagem $ola recebida e retorna uma mensagem para o usuário que a enviou.

Experimento mental:

O usuário João de número de celular 83999887766 enviou a mensagem $ola para um usuário com webhook da moorse e o programa funcionando.

João receberá a seguinte mensagem ```Olá João, sou um bot programado por Douglas Alves, sei que seu número é 83999887766```.

<br>

## 2. Instalação

Para a correta utilização da aplicação, é necessária a obtenção do python e das biblioteca requests e flask no computador. Seguem tutoriais para Linux e Windows.

Para instalar no Linux abra o terminal e execute os seguintes comandos:

1. Instale o python 3;

```sudo apt-get install python3```

2. Instale o gerenciador de pacotes do python;

```sudo apt-get install python3-pip```

3. Instale a biblioteca necessária para a realização da comunicação com a API.

```pip install requests```

Para instalar no Windows:

1. Siga os passos mostrados no <a href="https://python.org.br/instalacao-windows/">site do python</a> para a devida instalação do python 3;
2. Abra o cmd do Windows (Tecle Windows+r e na caixa *executar* digite cmd);
3. No cmd digite ```pip install requests```.

Logo após ter instalado python, pip e biblioteca requests, execute o último comando no terminal/cmd:

```pip install flask```

Este último serve para instalar o flask, é o que vamos utilizar para receber as requisições HTTP da API da moorse.

Se tudo foi feito corretamente, o sistema está apto a utilizar a aplicação.

<br>

## 3. Como usar

Uma vez que tudo foi instalado corretamente, torna-se simples executar os programas.

O programa que envia mensagens livremente fica na pasta ```EnviandoMensagens```, para utilizá-lo você deve executar o arquivo nomeado de ```main.py``` com o comando ```python3 main.py```.

O programa que recebe mensagens e responde elas localiza-se na pasta ```RecebendoMensagens```, para utilizá-lo você deve  abrir o arquivo nomeado de ```main.py```  e ir até a linha 6 do código-fonte, nesta linha você deve inserir seu token (ele pode ser obtido no dashboard do site da moorse) na variável *token_de_acesso*, lembre-se de colocar o token entre aspas para que o python reconheça-o como string.

Após isso, você deve ligar o <a href="https://ngrok.com/">ngrok</a>, configurar o webhook no <a href="https://app.moorse.io/">site da moorse</a> e seu programa está apto a ser ligado. Para executar o programa vá até a pasta ```RecebendoMensagens``` e execute o arquivo ```main.py``` com o comando ```python3 main.py```

*OBS: é importante observar que o programa localizado em ```RecebendoMensagens/main.py``` responde as mensagens apenas se o programa receber uma mensagem $ola no whatsapp, assim como é descrito na linha 13 deste arquivo, caso contrário ele não responde nada.*

<br>

## 4. Funcionalidades

O programa salvo em ```EnviandoMensagens/main.py``` que envia as mensagens  é capaz de:

- [x] Logar em uma conta da moorse
- [x] Resgatar todas as integrações de um usuário
- [x] Enviar mensagens para números de whatsapp
- [ ] Ler pensamentos
- [ ] Contar uma história

O programa salvo em ```RecebendoMensagens/main.py``` que recebe as mensagens enviadas a uma integração e responde de acordo é capaz de:

- [x] Conectar-se à API da moorse
- [x] Receber requisições HTTP da API
- [x] Responder usuários que enviem a mensagem $ola para a integração
- [ ] Ouvir música
- [ ] Ler um livro

<br>

## 5. Exemplo de utilização

<br>
