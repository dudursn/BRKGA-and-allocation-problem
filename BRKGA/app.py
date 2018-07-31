from Dado import Dados
from sys import argv
import numpy as np
from BRKGA import BRKGA

#Tamanho da população
TAM_POP = 150
#Criterio de parada
MAX_GEN = 1000
#Taxa da população que estara na população elite
TX_ELITE = 0.10
#Taxa de cruzamento(Probabilidade de um filho herdar o gene do seu pai de elite)
TX_CROSS = 0.7
#Taxa de mutacao(Numero de mutantes criados)
TX_MUT = 0.20


'''
Para executar o programa, 'python nomedoarquivo.py nome_do_arquivo 0' para os que não são np e
'python nomedoarquivo.py nome_do_arquivo 1' para os que são np
'''
dados = Dados('../dados_atribuicao/'+argv[1], argv[2])
matriz = np.array(dados.matriz)

atribuicao = BRKGA(dados, TAM_POP,MAX_GEN, TX_CROSS, TX_MUT, TX_ELITE)
print('Solucão '+ str(atribuicao.solucao))


