#dicionario
usuario = dict(nome="Fulando de Tal", idade=18, email="fulano@gmail.com")

#exibindo dados do dicionario
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")

    
