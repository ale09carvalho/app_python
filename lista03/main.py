#declaraçao de variavel
texto = "Este e um texto comum!"

#separando os caracteres do texto
for i in texto:
    print(i)  # imprime cada caractere do texto

#separando os caracteres do texto com o índice
for i in range(len(texto)):
    print(f"Item {i}: {texto[i]}")  # imprime o índice e o caractere correspondente