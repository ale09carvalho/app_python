#TODO

'''
Crie um programa que inicializa um dicionario, e o usuario adciona e insere os seguintes dados:
NOME, DATA DE NASCIMENTO, CPF, EMAIL, GENERO, TELEFONE, ALTURUA, PESO, TIPO SANGUINEO
AO FINAL o programa exibe os dados do usuario e informa seu IMC

'''
# declaraçao
usuario = {}

try:

    #Entrada de Dados
    usuario["nome"] = input ("Informe o nome:")
    usuario["data_nascimento"] = input("Informe a data de nascimento:")
    usuario["cpf"] = input("Informe o CPF:")
    usuario["email"] = input("Informe o e-mail:")
    usuario["genero"] = input("Informe o gênero:")
    usuario["telefone"] = input("Informe o telefone:")
    usuario["altura"] = float(input("Informe a altura em metros:").replace(",", "."))
    usuario["peso"] = float(input("Informe o peso em Kg:").replace(",", "."))
    usuario["tipo_sanguineo"] = input("Informe o seu tipo sanguineo:")

    # Exibe os dados do usuario
    for chave in usuario:
        print(f"{chave.title()}: {usuario.get(chave)}")
    
    # calcular o IMC usuario
    imc = usuario.get("peso")/usuario.get("altura")**2

    # exibe o valor do IMC
    print(f"IMC de {usuario.get("nome")}: {imc:,.2f}")

    # exibe o diagnostico do usuario com base no valor do IMC
    if imc <= 18.5:
        print(f"Usuario esta abaixo do peso")
    elif imc < 25:
         print(f"{usuario.get("nome")} esta no peso ideal. PARABENS!!!")
    elif imc < 30:
        print(f"{usuario.get("nome")} esta acima do peso ideal")
    elif imc < 35:
         print(f"{usuario.get("nome")} esta obeso.")
    elif imc < 40:
         print(f"{usuario.get("nome")} esta com obesidade nivel II")
    else:
         print(f"{usuario.get("nome")} esta com obseidade morbida. ATENCÃO PROCURE UM MÉDICO")

except Exception as e:
    print(f"Nao foi possivel inserir os dados {e}")