import flet as ft

def NavBar(page, ft=ft):
    Navbar = ft.AppBar(
        toolbar_height= 40,
        automatically_imply_leading=True,
        bgcolor=ft.colors.BLUE_50,
        actions=[


            # DOLE JSOU NÁVRHY APLIKACÍ, NĚKTERÉ JSOU ZBYTEČNÉ , TAKŽE BUDU MĚNIT, ZÁROVEŇ UPRAVIT APP BAR ABY BYL HEZKÝ

            ft.ElevatedButton("Exchange",icon=ft.icons.CURRENCY_EXCHANGE, on_click=lambda _: page.go('/exchange'), width=180,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), )),
            ft.ElevatedButton("Kalkulačka", icon=ft.icons.CALCULATE_OUTLINED, on_click=None, width=180, #Pro náhled rozhraní
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
            ft.ElevatedButton("Youtube konvertor", icon=ft.icons.PLAY_ARROW_OUTLINED, on_click=lambda _: page.go('/Ydown'), width=180,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
            ft.ElevatedButton("Hádač čísel", icon=ft.icons.CONFIRMATION_NUMBER_OUTLINED, on_click=None, width=180, #Pro náhled rozhraní
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
            ft.ElevatedButton("Překladač", icon=ft.icons.TRANSCRIBE_OUTLINED, on_click=None, width=180, #Pro náhled rozhraní
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
            ft.ElevatedButton("Hodiny", icon=ft.icons.PUNCH_CLOCK_OUTLINED, on_click=None, width=180, #Pro náhled rozhraní
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
            ft.ElevatedButton("Rychlost psaní", icon=ft.icons.TEXT_FIELDS_ROUNDED, on_click=None, width=180, #Pro náhled rozhraní
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2))),
        ]
    )
    return Navbar