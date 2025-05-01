#TODO - : Atividade
'''
Crie um programa em que o usuario informa varias notas de um aluno de 0 a 10 (quantas notas ele quiser inserir),
 e ao final, o programa calcule a média desse aluno e informa se ele esta aprovado, ou de recuperaçao ou reprovado
 Obs: Media para aprovaçao: 7 Media para recuperaçao: entre 5 e 7. abaixo de 5 : Reprovado.

'''

import os
#declaraço de variavel
notas = []

#tratamento de exceçao
try:
    while True:
        nota = float(input("Informe a nota do aluno: ").replace(",", ".")) # .replace(",", ".") permite substituir parte de uma sequência de caracteres por outras

        if notas >= 0 and nota <= 10: 
            notas.append(nota) #  append() aumenta o comprimento da lista addc ao final da lista
            print("Nota inserida com sucesso!")
            while True:                
                continuar = input("Deseja inserir outra nota? (s/n):")
                if continuar == "s" or continuar =="n":
                    os.system("cls")
                    break                  
                else:
                    print("Opçao invalida")
                    continue
                    match continuar:
                        case "s":
                            continue
                        case "n":
                            break
        else:
            print("Nota inválida, Favor inserir uma nota válida.")
            continue

    for i in range(len(notas)):
        print(f"Nota {i}: {notas[i]}")
        
    #media = sum(notas)/len(notas)
except Exception as e:    
    print(f"Nao foi possivel inserir dados na lista. (exceçao: {e})")
    
finally:
    media = sum(notas)/len(notas)
    print(f"\nMedia das notas:{media:,.2f}.")
    if media >= 7:
       print("O Aluno esta em APROVADO.")

    elif media >= 5:
       print("O Aluno esta de RECUPERAÇÃO.")

    else:
       print("O Aluno esta em REPROVADO.")
    


