"""
Autor: Yarlley Fernandes dos Santos
Componente Curricular: EXA855 - MI Algoritmos
Concluido em:  17/04/2025
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

import os
from time import sleep
from random import randint

# Cria a matriz 10x10 preenchida com ' '
matriz10x10 = criar_matriz_10x10()


# Exibe a matriz inicial
mostra_matriz_inicial(matriz10x10)


# Lista para armazenar os índices selecionados
indeces_selecionados = []


# Loop para preencher a matriz com 'V' onde o usuário escolher
qnt_cel_viva = int(input("Digite quantas células vivas quer no tabuleiro inicial: "))

for i in range(qnt_cel_viva):
    
    # Solicita ao usuário para escolher uma linha e uma coluna
    
    # verifica se o usuário digitou um número entre 0 e 9 para a linha
    while True:
        try:
            linha = int(input(f"Escolha a linha (0-9) para a célula {i+1}: "))
            if 0 <= linha < 10:
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 9.")
            
    # verifica se o usuário digitou um número entre 0 e 9 para a coluna
    while True:
        try:
            coluna = int(input(f"Escolha a coluna (0-9) para a célula {i+1}: "))
            if 0 <= coluna < 10:
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 9.")


    # Verifica se a posição já foi preenchida
    if (linha, coluna) in indeces_selecionados:
        print("Essa posição já foi preenchida. Tente novamente.")
        continue

    # Preenche a matriz com 'V' na posição escolhida
    matriz10x10[linha][coluna] = 'V'
    indeces_selecionados.append((linha, coluna))

        
# Exibe a matriz atualizada
mostra_matriz_atualizada(matriz10x10)

# lógica do jogo
# se uma célula viva tem menos de 2 vizinhos vivos ela morre
# se uma célula viva tem 2 ou 3 vizinhos vivos ela sobrevive
# se uma célula viva tem mais de 3 vizinhos vivos ela morre
# se uma célula morta tem exatamente 3 vizinhos vivos ela se torna viva


# Loop para atualizar a matriz
while True:
    # Cria uma nova matriz para armazenar o próximo estado
    nova_matriz = criar_matriz_10x10()
    
    # Atualiza a matriz com base nas regras do jogo
    for i in range(10):
        for j in range(10):
            # Conta os vizinhos vivos
            vizinhos_vivos = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x >= 0 and x < 10) and (y >= 0 and y < 10) and (x != i or y != j):
                        if matriz10x10[x][y] == 'V':
                            vizinhos_vivos += 1

            # Aplica as regras do jogo
            if matriz10x10[i][j] == 'V':
                if vizinhos_vivos < 2 or vizinhos_vivos > 3:
                    nova_matriz[i][j] = '.'
                else:
                    nova_matriz[i][j] = 'V'
            else:
                if vizinhos_vivos == 3:
                    nova_matriz[i][j] = 'V'
                else:
                    nova_matriz[i][j] = '.'

    # Atualiza a matriz original com o novo estado
    matriz10x10 = nova_matriz.copy()
    
    # Exibe a matriz atualizada
    mostra_matriz_atualizada(matriz10x10)
    
    # Pausa para visualizar a atualização
    sleep(.7)
    
    # Limpar o terminal (Windows)
    if os.name == 'nt':
        clear = os.system('cls')
    # Limpar o terminal (Linux/Mac) 
    if os.name == 'posix':
        clear = os.system('clear')


# se todas celulas estiverem mortas, o jogo termina
    if all(matriz10x10[i][j] == '.' for i in range(10) for j in range(10)):
        print("Todas as células estão mortas. O jogo terminou.")        
        break
