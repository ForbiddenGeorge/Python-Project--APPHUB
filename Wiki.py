import requests
from bs4 import BeautifulSoup
import webbrowser
import flet as ft


#IMPORTOVANÁ APLIKACE Z GITHUBU
"""Funkce pomocí odkazu https://en.wikipedia.org/wiki/Special:Random
načte náhodný článek v html kódu, vypíše titulek a první odstavec
a nabídne jeho zobrazení ve webovém prohlížeči
"""
title = "Woow"
def Wikipe(page, ft=ft):

    # address = requests.get(
    #     "https://en.wikipedia.org/wiki/Special:Random")  # získá html adresu náhodného článku pomocí odkazu
    # html = BeautifulSoup(address.content, 'html.parser')  # získá html kód článku
    # title = html.find(id="firstHeading").text  # získá titulek článku
    def Najdi(cislo):
        address = requests.get(
            "https://en.wikipedia.org/wiki/Special:Random")  # získá html adresu náhodného článku pomocí odkazu
        html = BeautifulSoup(address.content, 'html.parser')  # získá html kód článku
        titlek = html.find(id="firstHeading").text  # získá titulek článku
        odstavec = html.find(id="mw-content-text", ).text
        nadpis.value = str(titlek)
        obsah.value = str(odstavec)
        title = titlek
        page.update()
        print(title)


    def Otevri(e):
        url = 'https://en.wikipedia.org/wiki/%s' %nadpis.value
        webbrowser.open(url)



    nadpis = ft.Text(value="",style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    obsah = ft.TextField(   width=800,
                            multiline=True,
                            min_lines=1,
                            max_lines=7,
                            label="První odstavec",
                            border=ft.InputBorder.UNDERLINE,
                            read_only=True
                            )

    context= ft.Column([
        ft.Row(
            [
                nadpis
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
               obsah
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="Jiný článek", on_click=Najdi),
                ft.TextField(disabled=True,border=ft.InputBorder.NONE, width=300),
                ft.ElevatedButton(text="Celý článek", on_click=Otevri)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    ])

    return context