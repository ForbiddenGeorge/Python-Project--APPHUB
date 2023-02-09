import flet as ft

def One(page, ft=ft):
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Vítejte v mé aplikaci, nahoře si můžete vybrat, kterou miniaplikaci chcete využít", size = 20,)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content