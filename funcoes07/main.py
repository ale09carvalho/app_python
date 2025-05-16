#funçoes recursivas - Uma função recursiva é nada mais do que uma função que chama a si mesma quando executada.
#declaraçao de funçao recursiva

def calcular_fatorial(n):
    return 1 if n == 0 else n * calcular_fatorial(n-1)

if __name__ == "__main__":
    try:
        n = int(input("Informe um número inteiro positivo: "))
        result = calcular_fatorial(n)
        print(f"O fatorial de {n} é {result}.")

    except Exception as e:
        print (f"Não foi possivel calcular fatorial. {e}.")

