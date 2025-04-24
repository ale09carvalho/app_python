# TODO: tarefa desafio siginifica fazer uma tarefa

# tratamento de execeçao 
try:
    nome=input("informe seu nome: ")
    idade=int(input("Informe sua idade: "))

    #laço de repetição

    while True:

        print(f"{'-'*20}LISTA DE FILMES{'-'*20}\n") # MULTIPLINA 20 TRAÇOS E APOS MAIS 20 TRAÇOS
        print("Sala 1 - A Roda Quadrada -  Livre")
        print("Sala 2 - A Volta dos que não foram -  12 anos")
        print("Sala 3 - As Do Rei Careca -  14 anos")
        print("Sala 4 - Poeira em alto mar -  16 anos")
        print("Sala 5 - A Vingança do Peixe Frito - 18 anos")
    
        #recebe a sala desejada pelo usuario

        sala = input("*/nSala escolhida: ")

        #Verifica a sala escolhida 
        match sala:
            case "1":
                idade_minima = 0
            case "2":
                idade_minima = 12
            case "3":
                idade_minima = 14
            case "4":
                idade_minima = 16
            case "5":
                idade_minima = 18
            case _:
                idade_minima = idade+1 # obriga o usuario a escolher uma sala valida

        #verifica se o usuario tem idade minima para assistir o filme
        if idade >= idade_minima:
            print(f"Sala {sala} escolhida. Tenha um bom filme ")
            break # encerra o laço de repetição
        else:
            print(f"{nome}, você idade para assistir a esse filme")
            print("Por favor, escolha outro filme")
            continue # continua o laço de repetição

except Exception as e:
    print (f"Nao foi possivel executar a operaçao. {e}.")
finally:
    print("Programa encerrado.")
    '''
    Crie um algoritmo que receba o nome do usuario e sua idade e informe o nome de 5 filmes, e suas respectivas salas (sala 1 a sala 5),
    e tambem suas respectivas classificações indicativas. O usuario deera escolher o filme e o programa irá verificar se o usuario tem idade
     minima para assistir o filme. Caso tenha, o programa retornará para a tela de seleçao de filmes, permitindo que o usuario escolha outro filme.
   ctrl+ sf=hift + f = formata o codigo
   seleciona codigo aperta tab
   shift + tab = desce o codigo
   pep 8 = padroniza o codigo python
   ctrl + k + d = formata o codigo
 
     '''
