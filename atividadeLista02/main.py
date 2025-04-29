#TODO - : Atividade
'''
Crie um programa em que o usuario informa varias notas de um aluno de 0 a 10 (quantas notas ele quiser inserir),
 e ao final, o programa calcule a média desse aluno e informa se ele esta aprovado, ou de recuperaçao ou reprovado
 Obs: Media para aprovaçao: 7 Media para recuperaçao: entre 5 e 7. abaixo de 5 : Reprovado.

'''
#declaraço de variavel
notas = []

#tratamento de exceçao
try:
    while True:
        #Usuario informa o nome
        numero_decimal = float(input("Informe uma nota de 0 a 10, ou de enter para sair: ").replace(",", "."))
        
        media = sum(notas) / len(notas)
        print(f"A média do aluno é: {media:.2f}")
        
        if media >= 7:
            print("Situação: Aprovado")
        elif 5 <= media < 7:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")

except Exception as e:    
    print(f"Nao foi possivel inserir dados na lista. (exceçao: {e})")




