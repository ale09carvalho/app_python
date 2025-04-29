##importar biblioteca
import os

#declaraçao da lista

cidades = ["Brasília", "Sao Paulo", "Rio De Janeiro", "Curitiba", "Recife", "Fortaleza"]

#tratamento de excecao
try:
    #loop infinito
    while True:
        #exibe a lista
        for i in range(len(cidades)):
            print(f"Cidade de codigo {i}: {cidades[i]}. ")
        
        #print("\n") #quebra de linhan
        #usuario informa se deseja alter algunm valor
        alterar = input("\nDeseja alterar algum valor? (s/n)")
        match alterar:
            case "s":
                codigo_cidade = int(input("\nInforme o codigo da cide de deseja mudar: ")) #usuario informa a posiçao do valor que deseja alterar
                nova_cidade = input("Informe um novo nome para a cidade: ") #usuario informa o novo valor
                cidades[codigo_cidade] = nova_cidade #troca o valor
                os.system("cls")
                continue
            case "n":
                break
            case _:
                print("Opçao inválida")
                break
except Exception as e:
    print(f"Nao foi possível alterar o valor na lista. {e}")

