import flet as ft

def main (page: ft.Page):
    page.window_center()
    page.bgcolor = '#ffffff'
    page.window_width = '400'
    page.window_height = '550'
    page.window_resizable = False
    page.window_maximizable = False
    





    img = ft.Image(
        src=f"avatar.png.png",
        width=50, height=50,
        fit=ft.ImageFit.CONTAIN,
    )


    img2 = ft.Image(
        src=f"calculadora.png",
        width=50, height=50,
        fit=ft.ImageFit.CONTAIN,
    )




    page.add(img, img2 )
ft.app(target=main)
