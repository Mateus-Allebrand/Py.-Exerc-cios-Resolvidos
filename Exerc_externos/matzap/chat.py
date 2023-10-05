import flet as ft
from funcionalidades import entrar_chat

def main(pagina):
    texto = ft.Text("MATZAP")
    pagina.add(texto)
    

    nome_usuario = ft.TextField()

    popup = ft.AlertDialog(
        open= False,
        modal= True,
        title= ft.Text("BEM VINDO AO MATZAP"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar")],

    )



    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    #Criando Botão
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)
    pagina.add(botao_iniciar)






ft.app(target=main, view=ft.WEB_BROWSER)
