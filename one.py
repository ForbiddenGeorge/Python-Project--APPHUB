import flet as ft

def One(page, ft=ft):
    '''Úvodní stránka s jednoduchým textem'''
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("\nVítejte v mé aplikaci, nahoře si můžete vybrat, kterou miniaplikaci chcete využít",
                            size = 20, text_align= ft.TextAlign.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content