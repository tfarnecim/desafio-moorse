from conexoes import *
from flask import Flask
from flask import request
import requests

token_de_acesso = #insira seu token aqui

app = Flask(__name__)

@app.route("/webhooks", methods=["POST"])
def RecebendoEEnviandoMensagens():
	dados = request.get_json()
	if(dados["content"] == "$ola" and dados["status"] == "RECEIVED"):#só envia a mensagem caso ela seja um $ola
		nome_remetente = dados["contactUser"]["name"]
		numero_remetente = dados["contactUser"]["number"]
		mensagem = "Olá " + nome_remetente + ", sou um bot programado por Douglas Alves, sei que seu número é " + numero_remetente
		id_integracao = dados["integrationId"]
		enviarMensagem(id_integracao,numero_remetente,mensagem,token_de_acesso)
	return "OK"

if __name__ == '__main__':
    app.run(host="localhost", port=8080)

