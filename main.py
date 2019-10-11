# Base de uma mensagem
# [02/05/19 15:00:56] Pablo: nao sou obrigado a viver num mundo onde o mormaço é rei e acha q ta certo
# [04/05/19 00:20:22] ‪+55 15 98124‑6169‬: KKKKKKKK
# ‎[04/05/19 02:56:42] Cosi: ‎sticker omitted

def limpaDados(dados):
	for i in range(0, len(dados)):
		dados[i] = dados[i].replace('\u200a', '').replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\u200e', '').replace('\u200f', '').replace('\u202a', '').replace('\u202b', '').replace('\u202c', '').replace('\u202d', '').replace('\u202e', '').replace('\u202f', '')

def separaMensagem(mensagem):
	valida = False
	nome = "dummy"
	tipo = "dummy"
	dados = mensagem.split()
	
	if dados:
		limpaDados(dados)
		valida = dados[0]

		# Pegar nome pelo : (usar string.endswith())
		if valida.startswith('['):
			valida = True
			nome = dados[2].replace(':', '')

			# Caso seja um telefone e não um contanto
			if nome.replace("+", "").isdigit():
				nome = nome + " " + dados[3] + " " + dados[4].replace(":", "")
				tipo = dados[5]

			else:
				tipo = dados[3]


		else:
			valida = False

	return valida, nome, tipo

def organiza(Arq):

	usuarios = {}
	linha = Arq.readline()

	while linha != "":
		linha = Arq.readline()
		valida, nome, tipo = separaMensagem(linha)
		
		if valida:
			if nome not in usuarios:
				usuarios[nome] = {
					'mensagem' : 0,
					'sticker' : 0,
					'image' : 0,
					'audio' : 0,
				}			

			if tipo == "sticker":
				usuarios[nome]['sticker'] = usuarios[nome]['sticker'] + 1
			elif tipo == "image":
				usuarios[nome]['image'] = usuarios[nome]['image'] + 1
			elif tipo == "audio":
				usuarios[nome]['audio'] = usuarios[nome]['audio'] + 1
				
			usuarios[nome]['mensagem'] = usuarios[nome]['mensagem'] + 1	
				
	return usuarios
	
def printEstatisticas():
	# sorted(dic.items(), key=lambda dic: dic[1]['mensagens'])
	return "placeholder"

# MAIN
opcao = input("Selecione o arquivo para estatísticas: ")

try:
	Arq = open(opcao, "r")
except FileNotFoundError:
	print("O arquivo digitado não existe (você colocou o caminho correto e a extensão correta?)")

usuarios = organiza(Arq)
for u in usuarios:
	print(u, usuarios[u])