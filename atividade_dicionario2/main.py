#TODO atividade2
...
'''
Crie um CRUD, ou seja um programa que:
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

pessoas = []

try:
    print("\n====== MENU PRINCIPAL ======")
    opcao = input (" Digite: [1] - CADASTRAR - [2] ALTERAR - [3] EXCLUIR - [4] LISTAR - [5] SAIR:")

    match opcao:
            case 1:
                #CADASTRAR
                pessoa = {}
                pessoa['nome'] = input("Informe o nome:")  
                pessoa['cpf'] = input("Informe o cpf:")
                pessoa['email'] = input("Informe o e-mail:")
                pessoa['telefone'] = input("Informe o telefone:")
                pessoa['dataNascimento'] = input("Informe a data de nascimento (dd/mm/aa):")
                pessoa['genero'] = input("Informe o genero:")

                #adciona a pessoa na lista
                pessoas.append(pessoa)

                os.system("cls")
                print(f"{pessoa.get('nome')} cadastrado com sucesso!")
                cadastrar = input("Deseja cadastrar nova pessoa? (s/n):")

            case 2:
              # ALTERAR


            case 3:
              # EXCLUIR
            


            case 4:
                # LISTAR

                print(f"Nome: {pessoas.get('nome')}")
                print(f"CPF: {pessoas.get('cpf')}")
                print(f"Email: {pessoas.get('email')}")
                print(f"Telefone: {pessoas.get('telefone')}")
                print(f"Data de Nascimento: {pessoas.get('dataNascimento')}")
                print(f"Genero: {pessoas.get('genero')}")
            
            case 5:
                break
           
            case _:
                print("Opçao invalida.")
                continue
        
except Exception as e:
    print(f"Nao foi possível cadastrar pessoa. {e}.")