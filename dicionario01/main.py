'''
dicionário no Python é um tipo de coleção similar às listas, a diferença é que agora, para cada valor do dicionário, há uma chave associada àquele valor.
serealizar
'''
#declaraçao de dicionario
usuario = {
    'nome': "Alessandra",
    'idade': 46,
    'profissão': "Programador"
}
# Exibir dados 1
print(usuario)
'''
try:
    # Exibir dados 2 - porem nao exibi muito a respeito do erro
    
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissão']}")
    print(f"CPF: {usuario['CPF']}")

except Exception as e:
    print(f"Nao foi possivel separa os valores. {e}.")
'''
# Exibir dados 3
# var.get ignora nao interrompe a execuçao e CPF: None - retorna propriedades não relacionadas
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Profissão: {usuario.get('profissão')}")
print(f"CPF: {usuario.get('CPF')}")