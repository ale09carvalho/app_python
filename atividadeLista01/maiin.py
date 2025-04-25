#TODO: atividade
'''
Crie um programa que receba do usuario uma lista de compras e ordene a lista em oredem alfabética.
Obs1: so quero os nomes dos intens, deixe os preços e a quantidade de fora.
Obs2: apos terminar, faça um commit no repositorio remoto.

'''
#importando a biblioteca
import os

#declaraçao  da lista
lista = []
try:
    #loop infinito
    while True:
        item = input("Informe o nome do item ou deixe em branco para encerrar: ")  #input
        os.system("cls") #limpa o terminal

        #verifica se o item esta vazio ou não
        if item !="":
            lista.append(item) #inseri o item da lista
            print(f"{item} inserido na lista com sucesso!") #mensagem de confirmaçao
            continue
        else:
            break
    #ordena a lista 
    lista.sort()
except Exception as e:
    print(f"Nao foi possivel inserir dados na lista. (exceçao: {e})")

finally:
    #exibir a lista
    for item in lista:
        print(item)

