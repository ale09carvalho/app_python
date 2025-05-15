#Yield é um tipo de retorno para retornar valores de forma iterativa, sem encerrar a execução da função.
# Declaraçao de funçao

# função
def verificar_matricula(nome):
    yield f"{nome} está com a documentação pedente."
    yield f"{nome} está com a documentação em fase de verificação."
    yield f"{nome} está aprovado e com a matricula pendente."
    yield f"{nome} está com a matrícula aprovada e efetivada."

