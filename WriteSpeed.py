import random
import time

import flet as ft

def Rychlost(page, ft=ft):
    def Napis(e):
        f = open('vety.txt').read()
        sentences = f.split('\n')
        veta.value = random.choice(sentences)
        pole.value = ""
        page.update()


    def Test(e):
        veta.value = "Konec testu"
        page.update()

    def Cas(e):
        while pole.on_focus:
            start = time.time()
            end = time.time()
            sec = start - end
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            mins = mins % 60
            cas.value = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
            print( cas.value)
            time.sleep(1)
            page.update()


    veta =ft.Text(selectable=False, value="", text_align=ft.TextAlign.CENTER, size=30, weight=ft.FontWeight.BOLD)
    pole = ft.TextField(width=700, label="Text", on_submit=Test, on_focus=Cas)
    cas = ft.Text(size=45, weight=ft.FontWeight.BOLD, value= "0:0:0.0")
    spravnost = ft.Text(size=30, weight=ft.FontWeight.W_200, value="Správnost pokusu")
    content= ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Přepište větu co nejrychleji dokážete", size=22)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Text("Kliknutím na pole začne časovač počítat, stisknutím klávesy Enter pokus ukončíte", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                   veta
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    pole
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text="Restartovat", on_click=Napis)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    cas
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    spravnost
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )


        ]
    )
    return content