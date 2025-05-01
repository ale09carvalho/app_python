<<<<<<< HEAD
#importar biblioteca
import os


#declaçao de varianvel 
cidades = [
    "Brasilia", "Rio De Janeiro", "Sao Paulo",
    "Goiania", "Belo Horizonte", "Palmas", 
    "Brasilia", "Goiania", "Brasilia"
]

#PESQUISAR 
#tratamento de excecao
try:
    #Loop infinito
    while True:
        os.system("cls") #limpa terminal
        #usuario informa valor a ser pesquisado
        pesquisa = input("Informe a Cidade a ser pesquisada:").title() # title faz qdo o usuario digitar inicial minuscula enteda o entenda Maiuscula da lista


        #retorna a qauntidad de valores econtrado
        result =cidades.count(pesquisa)

        #mostra o resultado na tela
        if result != 0:
            print(f"{pesquisa} foi encontrado na lista {result} vezes.")
        else:
            print(f"{pesquisa} nao foi encontradao na lista.")

        #pergunta  se o usuario dese realizar uma nova pesquisa
        continuar = input("Deseja continuar? (s/n):")

        #verifica se o usuario deseja continuar
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _: #default
                print("Opçao Invalida.")
                break
except Exception as e:
    print(f"Nao foi possivel ralizar a busca {e}")

=======
#importar biblioteca
import os


#declaçao de varianvel 
cidades = [
    "Brasilia", "Rio De Janeiro", "Sao Paulo",
    "Goiania", "Belo Horizonte", "Palmas", 
    "Brasilia", "Goiania", "Brasilia"
]

#PESQUISAR 
#tratamento de excecao
try:
    #Loop infinito
    while True:
        os.system("cls") #limpa terminal
        #usuario informa valor a ser pesquisado
        pesquisa = input("Informe a Cidade a ser pesquisada:").title() # title faz qdo o usuario digitar inicial minuscula enteda o entenda Maiuscula da lista


        #retorna a qauntidad de valores econtrado
        result =cidades.count(pesquisa)

        #mostra o resultado na tela
        if result != 0:
            print(f"{pesquisa} foi encontrado na lista {result} vezes.")
        else:
            print(f"{pesquisa} nao foi encontradao na lista.")

        #pergunta  se o usuario dese realizar uma nova pesquisa
        continuar = input("Deseja continuar? (s/n):")

        #verifica se o usuario deseja continuar
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _: #default
                print("Opçao Invalida.")
                break
except Exception as e:
    print(f"Nao foi possivel ralizar a busca {e}")

>>>>>>> bbfefade35749fabdc42a6f2bc6e6443136ebf2b
