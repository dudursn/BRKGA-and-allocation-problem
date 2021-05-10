O Problema Generalizado de Atribuição (PGA) é um problema clássico de Otimização Combinatória, que consiste em atribuir n tarefas a m agentes ao menor
custo possível, de modo que cada tarefa seja atribuída a apenas um único agente e
cada agente, por sua vez, não exceda sua capacidade máxima(Balachandran, 1976).

Para resolver esse problema foi implementado na liguagem de programação python os algoritmos genéticos com chaves aleatórias (BRKGA) ela capacidade de representar de forma robusta chaves aleatórias e um decodificador eficite para cada tipo de problema. 

Essa aplicação trabalha com o caso m==n, o numero de tarefas é igual ao número de máquinas (matriz quadrada)
        
EXECUTAR
    Para executar o programa:
    > python nome_do_arquivo.py nome_do_arquivo 0' 
    O '0' serve para informar que a base de dados 'nome_do_arquivo' possui o numero de tarefas igual ao número de máquinas (m x n, onde m=n)
    
    Exemplo:
    python app.py assign2.txt 0 
    python app.py assign3.txt 0

DADOS
    O formato desses arquivos de dados é:

    Número de itens a serem atribuídos (n)
    para cada item i (i = 1, ..., n):
    o custo de atribuir item i ao item j (c (i, j), j = 1, ..., n)
