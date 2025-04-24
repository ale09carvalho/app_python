# declaraçao  de lista
lista = ["Maça", "Uva", "Laranja", "Melão", "Morango", "Manga"]

# imprime a lista
print(lista)
print(lista[0])  # imprime o primeiro elemento da lista
print(lista[1])  # imprime o segundo elemento da lista  
print(lista[2])  # imprime o terceiro elemento da lista

#exibindo itens um abaixo do outro
for fruta in lista:
    print(fruta)

#exibindo itens com o índice
for i in range(len(lista)):
    print(f"Item {i}: {lista[i]}")  # imprime o índice e o valor correspondente
    
