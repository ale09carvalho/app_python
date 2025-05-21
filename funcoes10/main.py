#Função map() --- Aplica uma função dentro de uma lista Exemplo Lista numerica - retorna nova sequência com os resultados

calcular_pg = lambda x: x * 2

#Lista numerica - PG de ordem 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8,9] #lista numerica
result = list(map(calcular_pg, numeros))

#print(list(map(calcular_pg, numeros)))

print("Proquressa geometrica: \n")
for n in result:
    print(n)