# Áudios é em segundos
usuarios = {
	'lucas' : {
		'mensagens' : 7,
		'stickers' : 2,
		'midias' : 2,
		'audios' : 1,
	},
	
	'cosi' : {
		'mensagens' : 23,
		'stickers' : 14,
		'midias' : 3,
		'audios' : 1
	},

	'pablo' : {
		'mensagens' : 21,
		'stickers' : 5,
		'midias' : 2,
		'audios' : 7
	}
}

#[02/05/19 15:00:56] Pablo: nao sou obrigado a viver num mundo onde o mormaço é rei e acha q ta certo
def organiza(Arq):

	usuarios = {}
	string = Arq.readline()

	# dados[0] = [02/05/19 
	# dados[1] = 15:00:56]
	# dados[2] = Pablo
	# dados[3...] = mensagem

	while string != "":
		dados = string.split()
		
		if dados:
			msgValida = dados[0].replace('\u200e', '')
			
			if msgValida.startswith('['):
				nome = dados[2].replace(':', '')
				nome = nome.replace('\u200e', '')
				tipoMsg = dados[3].replace('\u200e', '')
				print(tipoMsg, end=" - ")
				
				if nome in usuarios:
					print(tipoMsg)
					
					if tipoMsg == "‎sticker":
						usuarios[nome]['sticker'] = usuarios[nome]['sticker'] + 1
					elif tipoMsg == "image":
						usuarios[nome]['image'] = usuarios[nome]['image'] + 1
					elif tipoMsg == "audio":
						usuarios[nome]['audio'] = usuarios[nome]['audio'] + 1
					else:
						usuarios[nome]['mensagem'] = usuarios[nome]['mensagem'] + 1
							
				else:
					# tem que ver o tipo de mensagem aqui também
					
					usuarios[nome] = {
						'mensagem' : 0,
						'sticker' : 0,
						'image' : 0,
						'audio' : 0,
					}	
			
		string = Arq.readline()
	
	for u in usuarios:
		print(u, usuarios[u])
	
# x = {'a' : 0, 'b': 2, 'c' : 1}
# sorted(dic.items(), key=lambda dic: dic[1]['mensagens'])


# MAIN
opcao = input("Selecione o arquivo para estatísticas: ")

try:
	Arq = open(opcao, "r")
	organiza(Arq)

except FileNotFoundError:
	print("O arquivo digitado não existe")
