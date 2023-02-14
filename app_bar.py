import flet as ft

def NavBar(page, ft=ft):
    '''Skript, který sprostředkovává vrchní menu'''
    sirka = 252 #šířka jednoho tlačítka
    Navbar = ft.AppBar(
        toolbar_height= 40,
        automatically_imply_leading=True,
        bgcolor=ft.colors.BLUE_50,
        actions=[ #Položky menu
            ft.ElevatedButton("Exchange",icon=ft.icons.CURRENCY_EXCHANGE, on_click=lambda _: page.go('/exchange'), width=sirka,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), )),

            ft.ElevatedButton("Youtube konvertor", icon=ft.icons.PLAY_ARROW_OUTLINED, on_click=lambda _: page.go('/Ydown'), width=sirka,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),

            ft.ElevatedButton("Random Wiki", icon=ft.icons.TEXT_FIELDS_OUTLINED, on_click=lambda _: page.go('/Wiki'), width=sirka,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),

            ft.ElevatedButton("Překladač", icon=ft.icons.TRANSCRIBE_OUTLINED, on_click=lambda _: page.go('/Translate'), width=sirka,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),

            ft.ElevatedButton("Rychlost psaní", icon=ft.icons.TEXT_FIELDS_ROUNDED, on_click=lambda _: page.go('/Speed'), width=sirka,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
        ]
    )
    return Navbar