from pytube import YouTube
import os
import moviepy.editor as mp
import re
import flet as ft


def YDown(page, ft=ft):
    '''Hlavní funkce pro stahování a konverzí videí z Youtube'''
    def Vyber(e): #Funkce na zvolení, jestli stáhnout mp3 nebo mp 4, zavolá příslušnou funkci podle rozevíracího seznamu

        if Volba.value == "mp3":
            StahniTri(VstupniLink.value)
        elif Volba.value == "mp4":
            StahniCtyri(VstupniLink.value)
    page.update()
    def OznameniNacitani(e):
        '''Oznámení na spodu obrazovky(nepotřebné pro funkční chod programu)'''
        zprava = ft.SnackBar(ft.Text("Načítání videa", color=ft.colors.BLUE_900), bgcolor=ft.colors.BLUE_50)
        page.add(zprava)
        zprava.open = True
        page.update()

    def OznameniZacatek(e):
        '''Oznámení na spodu obrazovky(nepotřebné pro funkční chod programu)'''
        zprava = ft.SnackBar(ft.Text("Stahování začalo", color=ft.colors.BLUE_900), bgcolor=ft.colors.BLUE_50)
        page.add(zprava)
        zprava.open = True
        page.update()
    def Oznamenikonec(e):
        '''Oznámení na spodu obrazovky(nepotřebné pro funkční chod programu)'''
        zpravaK = ft.SnackBar(ft.Text("Stahování dokončeno", color="white"), bgcolor=ft.colors.GREEN_200)
        page.add(zpravaK)
        zpravaK.open = True
        page.update()

    def OznameniError(e):
        '''Oznámení na spodu obrazovky(nepotřebné pro funkční chod programu)'''
        zpravaE = ft.SnackBar(ft.Text("ERROR - Stahování se nezdařilo", color="white"), bgcolor="red")
        page.add(zpravaE)
        zpravaE.open = True
        page.update()

    # Grafické rozhraní
    VstupniLink = ft.TextField(label="link", width=800) #Textové pole pro link
    Volba = ft.Dropdown( #Volba mezi mp3 a mp4
        width=150,
        label="Formát",
        options=[
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("mp4"),
        ]

    )
    Jmeno = ft.Text("", size=20, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER) #Zobrazení jména videa
    Rozliseni = ft.Text("", size=20,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER) #Zobrazení formátu souboru pro potvrzení
    content = ft.Column(
        [
            ft.Row(
                [
                    VstupniLink,
                    Volba
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                ft.ElevatedButton(content=(ft.Text("Stáhni", size=20)), on_click=Vyber)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    Jmeno,
                    Rozliseni
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            )

        ],
    )
    def StahniCtyri(link):
        '''Funkce pro stáhnutí mp4 souboru'''
        streem = YouTube(link)
        OznameniNacitani(e=0)  # Oznameni
        streem = streem.streams.get_highest_resolution()  #Načtení videa
        try:
            Jmeno.value = str("Název videa\n\n" + str(streem.title)) #Načtení informací na obrrazovku
            Rozliseni.value = str("Formát\n\n.MP4") #Načtení informací na obrrazovku
            OznameniZacatek(e=0) #Oznameni
            streem.download("./MP4/") #stáhnutí videa do uvedené složky
            Oznamenikonec(e=0) #Oznameni
        except:
            OznameniError(e=0) #Oznameni

    def StahniTri(link):
        '''Funkce pro stáhnutí mp3 souboru'''
        streem = YouTube(link)
        OznameniNacitani(e=0)  # Oznameni
        streem = streem.streams.get_highest_resolution() #Načtení videa
        Jmeno.value = str("Název videa\n\n" + streem.title) #Načtení informací na obrrazovku
        Rozliseni.value = str("Formát\n\n.MP3") #Načtení informací na obrrazovku

        folder = "./MP3/"
        try:
            OznameniZacatek(e=0) #Oznameni
            YouTube(link).streams.filter(only_audio=True).first().download("./MP3/") #Stáhnutí audia, stále je to ale soubor mp4

        except:
            OznameniError(e=0) #Oznameni

        try:
            for file in os.listdir(folder):
                if re.search('mp4', file):
                    mp4_cesta = os.path.join(folder, file) #Nalezení souboru
                    mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
                    new_file = mp.AudioFileClip(mp4_cesta) #Vytvoření audio souboru
                    new_file.write_audiofile(mp3_path) #Jeho zápis
                    os.remove(mp4_cesta)
                    Oznamenikonec(e=0) #Oznameni
        except:
            OznameniError(e=0) #Oznameni


    return content


