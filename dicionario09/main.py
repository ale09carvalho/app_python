import os

pessoas = []

try:
    while True:
        cadastrar = input("Deseja cadastrar nova pessoa? (s/n):")
        match cadastrar:
            case "s":
                #sempre uma pessoa nova
                pessoa = {}

                pessoa['nome'] = input("Informe o nome:")
                pessoa['email'] = input("Informe o e-mail:")
                pessoa['cpf'] = input("Informe o cpf:")
                
                #adciona a pessoa na lista
                pessoas.append(pessoa)

                os.system("cls")
                print(f"{pessoa.get('nome')} cadastrado com sucesso!")
                
                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")
                
                continue
            case "n":
                break

            case _:
                print("Opçao invalida.")
                continue

except Exception as e:
    print(f"Nao foi possível cadastrar pessoa. {e}.")