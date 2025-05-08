#deletar chave

#TUPLA E DICIONARIO
import os

chaves = ("nome","idade", "CPF", "telefone","email", "profissao")

usuario = {
chaves[0]: "Alessandra",
chaves[1]: 46,
chaves[2]:"111.222.333-40",
chaves[3]:"(61)999-44-02",
chaves[4]:"ale09@gmail.com",
chaves[5]:"Programador"
}

#listar a chave perguntar ao usuario qual dessas chave ele deseja  EXCLUIR

try:
    while True:
        #FIXME: Eliminar este comando dessa linha os.system("cls")
        for chave in usuario:
            print(f"{chave}: {usuario.get(chave)}")
        
        prosseguir = input("Deseja EXCLUIR alguma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input ("Informe o nome da chave que deseja EXCLUIR:")
                if chave_escolhida in chaves:                      
                    usuario.pop(chave_escolhida, Nome)
                    os.system("cls")
                    continue
                else:
                     os.system("cls")
                     print(f"{chave_escolhida} não existe.")
            case "n":
                break
            case _:
                print("Opçao inválida.")
                continue            
except Exception as e:
    print(f"Nao foi possivel atualizar os dados. {e}.")
