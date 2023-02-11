import flet as ft



def Rychlost(page, ft=ft):
    def Napis(e):
        veta.value = "It's Over, Anakin. I Have The High Ground!!"
        pole.value = ""
        page.update()

    def Test(e):
        veta.value = "Konec testu"
        page.update()

    veta =ft.Text(selectable=False, value="", text_align=ft.TextAlign.CENTER, size=30, weight=ft.FontWeight.BOLD)
    pole = ft.TextField(width=700, label="Text", on_submit=Test)
    content= ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Přepište větu co nejrychleji dokážete", size=22)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Text("Kliknutím na pole začne časovač počítem, stisknutím klávesy Enter pokus ukončíte", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                   veta
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    pole
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text="Restartovat", on_click=Napis)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),


        ]
    )
    return content