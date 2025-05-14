'''
13/05/2025
Funções pequenos blocos de programação que podem ser chamados no algoritmo principal.
Isso possibilita que seu código seja dividido em partes menores.
'''
#Funçao com parametro e sem retorno
#declaraçao de funçao


def dar_boas_vindas(nome):
    print(f"{'='*10}CURSO DE APERFEIÇOAMENTO EM PYTHON {'='*20}\n")
    print("Seja bem vindo {nome}!!!")


# Algoritmo principal
nome = input("Informe seu nome: ")
dar_boas_vindas(nome)
