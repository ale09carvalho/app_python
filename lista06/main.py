#declaraçao  da lista
nomes = []

#tratamento de exceçao
try:
    #loop infinito
    while True:
        #Usuario informa o nome
        item = input("Informe um nome ou deixe em branco para exibir a lista: ")

        #verifia se o nome foi inserido
        if item != "":
            #adiciona o nome na lista
            nomes.append(item)
            continue
        else:
            break

     #exibe a lista de nomes ordem alfabética
    nomes.sort() ## ordena a lista em ordem alfabética

except Exception as e:
    print(f"Nao foi possivel inserir dados na lista. (exceçao: {e})")
finally:
    for item in nomes:
        print(item)