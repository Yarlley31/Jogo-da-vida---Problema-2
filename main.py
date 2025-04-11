"""
Autor: Yarlley Fernandes dos Santos
Componente Curricular: EXA855 - MI Algoritmos
Concluido em: 
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
# SO: Windows 11 Versão 24H2

# importa o módulo criar_matriz
from criar_matriz import criar_matriz_10x10
from exibir_matriz import mostra_matriz_atualizada, mostra_matriz_inicial

from time import sleep
from random import randint

# Cria a matriz 10x10 preenchida com ' '
matriz10x10 = criar_matriz_10x10()


# Exibe a matriz inicial
mostra_matriz_inicial(matriz10x10)


# Lista para armazenar os índices selecionados
indeces_selecionados = []


# Loop para preencher a matriz com 'V' onde o usuário escolher
sair = False 
while not sair:
    # Solicita ao usuário para escolher uma linha e uma coluna
    linha = randint(0, 9) # Depois atualizar para o usuário escolher
    # linha = int(input("Escolha uma linha (0-9): "))
    coluna = randint(0, 9)
    # coluna = int(input("Escolha uma coluna (0-9): "))
    
    
    # Verifica se a posição já foi preenchida
    if (linha, coluna) in indeces_selecionados:
        print("Essa posição já foi preenchida. Tente novamente.")
        continue

    # Preenche a matriz com 'V' na posição escolhida
    matriz10x10[linha][coluna] = 'V'
    indeces_selecionados.append((linha, coluna))

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar preenchendo a matriz? (s/n): ").strip().lower()
    if continuar != 's':
        sair = True
        
        
# Exibe a matriz atualizada
mostra_matriz_atualizada(matriz10x10)

# falta criar a lógica do jogo