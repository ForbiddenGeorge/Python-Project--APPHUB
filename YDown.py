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

    VstupniLink = ft.TextField(label="link", width=800) #Grafické rozhraní
    Volba = ft.Dropdown(
        width=150,
        label="Formát",
        options=[
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("mp4"),
        ]

    )
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
            )

        ],
    )
    def StahniCtyri(link):
        streem = YouTube(link)
        streem = streem.streams.get_highest_resolution()
        try:
            streem.download("./MP4/")
        except:
            pass

    def StahniTri(link):
        folder = "./MP3/"
        try:
            YouTube(link).streams.filter(only_audio=True).first().download("./MP3/")
        except:
            pass

        try:
            for file in os.listdir(folder):
                if re.search('mp4', file):
                    mp4_cesta = os.path.join(folder, file)
                    mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
                    new_file = mp.AudioFileClip(mp4_cesta)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_cesta)
        except:
            pass


    return content


