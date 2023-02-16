import random
import time
import keyboard

import flet as ft



def Rychlost(page, ft=ft):
    '''Hlavní flunkce volaná řídícím skriptem
    Skript pro kontrolu rychlosti a přesnosti psaní
    '''

    def Napis(e):
        '''Tato funkce vybere z textového souboru náhodnou testovací větu a tu následně zobrazí na obrazovce'''
        f = open('vety.txt').read() #Oteření souboru s větami
        sentences = f.split('\n') #Rozdělení jednotlivých vět po řádcích
        veta.value = random.choice(sentences)
        '''Vynulování všech hodnot pro novou větu'''
        pole.value = ""
        spravnost.value = "Správnost: "
        cas.value = "0:0.0"
        page.update()


    def Test(e):
        '''Funkce kotrolujíí přesnost přepisu'''
        pocet = 0
        for i, c in enumerate(str(veta.value)):
            try:
                if pole.value[i] == c: #Pokud se charakter věty rovná charakteru napsané věty, přičtě se 1 k počtu správných charakterů, jinak se nic neděje
                    pocet += 1
            except:
                pass
        presnost = pocet / len(veta.value) * 100 #počet správných charakterů / celkovým počtem charakterů * 100 abychom to měli v procenteech
        presnost = round(presnost, 2)

        spravnost.value = "Správnost: {0}".format(presnost) + "%" #Vypsání procentuálního výsledku
        page.update()


    def Cas(e):
        '''Stopkyw'''
        setina = 0
        sekunda = 0
        minuta = 0
        if pole.value != "":
            pass
        else:
            while not keyboard.is_pressed("enter"): #Dokud není stiknut Enter, časovač stále běží

                setina = setina +1
                time.sleep(0.01)
                if setina == 100: #Za každých sto setin se připíše jedna sekunda a setiny se vynulují
                    setina = 0
                    sekunda = sekunda + 1
                if sekunda == 60: # Za 60 vteřín se přičte minuta a sekundy se vynulují
                    sekunda = 0
                    minuta = minuta + 1
                cas.value = "{0}:{1}.{2}".format(int(minuta), int(sekunda), int(setina)) #Vypsání nového času na obrazovku
                page.update()
            else:
                cas.value = "{0}:{1}.{2}".format(int(minuta), int(sekunda), int(setina))
                page.update()


    veta =ft.Text(selectable=False, value="", text_align=ft.TextAlign.CENTER, size=30, weight=ft.FontWeight.BOLD) #Hlavní testovací věta
    pole = ft.TextField(width=700, label="Text", on_submit=Test, on_focus=Cas) #Pole kam uživatel přepisuje větu
    cas = ft.Text(size=45, weight=ft.FontWeight.BOLD, value= "0:0.0") # zobrazení času
    spravnost = ft.Text(size=30, weight=ft.FontWeight.W_200, value="Správnost pokusu") #Text pro výsledné zobrazení textu
    content= ft.Column( # Grafické rozložení aplikace
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