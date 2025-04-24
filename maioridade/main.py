
#declaraçao de variaveis
nome = input("Digite seu nome: ")

#parset para inteiro
idade = int(input("Digite sua idade: "))

#obs indentaçao e espaçamento são importantes em python
#estrutura de decisão
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")