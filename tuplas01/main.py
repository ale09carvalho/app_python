'''
TUPLAS
A diferença de lista e tupla é que em tuplas os valores não podem ser modificadas, pois elas funcionam como um conjunto de constantes ao invés de variáveis.
'''
dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado")

#LISTA a TUPLA
for dia in dias_semana:
    print(dia)

try:
    #tentativa de fazer operaçao de lista
    dias_semana.append("Sétima") # permite adicionar elementos a uma lista

    print("\n")

    for dia in dias_semana:
        print(dia)

except Exception as e:
    print(f"Nao foi possivel inserir item na tupla. {e}.")

