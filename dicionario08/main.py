'''
Listas são usadas para guardar dados de mesmo tipo e significado, de modo que a ordem pode fazer diferença.
#Dicionario é criado por chaves e os objetos são compostos por uma chave,


'''
# LISTA DENTRO DICIONARIO

pessoas = [
    {
        'nome': "Fulano de Tal",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano de Souza",
        'idade': 15,
        'email': "cicranoo@gmail.com"
    },
    {
        'nome': "Beltrano da Silva",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }
]

# listando 
for pessoa in pessoas:
    print(f"{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}:{pessoa.get(chave)}.")

