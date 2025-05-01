<<<<<<< HEAD
#importa biblioteca
import os

#declaraçao de lista
nomes = ["Fulano", "Cicrano", "Beltrano", "Joao", "Maria", "Jose"]
         
#Tratamento de exceçao
try:
    # Loop infinito
    while True:
        #limpa o terminal
        # REVIEW (revisar) os.system("cls")
        
        #exibir a lista
        for i in range(len(nomes)):# retorna o número de elementos na lista nomes, e range() gera uma sequência de números de 0
            print(f"Nome do codigo {i}: {nomes[i]}")
        opcao = input("Deseja excluir item da lista? (s/n): ")

        match opcao:
            case "s":
                posicao = int(input("Informe o codigo do nome a ser alterado:"))
                del(nomes[posicao])
                os.system("cls")
                print ( "Item excluido com sucesso \n")
                continue
                
            case "n":
                break
                
            case _:
                print("Opçao Invalida! ")
                continue

except Exception as e:
=======
#importa biblioteca
import os

#declaraçao de lista
nomes = ["Fulano", "Cicrano", "Beltrano", "Joao", "Maria", "Jose"]
         
#Tratamento de exceçao
try:
    # Loop infinito
    while True:
        #limpa o terminal
        # REVIEW (revisar) os.system("cls")
        
        #exibir a lista
        for i in range(len(nomes)):# retorna o número de elementos na lista nomes, e range() gera uma sequência de números de 0
            print(f"Nome do codigo {i}: {nomes[i]}")
        opcao = input("Deseja excluir item da lista? (s/n): ")

        match opcao:
            case "s":
                posicao = int(input("Informe o codigo do nome a ser alterado:"))
                del(nomes[posicao])
                os.system("cls")
                print ( "Item excluido com sucesso \n")
                continue
                
            case "n":
                break
                
            case _:
                print("Opçao Invalida! ")
                continue

except Exception as e:
>>>>>>> bbfefade35749fabdc42a6f2bc6e6443136ebf2b
    print(f"Nao foi possível deletar item da lista. {e}.")