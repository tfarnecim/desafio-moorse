from os import system, name

def limpa():#verifica se o sistema é linux, mac ou windows e limpa a tela de acordo, não tenho certeza se funciona para todos os SOs
	if(name == "nt"):
		system("cls")
	else:
		system("clear")

def mostra(mensagem, espaco):#Mostra na tela uma mensagem e dá espaços dos lados
	espaco-=2#duas barrinhas vao ficar nos cantos
	if(len(mensagem) > espaco):
		return ""
	sobra = espaco - len(mensagem)
	lado1 = int(sobra/2)
	lado2 = sobra-lado1
	return "|" + str(lado1*" ") + mensagem + str(lado2*" ") + "|"

def telaPrincipal(aviso, email_sessao, nome_integracao):#Cria a tela principal
	if(email_sessao!=""):
		print("EMAIL DA SESSAO : " + email_sessao)	

	if(nome_integracao!=""):
		print("INTEGRACAO ATUAL: " + nome_integracao)

	print("-="*25+"-")#observe que serão printados 51 caracteres 2*25+1 = 51
	print(mostra("",51))
	print(mostra("BOT MOORSE",51))
	print(mostra("",51))
	print(mostra("[1]REALIZAR LOGIN",51))
	print(mostra("[2]ESCOLHER INTEGRACAO",51))
	print(mostra("[3]ENVIAR MENSAGEM",51))
	print(mostra("",51))

	if(aviso!=""):
		print(mostra(aviso,51))
		print(mostra("",51))
		
	print("-="*25+"-")