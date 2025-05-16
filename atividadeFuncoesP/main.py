import os
import math


def calcular_1_grau(a,b):
    # TODO - a*x+b=2
    X = -b/a
    return X

def calcular_2_grau(a,b,c):
    # TODO - ax² + bx + c = 0
    if a is not 0: #if a is not --> operador booleano de negativo ou !==0
        delta = (b**2) - 4*a*c
        if delta > 0:
             x1 = (-b + math.sqrt(delta))/(2*a)
             x2 = (-b - math.sqrt(delta))/(2*a)
             yield f"x' = {x1}"
             yield f'x" = {x2}'

        elif delta == 0:
            x = -b / 2*a
            yield f"x = {x}"
        else:
            yield " A equaçao nao possoe valores reais."
    else:
        yield "O valor de 'a' e zero portanto não é uma equaçao do 2º grau."

if __name__ == "__main__":
    try:
        while True:
            print(" 1 - Calcular Equaçao do 1º Grua:")
            print(" 2 - Calcular Equaçao do 2º Grua:") 
            print(" 3 - SAIR DO PROGRAMA:")         
            opcao = input("Informe a opção desejada:")

            match opcao:
                case "1":
                    os.system("cls")

                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    result = calcular_1_grau(a,b)

                    print(f"O valor de x em {a} x + {b} = 0 é : {result}.")
                    continue
                case"2":
                    os.system("cls")
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    c = float(input("Informe o valor de 'c': ").replace(",","."))
                    result = calcular_2_grau(a,b,c)
                    for x in result:
                        print (x)
                    
                    continue
                case"3":
                    print("Programa encerrado com sucesso!!")
                    break
                case _:
                    print("Opção invalida.")
                    continue

    except Exception as e:
        print(f"Nao foi possivel executar a operaçao. {e}")

        
