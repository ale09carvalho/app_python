#NOTE - O JOIN e um comando que pega os valores de uma lista e junta em uma unica variável

#lista
dias = [
    "Domingo",
    "Sengunda-feria",
    "terça-feira",
    "quanta-feira",
    "quinta-feira",
    "sexta-feira",
    "Sábado"
]
#insere um separador
#separador = ' , '
#separador = ' - '
#separador = ' \n '
separador = ' [ '

# junta os nomes em uma única variável
semana = separador.join(dias) #juntar os itens da lista

#exibe na tela
print(semana)
