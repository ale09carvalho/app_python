#Tratamento de exceção
try:
    
    #declaração de variáveis
    x = int(input("Informe um número inteiro: "))


    #saida de dados
    print(f"O número informado foi {x}.")
except  Exception as e:
    print(f"Não foi possível ler o valor informado pelo usuario. {e}")
finally:
    print("Fim Programa executado com sucesso!.")
    
