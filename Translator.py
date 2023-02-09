import flet as ft
from googletrans import Translator
#from deep_translator import GoogleTranslator
import translators as ts


#from translate import Translator

def Prekladac(page, ft=ft):
    def Prace(e):
        DruhyText.value = ""
        Fromtext = str(PrvniText.value)
        print(Fromtext)
        To = str(VolbaJazykaDruha.value)
        To = To[0:2]
        From = str(VolbaJazykaPrvni.value)
        if From == "automatická detekce jazyka":
            DruhyText.value = str(ts.translate_text(query_text=str(Fromtext), translator='google',
                                                    from_language='auto', to_language=To))
        else:
            From = From[0:2]
            DruhyText.value = str(ts.translate_text(query_text=str(Fromtext),translator='google',
                          from_language=From,to_language=To))
        # prekladac = Translator()
        # DruhyText.value = prekladac.translate(text=Fromtext, dest=To, src=From)
        page.update()

    def Prehod(e):
        pomocna = VolbaJazykaPrvni.value
        VolbaJazykaPrvni.value = VolbaJazykaDruha.value
        VolbaJazykaDruha.value = pomocna
        pomocna = PrvniText.value
        PrvniText.value = DruhyText.value
        DruhyText.value = pomocna
        page.update()


        # preklad = Translator(from_lang=From, to_lang=To)
        # vysledek =preklad.translate(Fromtext)
        # DruhyText.value = vysledek
        # page.update()

    PrvniText = ft.TextField  (
                        label="Text (max 300 znaků)",
                        width=500,
                        multiline=True,
                        min_lines=1,
                        max_lines=5,
                        filled=True,
                        bgcolor=ft.colors.BLUE_GREY_50,
                        border=ft.InputBorder.UNDERLINE,
                                )
    DruhyText = ft.TextField  (
                        label="Text (max 300 znaků)",
                        multiline=True,
                        width=500,
                        filled=True,
                        min_lines=1,
                        max_lines=5,
                        bgcolor=ft.colors.BLUE_GREY_50,
                        border=ft.InputBorder.UNDERLINE,
                        value=" "
                                )
    znak = ft.IconButton (
            icon=ft.icons.TRANSLATE_OUTLINED,
            width=50,
            on_click=Prehod,
            tooltip="Přehoďit"

                        )
    VolbaJazykaPrvni = ft.Dropdown(
                    width=300,
                    label="Jazyk",
                    options=[
                        ft.dropdown.Option('automatická detekce jazyka'),
                        ft.dropdown.Option('en (angličtina)'),
                        ft.dropdown.Option('ja (japonština)'),
                        ft.dropdown.Option('cs (čeština)'),
                        ft.dropdown.Option('it (Italština)'),
                        ft.dropdown.Option('ar (arabština)'),
                        ft.dropdown.Option('ko (korejština)'),
                        ft.dropdown.Option('la (latina)'),
                        ft.dropdown.Option('bg (bulharština)'),
                        ft.dropdown.Option('hr (chorvatština)'),
                        ft.dropdown.Option('no (Norština)'),
                        ft.dropdown.Option('pl (polština)'),
                        ft.dropdown.Option('pt (portugalština)'),
                        ft.dropdown.Option('ru (ruština)'),
                        ft.dropdown.Option('sk (slovenština)'),
                        ft.dropdown.Option('de (němčina)'),
                        ft.dropdown.Option('es (španělština)'),
                        ft.dropdown.Option('hi (Indština)'),
                        ft.dropdown.Option('el (řečtina)'),

                    ]
                )
    VolbaJazykaDruha = ft.Dropdown(
        width=300,
        label="Jazyk",
        options=[
            ft.dropdown.Option('en (angličtina)'),
            ft.dropdown.Option('ja (japonština)'),
            ft.dropdown.Option('cs (čeština)'),
            ft.dropdown.Option('it (Italština)'),
            ft.dropdown.Option('ar (arabština)'),
            ft.dropdown.Option('ko (korejština)'),
            ft.dropdown.Option('la (latina)'),
            ft.dropdown.Option('bg (bulharština)'),
            ft.dropdown.Option('hr (chorvatština)'),
            ft.dropdown.Option('no (Norština)'),
            ft.dropdown.Option('pl (polština)'),
            ft.dropdown.Option('pt (portugalština)'),
            ft.dropdown.Option('ru (ruština)'),
            ft.dropdown.Option('sk (slovenština)'),
            ft.dropdown.Option('de (němčina)'),
            ft.dropdown.Option('es (španělština)'),
            ft.dropdown.Option('hi (Indština)'),
            ft.dropdown.Option('el (řečtina)'),
        ]
    )



    context = ft.Column(
        [
            # ft.Row( MARGIN OD APPBARU
            #     [
            #         ft.TextField(
            #         width=1050,
            #         border=ft.InputBorder.NONE,
            #         disabled=True,
            #                     ),
            #     ]
            # ),
            ft.Row(
                [
                VolbaJazykaPrvni,
                ft.TextField(
                    width=450,
                    border=ft.InputBorder.NONE,
                    disabled=True,
                            ),
                    VolbaJazykaDruha
                ],
                alignment=ft.MainAxisAlignment.CENTER
                    ),
            ft.Row(
                [
                    ft.Column(
                        [
                            PrvniText
                        ],
                    ),
                    ft.Column(
                        [
                            znak
                        ],
                    ),
                    ft.Column(
                        [
                            DruhyText
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Přelož",
                        on_click=Prace,
                        width=100,
                        height=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return context