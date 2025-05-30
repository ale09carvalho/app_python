import flet as ft
import random

# Aplicativo Flet simples para sortear nomes

def main(page: ft.Page):
    nomes = []

    # Função para adicionar nome à lista
    def adicionar_nome(e):
        nome = campo_nome.value.strip()
        if nome:
            nomes.append(nome)
            lista_nomes.value = ", ".join(nomes)
            campo_nome.value = ""
            campo_nome.error_text = ""
        else:
            campo_nome.error_text = "Digite um nome."
        page.update()

    # Função para sortear um nome da lista
    def sortear_nome(e):
        if nomes:
            nome_sorteado.value = f"Nome sorteado: {random.choice(nomes)}"
            nome_sorteado.color = ft.colors.BLUE
        else:
            nome_sorteado.value = "Adicione nomes antes de sortear."
            nome_sorteado.color = ft.colors.RED
        nome_sorteado.update()

    # Configurações da página
    page.title = "Sorteador de Nomes"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    campo_nome = ft.TextField(label="Digite um nome", on_submit=adicionar_nome)
    lista_nomes = ft.Text(value="", size=16)
    nome_sorteado = ft.Text(size=20, weight="bold")

    # Layout da página
    page.add(
        ft.SafeArea(
            ft.Column([
                ft.Text("Sorteador de Nomes", size=30, weight="bold"),
                campo_nome,
                ft.ElevatedButton("Adicionar Nome", on_click=adicionar_nome),
                ft.Text("Nomes adicionados:", size=18, weight="bold"),
                lista_nomes,
                ft.ElevatedButton("Sortear Nome", on_click=sortear_nome),
                nome_sorteado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

ft.app(main)
