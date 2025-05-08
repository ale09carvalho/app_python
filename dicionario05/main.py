#TUPLA E DICIONARIO
chaves = ("nome","idade", "CPF", "telefone","email", "profissao")

usuario = {
chaves[0]: "Alessandra",
chaves[1]: 46,
chaves[2]:"111.222.333-40",
chaves[3]:"(61)999-44-02",
chaves[4]:"ale09@gmail.com",
chaves[5]:"Programador"
}

for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")

