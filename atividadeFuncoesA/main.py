# TODO - Atividade
'''
Crie um programa onde o usuario poderá escolher se deseja calcular a equaçao do 1º grau ou a equaçao do 2º grau e o programa retornar o resultado da equaçao
'''
# NOTE - O programa deverá ser executado em loop
import equacao as eq

if __name__=="__main__":
    try:
        print(" Escolha a figura do qual deseja calcular :")
        print("1 -Equaçao do 1º Grau")
        print("2 -Equaçao do 2º Grau")
        opcao = input("Informe a opçaõ desejada:")
    
        match opcao:
            case "1":
                a = float(input("Informe o valor da a: ").replace(",","."))
                b = float(input("Informe o valor da b: ").replace(",","."))
                result = eq.equacao_1_grau(a,b) # Chame a função  com os valores
                print(f"o valor de x e: {result}")

            case "2":
                a = float(input("Informe o valor da a: ").replace(",","."))
                b = float(input("Informe o valor da b: ").replace(",","."))
                c = float(input("Informe o valor da c: ").replace(",","."))
                result = eq.equacao_2_grau(a,b,c) # Chame a função  com os valores

                for resultados_posiveis in result:
                    print(f"o valor de x e: {resultados_posiveis}")
            case _:
                print("Opção inválida.")
    
    except Exception as e:
        print(f"Nao foi possivel executar a operaçao. {e}")

