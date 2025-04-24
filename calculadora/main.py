#declaraçao de variaveis
x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))

#Mostrar menu de opçoes
print("Escolha uma operação desejada:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. - Resto da Divisão")

#Usuario escolhe a operação
operador = input("Informe o número da operação desejada: ")

# Estrutura match = escolha de operação)
match operador:
    case "1":
        print(f"Resultado da soma: {x+y}.")#soma
    case "2":
        print(f"Resultado da subtração: {x-y}.") #subtração
    case "3":
        print(f"Resultado da multiplicação: {x*y}.") #multiplicação
    case "4":
        print(f"Resultado da divisão: {x/y}.") #divisão
    case "5":
        print(f"Resultado do resto da divisão: {x%y}.") #resto da divisão
    case _: # :_ default 
        print(" Operação inválida. Tente novamente.")
 

