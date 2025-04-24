# tratamento de exeções
try: 
    # repetiçao do algoritmo com o uso de while True
    while True:  
        #declaraçao de variáveis
        nome = input("Informe seu nome: ") 
        idade = int(input("Informe sua idade: "))
        
        #saida de dados
        print(nome, "é maior de idade." if idade >= 18 else "é menor de idade.") # operador ternário 
        
        #decisao
        continuar = input("Deseja continuar? (s/n) ")
        
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
except Exception as e:
    print(f"Dados informado invalidos. {e}") 
finally:
    print("Fim do programa.")