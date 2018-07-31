
class Dados:
	def __init__(self, arquivo, tipo):
		tupla = self.ler_dados(arquivo, tipo)
		self.dim = tupla[0]
		self.matriz = tupla[1]
		
	def ler_dados(self, arquivo,tipo):
		try:
			matriz = []
			f = open(arquivo, 'r')
			data = f.read()
			data = data.split()
			#Primeiro valor e a dimensao
			dimensao = int(data[0])
			if tipo =='0':
				k = 1
				for i in range(dimensao):
					linha = []

					for j in range(dimensao):
						linha.append(int(data[k]))
						k+=1
		
					matriz.append(linha)


			elif tipo == '1':
				k = pos_atual = 1
				valor = int(data[k])
				for i in range(dimensao):
					linha = []
					#Corresponde ao dado do texto que especifica a linha da matriz que nao pode ser armazenado nela
					invalido = 0
					for j in range(dimensao):
						
						if pos_atual == i+1: 
							
							if k%3 != 1:
								linha.append(valor)	
							else:
								pos_atual = valor
								invalido+=1
							k +=1
							
							if k<len(data):
								valor = int(data[k])
								
						else:
							invalido+=1
					
					#Para todos os invalidos coloca-se zero na matriz
					for l in range(invalido):
						linha.append(0)	

					matriz.append(linha)
				print(matriz)
				input()
			else:
				print('Para executar o programa, \'python nome_do_arquivo.py nome_do_arquivo 0\' para os que nao sao np e\'python nomedoarquivo.py nome_do_arquivo 1\' para os que sao np')
				exit()

			return(dimensao, matriz)

		except IOError:
			print('Erro ao abrir arquivo ', arquivo)

		
		