import random
import time
import keyboard

import flet as ft



def Rychlost(page, ft=ft):


    def Napis(e):
        f = open('vety.txt').read()
        sentences = f.split('\n')
        veta.value = random.choice(sentences)
        pole.value = ""
        spravnost.value = "Správnost: "
        cas.value = "0:0.0"
        page.update()


    def Test(e):
        pocet = 0
        for i, c in enumerate(str(veta.value)):
            try:
                if pole.value[i] == c:
                    pocet += 1
            except:
                pass
        presnost = pocet / len(veta.value) * 100
        presnost = round(presnost, 2)

        spravnost.value = "Správnost: {0}".format(presnost) + "%"
        page.update()


    def Cas(e):
        setina = 0
        sekunda = 0
        minuta = 0
        if pole.value != "":
            pass
        else:
            while not keyboard.is_pressed("enter"):

                setina = setina +1
                time.sleep(0.01)
                if setina == 100:
                    setina = 0
                    sekunda = sekunda + 1
                if sekunda == 60:
                    sekunda = 0
                    minuta = minuta + 1
                cas.value = "{0}:{1}.{2}".format(int(minuta), int(sekunda), int(setina))
                page.update()
            else:
                cas.value = "{0}:{1}.{2}".format(int(minuta), int(sekunda), int(setina))
                page.update()


    veta =ft.Text(selectable=False, value="", text_align=ft.TextAlign.CENTER, size=30, weight=ft.FontWeight.BOLD)
    pole = ft.TextField(width=700, label="Text", on_submit=Test, on_focus=Cas)
    cas = ft.Text(size=45, weight=ft.FontWeight.BOLD, value= "0:0.0")
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
                    ft.Text("Kliknutím na textové pole začne časovač počítat, stisknutím klávesy Enter pokus ukončíte", size=16)
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
                    ft.ElevatedButton(text="Nová věta", on_click=Napis)
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