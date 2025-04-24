#declaraçao de variaveis
nome = input("Informe o nome do aluno: ")
nota = float(input("Informe a nota do aluno: "))

#verifica se o aluno é aprovado ou reprovado
#nota minima 0
#nota maxima 10
## reticencia e valida dentro da liguagem python ....
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} foi APROVADO.")
    elif nota >= 5:
        print(f"{nome} está de RECUPERAÇÃO.")
    else:
        print(f"{nome} está REPROVADO.")
else:
    print("Nota inválida!")
#fim do programa



