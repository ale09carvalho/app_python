<<<<<<< HEAD
#NOTE - O SPLIT sepra os valores de uma variavel em uma lista

#varialvel
ano = "Jan, Fev, Mar, Abr, Jun, Jul, Ago, Set, Out, Nov, Dez"

#algarismo

try:
    # insere o separador para separar os valores e os insere em uma lista
    meses = ano.split(",")
    for mes in meses:
        print(mes)

except Exception as e:
=======
#NOTE - O SPLIT sepra os valores de uma variavel em uma lista

#varialvel
ano = "Jan, Fev, Mar, Abr, Jun, Jul, Ago, Set, Out, Nov, Dez"

#algarismo

try:
    # insere o separador para separar os valores e os insere em uma lista
    meses = ano.split(",")
    for mes in meses:
        print(mes)

except Exception as e:
>>>>>>> bbfefade35749fabdc42a6f2bc6e6443136ebf2b
    print(f"Nao foi possivel separa os valores. {e}.")