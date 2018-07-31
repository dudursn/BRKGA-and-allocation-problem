import numpy as np

class Decoder:
	def __init__(self, custos, tamanho):
		self.custos = custos
		self.tam = int(tamanho)

	def decode(self, cromossomos):

		'''
		Cromossomos é um vetor e redimensionado em uma matriz para a realização das 
		operações de restrição e função objetivo
		'''
		cromossomos = np.reshape(cromossomos,(self.tam,self.tam))

		#Variavel que representa se as tarefas i estão atribuidas a uma maquina j(1 ou 0)
		X_binarios = []
		for i in range(self.tam):
			#Variavel que representa se uma tarefa i esta atribuida a uma maquina j
			X = []
			for j in range(self.tam):
				if cromossomos[i,j]>0.5:
					X.append(1)
				else:
					X.append(0)
			X_binarios.append(X)
		
		X_binarios = np.array(X_binarios)		

		#Primeira restrição: soma das linhas tem que ser igual a 1
		for i in range(self.tam):
			soma_linha = 0
			for j in range(self.tam):
				soma_linha += X_binarios[i,j]	
			if soma_linha!=1:
				#Retorna um fitness alto para uma solução inválida, assim não vai ser a resposta da minimização
				return 99999
	
		#Segunda restrição: soma das colunas tem que ser igual a 1
		for j in range(self.tam):
			soma_coluna = 0
			for i in range(self.tam):
				soma_coluna += X_binarios[i,j]	
			if soma_coluna!=1:
				#Retorna um fitness alto para uma solução inválida, assim não vai ser a resposta da minimização
				return 99999

		
		#Função objetivo
		Z = 0
		for i in range(self.tam):
			for j in range(self.tam):
				Z += self.custos[i][j]* X_binarios[i][j]
		return Z