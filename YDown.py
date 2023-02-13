from pytube import YouTube
import os
import moviepy.editor as mp
import re
import flet as ft


def YDown(page, ft=ft):
    def Vyber(e): #Funkce na zvolení, jestli stáhnout mp3 nebo mp 4

        if Volba.value == "mp3":
            StahniTri(VstupniLink.value)
        elif Volba.value == "mp4":
            StahniCtyri(VstupniLink.value)
    page.update()

    def OznameniZacatek(e):
        zprava = ft.SnackBar(ft.Text("Stahování začalo", color=ft.colors.BLUE_900), bgcolor=ft.colors.BLUE_50)
        page.add(zprava)
        zprava.open = True
        page.update()
    def Oznamenikonec(e):
        zpravaK = ft.SnackBar(ft.Text("Stahování dokončeno", color="white"), bgcolor=ft.colors.GREEN_200)
        page.add(zpravaK)
        zpravaK.open = True
        page.update()

    def OznameniError(e):
        zpravaE = ft.SnackBar(ft.Text("ERROR - Stahování se nezdařilo", color="white"), bgcolor="red")
        page.add(zpravaE)
        zpravaE.open = True
        page.update()


    VstupniLink = ft.TextField(label="link", width=800) #Grafické rozhraní
    Volba = ft.Dropdown(
        width=150,
        label="Formát",
        options=[
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("mp4"),
        ]

    )
    Jmeno = ft.Text("", size=20, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER)
    Rozliseni = ft.Text("", size=20,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER)
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
        streem = YouTube(link)
        streem = streem.streams.get_highest_resolution()
        try:
            Jmeno.value = str("Název videa\n\n" + str(streem.title))
            Rozliseni.value = str("Formát\n\n.MP4")
            OznameniZacatek(e=0)
            streem.download("./MP4/")
            Oznamenikonec(e=0)
        except:
            OznameniError(e=0)

    def StahniTri(link):
        streem = YouTube(link)
        streem = streem.streams.get_highest_resolution()
        Jmeno.value = str("Název videa\n\n" + streem.title)
        Rozliseni.value = str("Formát\n\n.MP3")

        folder = "./MP3/"
        try:
            OznameniZacatek(e=0)
            YouTube(link).streams.filter(only_audio=True).first().download("./MP3/")

        except:
            OznameniError(e=0)

        try:
            for file in os.listdir(folder):
                if re.search('mp4', file):
                    mp4_cesta = os.path.join(folder, file)
                    mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
                    new_file = mp.AudioFileClip(mp4_cesta)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_cesta)
                    Oznamenikonec(e=0)
        except:
            OznameniError(e=0)


    return content


