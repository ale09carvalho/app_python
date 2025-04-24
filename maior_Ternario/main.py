#declaraçao de variaveis
nome = input("Digite seu nome: ")

#parset para inteiro
idade = int(input("Digite sua idade: "))

#obs indentaçao e espaçamento são importantes em python
#estrutura de decisão com operador ternário
#operador ternário é uma forma reduzida de escrever uma estrutura de decisão simples de if-else
result = "é maior de idade." if idade >= 18 else "é menor de idade"

#exibe o resultado
print(f"{nome} {result}.")
#exibe o resultado com f-string


