#TODO: atividade
'''
Crie um programa que receba do usuario uma lista de compras e ordene a lista em oredem alfabética.
Obs1: so quero os nomes dos intens, deixe os preços e a quantidade de fora.
Obs2: apos terminar, faça um commit no repositorio remoto.
'''

#declaraçao  da lista
compras = []

#tratamento de exceçao
try:
    #loop infinito
    while True:
        #Usuario informa o nome
        item = input("Informe um item ou deixe em branco para exibir a lista: ")

        #verifia se o nome foi inserido
        if item != "":
            #adiciona o nome na lista
            compras.append(item)
            continue
        else:
            break

     #exibe a lista de nomes ordem alfabética
    compras.sort()
except Exception as e:
    print(f"Nao foi possivel inserir dados na lista. (exceçao: {e})")
finally:
    for item in compras:
        print(item)

