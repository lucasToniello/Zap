# Base de uma mensagem
# [02/05/19 15:00:56] Pablo: nao sou obrigado a viver num mundo onde o mormaço é rei e acha q ta certo
# [04/05/19 00:20:22] ‪+55 15 98124‑6169‬: KKKKKKKK
# ‎[04/05/19 02:56:42] Cosi: ‎sticker omitted
# ‎[04/05/19 02:56:42] Lucas Toniello: ‎sticker omitted

import os
import sys

from classes import Usuario, Mensagem

def organizaUsuarios(Arq):

	i = 2
	nomeGrupo = ""
	usuarios = {}
	linha = Arq.readline().split()

	nomeGrupo = "Chambra"

	print("Estatísticas do grupo:", nomeGrupo)

	while linha != "":
		linha = Arq.readline()
		mensagem = Mensagem(linha)
		nome = mensagem.getNome()

		if mensagem.isValida():
			if nome not in usuarios:
				usuarios[nome] = Usuario(nome)

			usuarios[nome].adicionaMensagem(mensagem)
	
	return nomeGrupo, usuarios

def salvaDados(nomeGrupo, usuarios):

	path = "saidas/" + nomeGrupo + "/"
	
	if not os.path.exists(path):
		os.mkdir(path)

	for u in usuarios:
		Saida = open(path + u[0] + ".csv", "w")
		
		Saida.write("Nome;Número de Mensagens;Stickers;Imagens;Áudios\n")
		Saida.write("{};{};{};{};{}\n" .format(u[0], u[1].getDados('mensagem'), u[1].getDados('sticker'), u[1].getDados('image'), u[1].getDados('audio')))

		Saida.write("Palavra;Frequência\n")
		palavras = u[1].getPalavras()
		palavras = sorted(palavras.items(), key=lambda x: x[1], reverse=True)

		for p in palavras:
			Saida.write("{};{}\n" .format(p[0], p[1]))

		Saida.close()

###################################################################################################
#############################################          ############################################
############################################	MAIN	###########################################
#############################################          ############################################
###################################################################################################

if len(sys.argv) < 2:
	print("Erro: Arquivo do chat não informado")
	sys.exit()

try:
	Arq = open(sys.argv[1], "r")
except FileNotFoundError:
	print("O arquivo digitado não existe (você colocou o caminho correto e a extensão correta?)")
	sys.exit()

nomeGrupo, usuarios = organizaUsuarios(Arq)
usuarios = sorted(usuarios.items(), key=lambda x: x[0])
salvaDados(nomeGrupo, usuarios)