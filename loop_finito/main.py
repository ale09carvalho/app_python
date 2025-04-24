#Tratamento de exceção
try:
    #declaração de variáveis
    n = int(input("Informe um número inteiro positivo "))
    
    #loop
    while n >= 0:
        print(n)
        n -= 1       
        
except Exception as e:
    print(f"Numerio inválido. {e}")
