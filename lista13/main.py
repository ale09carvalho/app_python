lista_numerica = [1, 3, 6, 1.5, 2.7, 5.2]


#exibi a lista
for n in lista_numerica:
    print(n)

# soma oos itens da lista
print(f"Soma dos números da lista: {sum(lista_numerica)}")

# imprime em ordem decrescente
lista_numerica.sort(reverse=True)
print(lista_numerica)


# imprime em ordem crescente
lista_numerica.sort()
print(lista_numerica)