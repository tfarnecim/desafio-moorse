from conexoes import *
from flask import Flask
from flask import request
import requests

token_de_acesso = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0Zm5zb25nc0BnbWFpbC5jb20iLCJpZENsaWVudCI6IjA5OTgzMzliLTcxM2UtNDA2Zi05N2Q5LTU0MDUzN2FjZmZhNCIsImNyZWF0ZWQiOjE2Mzg0NjEyMDcxODEsInJvbGVzIjpbIlJPTEVfQVBJIiwiUk9MRV9EQVNIQk9BUkQiLCJST0xFX0RBU0hCT0FSRF9HUk9VUFMiLCJST0xFX0dST1VQUyIsIlJPTEVfSU5URUdSQVRJT05fVVNFUiIsIlJPTEVfVFJJQUwiLCJST0xFX1VTRVJTIiwiUk9MRV9XRUJIT09LIl0sImlkIjoyMDcsImV4cCI6MTY2OTk5NzIwN30.l2sTWiiUP48j1HLqXH5V0P2hMmJiAs7VtLSo6E9iIN8Qu6HWEsv_GoRdaI-U_kBoMIe0uUApB1LuSeERK7Z9bQ"

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

#http://70a4-167-250-157-99.ngrok.io