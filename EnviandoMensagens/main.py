from os import system, name
import requests
import json
import time

from exibicao import *
from conexoes import *

#O programa não foi feito para resistir a strings sendo digitadas na tela principal
#Digite inteiros válidos e ele funcionará corretamente
email_sessao = ""
senha_sessao = ""
id_integracao = ""
nome_integracao = ""
aviso = ""
token = ""

while(1):

	limpa()
	telaPrincipal(aviso, email_sessao, nome_integracao)

	opcao = int(input())

	if(opcao==1):

		limpa()

		email = input("Digite seu login no moorse: ")
		senha = input("Digite sua senha no moorse: ")

		retorno = pegaToken(email,senha)

		if(retorno["data"] == None):
			aviso = "UM ERRO OCORREU DURANTE O LOGIN :'("
		else:
			token = retorno["data"]
			aviso = "LOGIN EFETUADO COM SUCESSO :D"
			email_sessao = email
			senha_sessao = senha

	elif(opcao==2):
		
		if(token==""):
			aviso = "LOGUE ANTES DE SELECIONAR INTEGRACOES!"
			continue

		limpa()
		retorno = pegarIntegracoes(token)

		nomes_integracoes    = []
		ids_integracoes      = []
		dados_integracoes    = retorno["data"]["content"]
		integracao_escolhida = -1

		for i in range(len(dados_integracoes)):
			nomes_integracoes.append(dados_integracoes[i]["name"])
			ids_integracoes.append(dados_integracoes[i]["id"])

		while(integracao_escolhida < 1 or integracao_escolhida > len(dados_integracoes)):
			limpa()
			for i in range(len(nomes_integracoes)):
				print("["+str(i+1)+"] " + nomes_integracoes[i])

			print("")
			integracao_escolhida = int(input("Selecione uma das integracoes acima\n[Sao validos numeros de 1 a " + str(len(nomes_integracoes)) + "]\n\n"))

		id_integracao   = ids_integracoes[integracao_escolhida-1]
		nome_integracao = nomes_integracoes[integracao_escolhida-1]

		aviso = "ENTROU"

	elif(opcao==3):

		if(id_integracao==""):
			aviso = "SELECIONE UMA INTEGRACAO"
			continue		

		limpa()
		
		print("Integracao escolhida: " + nome_integracao + "\n")
		numero_destinatario = input("Numero do destinatario: ")
		mensagem_envio = input("Mensagem desejada: ")

		enviarMensagem(id_integracao, numero_destinatario, mensagem_envio, token)
		#A própria api da moorse não trata erros no número digitado, não há como eu consiga tratar
		#Todas as mensagens serão consideradas enviadas

		aviso = "MENSAGEM COLOCADA NA FILA"

	else:
		limpa()
		quit()