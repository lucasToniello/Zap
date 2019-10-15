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

	print("\n\n\n")
	print("Estatísticas do grupo:", linha, "\n\n\n")

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
	
def printEstatisticas(usuarios, opcao):

	if opcao == "N":
		usuarios = sorted(usuarios.items(), key=lambda x: x[0], reverse=True)

	elif opcao == "M":
		usuarios = sorted(usuarios.items(), key=lambda x: x[1]['mensagem'], reverse=True)

	elif opcao == "S":
		usuarios = sorted(usuarios.items(), key=lambda x: x[1]['sticker'], reverse=True)

	elif opcao == "I":
		usuarios = sorted(usuarios.items(), key=lambda x: x[1]['image'], reverse=True)

	elif opcao == "A":
		usuarios = sorted(usuarios.items(), key=lambda x: x[1]['audio'], reverse=True)

	print("\n")
	for u in usuarios:
		print(u)

def toCsv(usuarios):
	Saida = open("mktable/dados.csv", "w")
	Saida.write("Nome;Número de Mensagens;Stickers;Imagens;Áudios\n")

	for u in usuarios:
		Saida.write("{};{};{};{};{}\n" .format(u, usuarios[u]['mensagem'], usuarios[u]['sticker'], usuarios[u]['image'], usuarios[u]['audio']))

# MAIN
opcao = input("Selecione o arquivo para estatísticas: ")

try:
	Arq = open(opcao, "r")
except FileNotFoundError:
	print("O arquivo digitado não existe (você colocou o caminho correto e a extensão correta?)")
	# Encerrar o programa aqui

opcao = input("Escolha a opção de organização: [N] Nome [M] Número de mensagens [S] Número de stickers [I] Número de imagens/mídias [A] Número de áudios: ")

usuarios = organiza(Arq)
toCsv(usuarios)