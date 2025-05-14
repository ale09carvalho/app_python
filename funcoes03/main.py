'''
13/05/2025
Funções pequenos blocos de programação que podem ser chamados no algoritmo principal.
Isso possibilita que seu código seja dividido em partes menores.
'''
#Funçao com parametro e com retorno --> retornar uma string

#declaraçao de funçao ---
#return marca o encerramento da funçao

def dar_boas_vindas(nome, curso):
    return f"{nome}, seja bem vindo ao curso de {curso}!"

# Algoritmo principal
nome = input("Informe seu nome: ")
curso = input("Informe o curso:")

# outra forma de emitir a saida de dados com melhor
saida = dar_boas_vindas(curso, nome)
print(saida)