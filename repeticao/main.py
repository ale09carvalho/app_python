# Tratamento de exceção
try:  
    #declaraçao de variáveis
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    
    #saida de dados
    print(nome, "é maior de idade." if idade >= 18 else nome, "é menor de idade.") # operador ternário 
    
except Exception as e:
    print(f"Dados informado invalidos. {e}") 