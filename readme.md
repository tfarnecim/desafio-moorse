<h1 align="center">Desafio moorse</h1>
<p align="center">Desenvolvido com o intuito de enviar e responder mensagens enviadas no whatsapp</p>

<br>

Tópicos importantes
===================
<!--ts-->
   * Sobre
   * Instalação
   * Como usar
      * Pré-requisitos
      * Funcionalidades
   * Exemplo de utilização
<!--te-->

<br>

## 1. Sobre

O programa é dividido em duas partes básicas, um programa simples de terminal que envia mensagens a partir de um login na conta do moorse, e outro que apenas recebe mensagens em uma url gerada pelo ngrok e retorna mensagens.

<br>

## 2. Instalação

Para a correta utilização do programa que envia mensagens, é necessária a obtenção do python e da biblioteca requests no computador. Seguem tutoriais para Linux e Windows.

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

Se tudo foi feito corretamente, o sistema está apto a utilizar a aplicação.

<br>

## 3. Como usar

Uma vez que tudo foi instalado corretamente, torna-se simples executar os programas.

A fim de executar o programa que envia as mensagens, certifique-se de estar na pasta raiz do repositório. Logo após, entre na pasta EnviandoMensagens e execute o arquivo ```main.py```.


<br>

## 4. Funcionalidades

O programa salvo em ```EnviandoMensagens/main.py``` que envia as mensagens  é capaz de:

- [x] Logar em uma conta da moorse
- [x] Resgatar todas as integrações de um usuário
- [x] Enviar mensagens para números de whatsapp
- [ ] Ler pensamentos
- [ ] Contar uma história

<br>

## 5. Exemplo de utilização

<br>
