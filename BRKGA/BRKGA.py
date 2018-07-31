from Decoder import Decoder
import numpy as np
from math import sqrt
import time, timeit

class BRKGA:
	def __init__(self, dados,tam_pop, max_gen, tx_cross,tx_mut, tx_elite):
		#Tamanho da população
		self.TAM_POP = int(tam_pop)
		#Criterio de parada
		self.MAX_GEN = max_gen
		#Matriz de custos
		self.custos = np.array(dados.matriz)
		#Numero de genes em cada cromossomo
		self.TAM_CROM = int(dados.dim**2)
		#Taxa de cruzamento
		self.TX_CROSS = tx_cross
		#Taxa de mutação(Numero de mutantes criados)
		self.TX_MUT = tx_mut
		#Taxa da populacao que estara na populacao elite
		self.TX_ELITE = tx_elite
	
		#Utilizado p medir o tempo
		inicio = timeit.default_timer()
		self.solucao, fim = self.brkga_init(inicio)
		
		print ('duracao: %f' % (fim - inicio))
		

		

	#Gera a populacao
	def gera_populacao(self):
		populacao = []
		for i in range(self.TAM_POP):
			#Gera um individuo com chaves aleatórias [0,1]
			self.cromossomo = np.random.rand(self.TAM_CROM)
			#Esse individuo é adicionado a uma população
			populacao.append(self.cromossomo)
		return np.array(populacao)
		
	#Faz o cálculo da aptidão(Fitness)
	def aptidao(self, cromossomo):
		decodificacao = Decoder(self.custos, sqrt(self.TAM_CROM))
		'''
		Transforma as chaves aleatorias em binarios, verifica as restrições e 
		retorna o custo a ser minimizado
		'''
		Z = decodificacao.decode(cromossomo)
		return Z

    #Retorna a aptidão de cada individuo da população e adiciona em uma lista de aptidões
	def calcula_aptidao(self, populacao):
		return [self.aptidao(individuo) for individuo in populacao]

	def selecao_roleta(self, aptidoes):
		
		percentuais = np.array(aptidoes)/float(sum(aptidoes))
		vet = [percentuais[0]]
		for p in percentuais[1:]:
			vet.append(vet[-1]+p)
		r = np.random.random()
		for i in range(len(vet)):
			if r <= vet[i]:
				return i
        
    #parametrized uniform crossover    
	def cruzamento(self, pai,mae):
		filhos = []
		for i in range(2):
			filho = []
			for j in range(self.TAM_CROM):
				#Vicio probabilistico
				vp = np.random.rand()
				if vp <= self.TX_CROSS:
					filho.append(mae[j])
				else:
					filho.append(pai[j])
				filhos.append(filho)

		return filhos[0], filhos[1]

	def separacao_da_populacao(self, aptidoes, populacao):
		#Elementos vai se tornar uma tupla composta por(aptidoes, populacao)
		elementos = []
		for i in range(len(aptidoes)):
			elementos.append([aptidoes[i], list(populacao[i])])
		
		qtd = int(self.TX_ELITE*self.TAM_POP)

		#Ordena do menor para o maior pelas aptidoes
		elementos = sorted(elementos)
		
		pop_elite = []
		apt_elite = []
		pop_nao_elite = []
		apt_nao_elite = []
		i = 0
		for x in elementos:
			if i< qtd:
				apt_elite.append(x[0])
				pop_elite.append(x[1])
			else:
				apt_nao_elite.append(x[0])
				pop_nao_elite.append(x[1])

			i += 1

		#Retorna os melhores e os piores
		return pop_elite, apt_elite, pop_nao_elite, apt_nao_elite 
	
	#Para continuar compondo a nova geração, uma quantidade de mutantes é criada.
	def mutacao(self):
		qtd = int(self.TX_MUT*self.TAM_POP)
		mutantes = []
		for i in range(qtd):
			#Gera um individuo com chaves aleatórias [0,1]
			self.cromossomo = np.random.rand(self.TAM_CROM)
			#Esse individuo é adicionado a uma população
			mutantes.append(self.cromossomo)
		return mutantes
		

	def brkga_init(self, inicio):
		melhores = []
		print('Executando BRKGA...')
		#Cria a população
		populacao = self.gera_populacao()
		#Inicia com o cálculo das aptidões da população 
		aptidoes = self.calcula_aptidao(populacao) 
		#Melhores
		melhores.append(np.min(aptidoes))
		#Imprime o melhor de cada geração
		print('0 - melhor:',np.min(aptidoes))

		#Criterio de parada: gerações
		for geracao in range(self.MAX_GEN):
			
			'''
			Aqui o grande diferencial do BRKGA com o RKGA, ordena por aptidões e separa em
			elite e não elite a população
			'''
			populacao_elite,aptidao_elite, populacao_nao_elite , aptidao_nao_elite = self.separacao_da_populacao(aptidoes, populacao)

			#A população elite ja está garantida para proxima geração
			nova_populacao = [individuo for individuo in populacao_elite]

			#Geração de individuos que sofreram mutação são adicionados a nova população
			mutantes = self.mutacao()
			for individuo in mutantes:
				nova_populacao.append(individuo)

			#Agora faz o cruzamento e gerar os individuos restantes para compor a nova população
			for c in range(int((self.TAM_POP-len(nova_populacao))/2)):
				'''
				print(len(populacao))
				print(len(aptidoes))
				'''
				#Seleção depois do elitismo do BRKGA em separar a população
				pai = populacao_nao_elite[self.selecao_roleta(aptidao_nao_elite)]
				mae = populacao_elite[self.selecao_roleta(aptidao_elite)]

				#Cruzamento
				filho,filha = self.cruzamento(pai,mae)

				#Nova população sendo criada
				nova_populacao.append(filho)
				nova_populacao.append(filha)

			
			
			#A população atual passa a ser a nova geração
			populacao = nova_populacao

			#Calcula as aptidões da nova geração
			aptidoes = self.calcula_aptidao(populacao)

			#Utilizado para medir o tempo
			fim = timeit.default_timer()
			#Imprime o melhor de cada geração
			print(geracao+1,'- melhor:',melhores[0],' - tempo: ', fim)
			
			#Melhores
			melhores.insert(0, np.min(aptidoes))	

		fim = timeit.default_timer()
		return np.min(melhores), fim 