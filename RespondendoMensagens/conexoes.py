import requests
import json

prefixo = "https://api.moorse.io/"

def pegaToken(email,senha):
	dados = {'login': email, 'senha': senha}
	cabecalho = {"Accept": "application/json","Content-Type": "application/json"}
	response = requests.request("POST", prefixo + "oauth/login", json=dados, headers=cabecalho)
	return json.loads(response.text)


def pegarIntegracoes(token):
	cabecalho = {"Accept": "application/json","Authorization": "Bearer " + token}
	response = requests.request("GET", prefixo + "v2/whatsapp", headers=cabecalho)
	return json.loads(response.text)


def enviarMensagem(id_integracao, numero_destinatario, mensagem, token):
	dados = {'to': numero_destinatario, 'body': mensagem}
	cabecalho = {"Accept": "application/json", "Content-Type": "application/json","Authorization": "Bearer "+ token}
	response = requests.request("POST", prefixo + "v2/whatsapp/" + id_integracao + "/send-message", json=dados, headers=cabecalho)
	return json.loads(response.text)