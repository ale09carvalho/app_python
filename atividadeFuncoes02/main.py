# TODO - ATIVIDADADE
'''
Crie um programa em python que calcule um número informado pelo usuarioda sequência Fibonacci
'''
# NOTE - Utilizar funçao recursiva
import os

def fibonacci_recursivo(n):
    return n if n <= 1 else fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


if __name__ == "__main__":
    os.system("cls")
    try:
        n = int(input("Digite um número inteiro não negativo para calcular o Fibonacci: "))
        print(fibonacci_recursivo(n))

    except Exception as e:
        print (f"Não foi possivel realizar a operaçao. {e}.")