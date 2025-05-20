#TODO atividade2
'''
Crie um programa em pyton utilizando lista ou dicionario, ou seja um programa que:
- Cadastre
- Liste
- Altere
- Exclua
O programa deverá cadastrar possoas com os seguintes dados:
Nome, CPF, E-mail,  Telefone, Data de Nascimento, Gênero.
'''
# NOTE: o usuário poderá cadastrar quantas pessoas quiser.
# NOTE: O Programa dverá fornecer um menu de opções: cadastrar, listar, alterar, excluir e sair do programa



#importando a biblioteca
import os

lista = []

try:
    while True:
        # NOTE - adcionar a inha abaixo
        usuario = {} #dicionario

        print(f"{'='*15} CRUD COBRA {'='*15}")
        print("Informe a opao desejada:")
        print("0 - Sair:")
        print("1 - Cadastrar usuario:")
        print("2 - Listar Usuarios:")
        print("3 - Alterar dados:")
        print("4 - Excluir  usuario:")

        opcao = input("Informe a Opçao desejada: ")

        match opcao:
            case "0":
                print("\nPrograma encerrado!\n")
                break
         
            case "1":
                # FIXME eliminar essa linha usuario = {}
                
                usuario['nome'] = input("Informe o nome:")  
                usuario['cpf'] = input("Informe o cpf:")
                usuario['email'] = input("Informe o e-mail:")
                usuario['telefone'] = input("Informe o telefone:")
                usuario['dataNascimento'] = input("Informe a data de nascimento (dd/mm/aa):")
                usuario['genero'] = input("Informe o genero:")

                lista.append(usuario)
                os.system("cls")
                print(f"{usuario.get('nome')} cadastrado com sucesso!\n")
                continue

            case "2":
                os.system("cls")
                for i in range(len(lista)):
                    print(f"Posiçao: {i}")

                    # NOTE - alterar a linha abaixo chamar a lista
                    for chave in lista[i]:
                        print(f"{chave.title()}: {lista[i].get(chave)}")
                    print("\n")
                    continue

            case "3":
                os.system("cls")
                posicao = int(input("Informe a posição do usuario que deseja alterar: "))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                        print("\n")
                        dado = input("Informe o nome da chave que deseja alterar: ")
                        if lista[posicao][dado]:
                            lista[posicao][dado] = input(f"Inofrme o novo valor de {dado}: ")
                            os.system("cls")
                            print("Dados alterado com sucesso!\n")
                        else:
                            print("Chave invalida!")
                    else:
                        print("Posiçao invalida!")
                        continue
            case "4":
                os.system("cls")
                posicao = int(input("Informe a posição do usuario que deseja deletar: "))
                if lista[posicao]:
                    del(lista[posicao])
                    print("Usuario deletado com sucesso!")
                else:
                     print("Não foi possivel deletar o usuario!")
                continue
            case _:
                print("Opçao invalida!")
                continue

except Exception as e:
    print(f"Nao foi possivel executar a operaço. {e}.")
