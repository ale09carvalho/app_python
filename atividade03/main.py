# TOFO
'''
CRIES UM PROGRAMA ONDE O USUARIO  ESCOLHE UMA DESSAS OPÇOES:
0 -  SAIR DO PROGRAMA
1 - CRIAR UMA NOVA CONTA
2 - ALTERAR DADOS DO TITULAR DA CONTA
[**3 - EXCLUIR CONTA <------- vai ser retirado]
3 - FAZER SAQUE
4 - FAZER DEPOSITO
5 - CONSULTAR DADOS DA CONTA

DADOS DO TITULAR DA CONTA:
- NOME
- CPF
- AGENCIA (1010)
- NUMERO DA CONTA (NUMERO ALEATORIO)
- SALDO (SEMPRE VAI COMEÇAR COM ZERO)
'''
# NOTE - CONSULTAR DADOS DA CONTA ENVOLVE DADOS DA CONTA
# NOTE - PARA NUMERO DA CONTA, USE A BIBLIOTECA RADOM

#importando a biblioteca
import os
import random as r
import modulo as m


if __name__== "__main__":
    titulares = []
    try:
        while True:
            titular = {} #dicionario

            #ANCHOR - menu
            print(f"{'='*30} BANCO COBRA  {'='*30}")
            print("0 - Sair do Programa:")
            print("1 - Criar nova conta:")
            print("2 - Alterar dados do titular da conta:")
            #print("3 - Excluir Conta:") #retirada essa opçao
            print("3 - Fazer saque:")
            print("4 - Fazer deposito:")
            print("5 - Consultar dados da conta:")

            opcao = input("Informe a Opçao desejada: ")

            os.system("cls")
            match opcao:
                case "0":#Sair do programa
                    print("\n Programa encerrado com sucesso!\n")
                    print("\n Tenha um otimo dia!!!\n")
                    break

                case "1": #Criar conta
                    titular['agencia'] = 1010
                    titular ['num_conta'] = r.randint(10000, 99999) # gerar números aleatórios, que é randint() 
                    titular ['saldo'] = 0.00
                    titular['nome'] = input("Informe o Nome do titular:")
                    titular['cpf'] = input("Informe o CPF do titular:")

                    os.system("cls")

                    print(f"{titular.get('num_conta')} criada com sucesso! \n")

                case "2": # Alterar dados
                    print(f"Nome: {titular.get('nome')}")
                    print(f"CPF: {titular.get('cpf')}\n")

                    campo = input("Informe o campo que deseja alterar: ").strip().lower()
                    
                    match campo:
                        case "nome":
                            titular ['nome'] = input("Informe o novo nome do titular: ")
                            os.system("cls")
                            print("Nome do titular atualizado com sucesso.")

                        case "cpf":
                             titular ['cpf'] = input("Informe o novo CPF do titular: ")
                             os.system("cls")
                             print("CPF titular atualizado com sucesso.")
                             
                        case _:
                            print ("Opçao invalida!")
                      
                case "3":
                     valor = float(input("Informe o valor do saque: R$").replace(",", "."))
                     saldo = titular.get('saldo')

                     if valor <= saldo:
                         titular['saldo'] = m.fazer_saque(saldo, valor)

                         os.system("cls")
                         print("Saque efetuado com sucesso!")
                         print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")
                     else:
                        print("Nao foi possivel efeturar o saque. Valor indisponível.")
                     continue

                case "4":
                      valor = float(input("Informe o valor do deposito em reais: R$").replace(",", "."))
                      titular['saldo'] = m.fazer_deposito(titular.get('saldo'),valor)

                      os.system("cls")
                      print(f"Deposito efetuado com sucesso.")
                      print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")
                      
                      continue
                case "5":
                      m.consultar_dados(titular)
                      continue
                
                case _:
                    print("Opçao Invalida.")
                    continue
                    
    except Exception as e:
        print(f"Nao foi possivel executar a operaço. {e}.")