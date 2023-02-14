import flet as ft

from app_bar import NavBar
from FletRouter import Router

def main(page: ft.Page):
    '''Hlavní skript, obsahuje řídící skripty, udává vlastnosti okna a úvodní obrazovku'''
    page.appbar = NavBar(page, ft)
    myRouter = Router(page, ft)

    page.title = "APP HUB"
    page.window_width = 1260
    page.window_height = 600
    page.on_route_change = myRouter.route_change
    page.window_maximizable = False
    page.add(
        myRouter.body
    )

    page.go('/')

ft.app(target=main)















# class Menu(ft.UserControl):
#     def build(self):
#         view = ft.Column(
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
#                 ft.Text(value='APP HUB', style=ft.TextThemeStyle.HEADLINE_LARGE, color="blue"),
#                 ft.Row(
#                     wrap=True,
#                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     controls=[
#                         ft.ElevatedButton(
#                             style=ft.ButtonStyle(
#                                 shape=ft.RoundedRectangleBorder(radius=7),
#                             ),
#                             content=(Text("Kalkulačka", size=14)),
#                             bgcolor="LIGHTBLUE",
#                             color="WHITE",
#                             width=150,
#                             height=50,
#                             on_click=None
#                         ),
#                         ft.ElevatedButton(
#                             style=ft.ButtonStyle(
#                                 shape=ft.RoundedRectangleBorder(radius=7),
#                             ),
#                             content=(Text("Směnárna", size=14)),
#                             bgcolor="LIGHTBLUE",
#                             color="WHITE",
#                             width=150,
#                             height=50,
#                             on_click=None
#                         ),
#                         ft.ElevatedButton(
#                             style=ft.ButtonStyle(
#                                 shape=ft.RoundedRectangleBorder(radius=7),
#                             ),
#                             content=(Text("Youtube D/C", size=14)),
#                             bgcolor="LIGHTBLUE",
#                             color="WHITE",
#                             width=150,
#                             height=50,
#                             on_click=None
#                         ),
#                         ft.ElevatedButton(
#                             style=ft.ButtonStyle(
#                                 shape=ft.RoundedRectangleBorder(radius=7),
#                             ),
#                             content=(Text("ToDo", size=14)),
#                             bgcolor="LIGHTBLUE",
#                             color="WHITE",
#                             width=150,
#                             height=50,
#                             on_click=None
#                         )
#                     ]
#                 ),
#             ]
#         )
#         return view

# def main(page: ft.Page):
#     #page.window_frameless = True      nejde pak pohybovat s aplikací
#     page.window_maximizable=False
#     page.title = 'AppHub'
#     page.window_height = 650
#     page.window_width = 665
#     page.bgcolor = 'white'
#     domovskaStranka = Menu()
#     page.add(domovskaStranka)
#     page.update()
#
# ft.app(target=main)
