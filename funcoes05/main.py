#Os arquivos em Python são chamados de módulos e são identificados pela extensão .py. Um módulo pode definir funções, classes e variáveis.
#importar módulo
#pode usar assim  ---> import funcoes OU  apelidar  ---> import funcoes as f  ou ainda --> from funcoes import calcular_quadrilatero OU 'from funcoes import *'

#from funcoes import calcular_quadrilatero, calcular_triangulo, calcular_trapezio

import funcoes

#o que tiver dentro do if nao sera importado
#o script atual está sendo executado diretamente como o programa principal ou se está sendo importado como um módulo 
if __name__=="__main__":
    try:
        print(" Escolha a figura do qual deseja calcular a área:")
        print("1 - Quadrilatero")
        print("2 - Triângulo")
        print("3 - Trapezio")
        opcao = input("Opçaõ desejada:")

        if opcao == "1" or opcao == "2":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
                    
            match opcao:
                case "1":
                    #resultado = calcular_quadrilatero(b,h)
                    resultado = funcoes.calcular_quadrilatero(b,h)
                    print (f"A area do quadilatero é {resultado}.")

                case "2":
                    #resultado = calcular_triangulo(b,h)
                    resultado = funcoes.calcular_triangulo(b,h)
                    print (f"A area do triângulo: {resultado}.")

        elif opcao == "3":
            b = float(input("Informe o valor da base menor: ").replace(",","."))
            B = float(input("Informe o valor da Base maior: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            #resultado = calcular_trapezio(b,B,h)
            resultado = funcoes.calcular_trapezio(b,B,h)

            print (f"A area do trapezio: {resultado}.")
        else:
            print("Opaçao invalida Programa Encerrado")

    except Exception as e:
        print(f"Nao foi possivel executar a operaçao. {e}")

