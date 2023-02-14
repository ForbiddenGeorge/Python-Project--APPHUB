import flet as ft
import translators as ts


def Prekladac(page, ft=ft):
    '''Tato funkce obsahuje celý překladač, tato funkce je volána podle svého unikátního identeifikátoru ve skriptu "FletRouter.py", používán je následně ve skriptu "app_bar.py"'''
    def Prace(e):
        '''Samotný překladač'''
        DruhyText.value = "" #vymažu předešlý výsledek
        Fromtext = str(PrvniText.value) #Načtu si text z prvního pole
        To = str(VolbaJazykaDruha.value)
        To = To[0:2] #překladač pracuje s jazyky jako dvoupísmennými značkami
        From = str(VolbaJazykaPrvni.value)
        if From == "automatická detekce jazyka":
            From = From[0:4]
        else:
            From = From[0:2]

        DruhyText.value = str(ts.translate_text(query_text=str(Fromtext), translator='deepl', from_language=From, to_language=To)) #Přeložení a následné vložení do pole
        '''lze použít spoustu překladačů,
         každý překladač však umí jiný soubor jazyků,
         bylo by tedy potřeba vytvořit variace nabídek jazyků pro různé překladače,
         aby si mohl uživatel zvolit svůj oblíbený překladač
         https: // github.com / UlionTse / translators / blob / master / README.md
         ['alibaba', 'argos', 'baidu', 'bing', 'caiyun', 'deepl', 'google', 'iciba', 'iflytek', 'itranslate',
         'lingvanex', 'niutrans', 'mglip', 'papago', 'reverso', 'sogou', 'tencent', 'translateCom', 'utibet', 'yandex',
         'youdao'] '''
        # lze použít spoustu překladačů,
        # třeba skvělej Deepl, či Yandex, každý překladač však umí jiný soubor jazyků,
        # bylo by tedy potřeba vytvořit variace nabídek jazyků pro různé překladače,
        # aby si mohl uživatel zvolit svůj oblíbený překladač
        # https: // github.com / UlionTse / translators / blob / master / README.md
        #['alibaba', 'argos', 'baidu', 'bing', 'caiyun', 'deepl', 'google', 'iciba', 'iflytek', 'itranslate',
        # 'lingvanex', 'niutrans', 'mglip', 'papago', 'reverso', 'sogou', 'tencent', 'translateCom', 'utibet', 'yandex',
        # 'youdao']

        page.update()

    def Prehod(e):
        ''' kliknutím na ikonku jazyků se přehodí honodty textových polí, tak i hondnoty rozevíracího seznamu'''
        pomocna = VolbaJazykaPrvni.value
        VolbaJazykaPrvni.value = VolbaJazykaDruha.value
        VolbaJazykaDruha.value = pomocna
        pomocna = PrvniText.value
        PrvniText.value = DruhyText.value
        DruhyText.value = pomocna
        page.update()

    PrvniText = ft.TextField  ( #První textové pole kam uživatel zadává text k přeložení
                        label="Text (max 300 znaků)",
                        width=500,
                        multiline=True,
                        min_lines=1,
                        max_lines=5,
                        filled=True,
                        bgcolor=ft.colors.BLUE_GREY_50,
                        border=ft.InputBorder.UNDERLINE,
                                )
    DruhyText = ft.TextField  (  #Druhé textové pole kde se zobrazí přeložený text
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
    znak = ft.IconButton (  #Grafiká ikonka co po klinutí otočí hodnoty viz. funkce 'Prehod(e)'
            icon=ft.icons.TRANSLATE_OUTLINED,
            width=50,
            on_click=Prehod,
            tooltip="Přehoďit"

                        )
    VolbaJazykaPrvni = ft.Dropdown(  #Prvni seznam jazyků, narozdíl od druhého má možnost 'automatická detekce jazyka'
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
    VolbaJazykaDruha = ft.Dropdown( #Druhy seznam jazyků
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



    context = ft.Column( #Grafický obsah stránky, několik řádků obsahující jednotlivé prvky, celé v jednom sloupci
        [
            # ft.Row(  Možné zavedení marginu od app baru
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