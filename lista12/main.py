import os

nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'Jose']


try:
    
    for i in range(len(nomes)):
        print(f"Código {i}: {nomes[i]}.")
    posicao = int(input("Informe o código do item a ser separado:"))
    nome_separado = nomes.pop(posicao) # separa o item da lista
    os.system("cls")
    print(nome_separado)      

except Exception as e:
    print(f"Nao foi possivel separa o itemn da lista. {e}.")