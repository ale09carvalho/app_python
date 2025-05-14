#declaraçao de funçao

#calcular triangulo

def calcular_triangulo(b, h):
    area = (b*h)/2
    return area

#algoritmo principal
try:
    b = float(input("Informe o valore da base:").replace(",","."))
    h = float(input("Informe o valore da altura:").replace(",","."))
    area = calcular_triangulo(b,h)

    print(f"O valor da área do triângulo é : {area}.")

except Exception as e:
    print(f"Nao foi possivel calcular a àrea do triângulo. {e}")
