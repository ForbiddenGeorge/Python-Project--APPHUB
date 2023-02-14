import requests
from bs4 import BeautifulSoup
import webbrowser
import flet as ft


#IMPORTOVANÁ APLIKACE Z GITHUBU
"""Funkce pomocí odkazu https://en.wikipedia.org/wiki/Special:Random
načte náhodný článek v html kódu, vypíše titulek a první odstavec
a nabídne jeho zobrazení ve webovém prohlížeči
"""
def Wikipe(page, ft=ft):
    '''Hlavní funkce volaná řídícím skriptem'''
    def Najdi(cislo):
        '''Najde náhodný článek a jeho titulek, data následně načte a zobrazí'''
        address = requests.get(
            "https://en.wikipedia.org/wiki/Special:Random")  # získá html adresu náhodného článku pomocí odkazu
        html = BeautifulSoup(address.content, 'html.parser')  # získá html kód článku
        titlek = html.find(id="firstHeading").text  # získá titulek článku

        odstavec = html.find(id="mw-content-text", ).text #získá první odstavec a ten zobrazí
        obsah.value = str(odstavec)
        #odstavec = html.find_all('p')
        #obsah.value = str(odstavec[0].text)

        nadpis.value = str(titlek)
        title = titlek
        page.update()


    def Otevri(e):
        '''Otevře webový prohlížeč se stránkou na daný článek'''
        url = 'https://en.wikipedia.org/wiki/%s' %nadpis.value
        webbrowser.open(url)



    nadpis = ft.Text(value="",style=ft.TextThemeStyle.HEADLINE_MEDIUM) #Hlavní nadpis
    obsah = ft.TextField(   width=800, #Pole obsahující odstavec textu
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
            [   #Dvě tlačítka, jedno na načtení jiného článku, druhé na otevření webové stránky
                ft.ElevatedButton(text="Jiný článek", on_click=Najdi),
                ft.TextField(disabled=True,border=ft.InputBorder.NONE, width=300), #Výplňový blok kvůli estetice
                ft.ElevatedButton(text="Celý článek", on_click=Otevri)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    ])

    return context