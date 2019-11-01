class Usuario:

	def __init__(self, nome):
		self.nome = nome
		self.dados = {
			'mensagem' : 0,
			'sticker' : 0,
			'image' : 0,
			'audio' : 0
		}

		self.palavras = {}
	
	def adicionaMensagem(self, mensagem):
		tipo = mensagem.getTipo()

		if tipo == "sticker":
			self.dados['sticker'] += 1
		elif tipo == "image":
			self.dados['image'] += 1
		elif tipo == "audio":
			self.dados['audio'] += 1
		else:
			palavras = mensagem.getPalavras()

			# Devemos adicionar ao dicionário do usuário todas as palavras que ele disse
			for p in palavras:
				# Primeiro convertemos a palavra toda pra minúscula para diminuirmos a quantidade e palavras
				p = p.lower()

				if p in self.palavras:
					self.palavras[p] += 1
				else:
					self.palavras[p] = 1

			self.dados['mensagem'] += 1

	def getDados(self, param="mensagem"):
		return self.dados[param]

	def getPalavras(self):
		return self.palavras

class Mensagem:

	def __init__(self, linha):
		self.valida = False
		self.nome = "dummy"
		self.tipo = "dummy"
		self.palavras = []

		dados = linha.split()
		self.separaMensagem(dados)

	def limpaDados(self, dados):
		for i in range(0, len(dados)):
			dados[i] = dados[i].replace('\u200a', '').replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\u200e', '').replace('\u200f', '').replace('\u202a', '').replace('\u202b', '').replace('\u202c', '').replace('\u202d', '').replace('\u202e', '').replace('\u202f', '')

	def separaMensagem(self, dados):

		if dados:
			self.limpaDados(dados)
			self.valida = dados[0]

			if self.valida.startswith('['):
				self.valida = True
				self.nome = dados[2].replace(':', '')

				# Caso seja um telefone e não um contanto registrado
				if self.nome.replace("+", "").isdigit():
					self.nome = self.nome + " " + dados[3] + " " + dados[4].replace(":", "")
					self.tipo = dados[5]
					i = 5

				else:
					i = 2
					
					while not dados[i].endswith(":"):
						if dados[i+1] == "changed" or dados[i+1] == "added" or dados[i+1] == "removed" or dados[i+1] == "left" or dados[i+1] == "joined" or dados[i+1] == "created":
							break

						i += 1
						self.nome += " " + dados[i]

					self.tipo = dados[i+1]
					i += 2

				while i < len(dados):
					self.palavras.append(dados[i])
					i += 1

			else:
				self.valida = False

	def isValida(self):
		return self.valida
	
	def getNome(self):
		return self.nome

	def getTipo(self):
		return self.tipo

	def getPalavras(self):
		return self.palavras
