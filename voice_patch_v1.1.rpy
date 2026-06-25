init offset = 1

# main screens
screen qq_menu():
    zorder 5

    if _history_list:
        key 'K_e' action Function(renpy.alt, renpy.filter_text_tags(_history_list[-1].what, ()), _update_screens=False)

    key 'K_q' action If(
        preferences.self_voicing_volume_drop != 0.5,
        Preference("self voicing volume drop", 0.5),
        Preference("self voicing volume drop", 1.0)
    )

    key "t" action Language(None)
    key "y" action Language("english")

    hbox:
        yalign 0.99
        xalign 0.5
        spacing 190

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q01.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu("history")
            tooltip (450, __("ИСТОРИЯ"))
            at for_say_buttons
            alt __("ИСТОРИЯ")

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q02.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action Preference("auto-forward", "toggle")
            tooltip (680, __("АВТО"))
            at for_say_buttons
            alt __("АВТО")

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q03.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action Skip()
            tooltip (935, __("ПЕРЕМОТКА"))
            at for_say_buttons
            alt __("ПЕРЕМОТКА")

        button:
            xsize 54
            ysize 40
            background "interface/quick_menu/q04.png"
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu("quick_menu")
            tooltip (1170, __("МЕНЮ"))
            at for_say_buttons
            alt __("МЕНЮ")

        button:
            xsize 54
            ysize 40
            hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
            action ShowMenu('dictionary_scr')
            tooltip (1420, __("СЛОВАРЬ"))
            if not new_words:
                add "q_base":
                    align (.5,.5)
                    at for_say_buttons
            else:
                add "q_base":
                    align (.5,.5)
                    at for_say_buttons_new
            alt __("СЛОВАРЬ")

        if window_shake:
            at win_shake

    button:
        xpos 1675
        ypos 850
        xsize 54
        ysize 40
        background "interface/quick_menu/q07.png"
        hover_sound "sounds/menu/menu-button-select-new-3-27_dB.ogg"
        activate_sound "sounds/menu/menu-button-push-1_1-14_dB.ogg"
        action HideInterface()
        tooltip (None, __("СКРЫТЬ"))
        if window_shake:
            at for_say_buttons, win_shake
        else:
            at for_say_buttons
        alt __("СКРЫТЬ")

    if (tt := GetTooltip()):
        if tt[0] is not None:
            text "{noalt}[tt[1]]" yalign 0.99 yoffset 5 xpos tt[0] xanchor 1. size 44
        else:
            text "{noalt}[tt[1]]" xpos 1675 ypos 870 xanchor 1. yanchor .5 size 38

screen quick_menu():
    tag menu
    zorder 100
    modal True
    style_prefix "quick"

    on "show" action Play("test_five", "sounds/menu/menu-pause-3.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-pause-3.ogg")

    add "bg_menu_quick"

    default ms1 = __("Приглушить музыку и звуки")
    default ms2 = __("Произнести последнюю реплику")

    text "{alt}Q: [ms1]"
    text "{alt}E: [ms2]"

    vbox:
        xalign 0.47
        yalign 0.38

        textbutton _("Продолжить"):
            background Null(10, 10)
            action Return()
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

        textbutton _("Древо Истории"):
            action Hide(), Function(GetFlowchartData, story_manager = story_manager)
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

        textbutton _("Сохранить"):
            action ShowMenu("save")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
            sensitive is_save_allowed

        textbutton _("Загрузить"):
            action ShowMenu("load")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

        textbutton _("Настройки"):
            action ShowMenu("preferences")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

        textbutton _("В меню"):
            action MainMenu(confirm=True)
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

        textbutton _("Выход"):
            action Quit(confirm=True)
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        at qm_elements

    vbox:
        xalign 0.47
        yalign 0.38

        button:
            background "interface/main_meny/plaska.png"
            text _("Продолжить"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Return()
            default_focus True

        button:
            background "interface/main_meny/plaska2.png"
            text _("Древо Истории"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Hide(), Function(GetFlowchartData, story_manager = story_manager)

        button:
            background "interface/main_meny/plaska.png"
            text _("Сохранить"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("save")
            sensitive is_save_allowed

        button:
            background "interface/main_meny/plaska.png"
            text _("Загрузить"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("load")

        button:
            background "interface/main_meny/plaska.png"
            text _("Настройки"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("preferences")

        button:
            background "interface/main_meny/plaska.png"
            text _("В меню"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action MainMenu(confirm=True)

        button:
            background "interface/main_meny/plaska.png"
            text _("Выход"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Quit(confirm=True)
        at qm_elements

    on "show" action Show("block_screen")
    timer 0.4 action Hide("block_screen")

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background
    if persistent.animal_unlock[3]:
        add "interface/main_meny/fon_05.png"
    if persistent.animal_unlock[0]:
        add "interface/main_meny/fon_02.png"
    if persistent.animal_unlock[4]:
        add "interface/main_meny/fon_06.png"
    add "menu002_1"
    add "menu002_2"
    add "chastichka_2"
    if persistent.animal_unlock[1]:
        add "interface/main_meny/fon_03.png"
    if persistent.animal_unlock[2]:
        add "interface/main_meny/fon_04.png"
    add "menu001_1"
    add "menu001_2"
    add "chastichka_1_1"
    add "main_menu_bg"
    add "chastichka_1_2"

    add "bg_black" at mm_bg_diss_1to0

    if preferences.language != "japan":
        add "[logo!t]" xalign 0.47 yalign 0.09 at mm_elements
    else:
        add "interface/main_meny/logo_en.png" xalign 0.47 yalign 0.09 at mm_elements

    on "show" action ShowTransient(lang_mm_screen[preferences.language])
    on "replace" action ShowTransient(lang_mm_screen[preferences.language])
    on "replaced" action Hide(lang_mm_screen[preferences.language])
    on "hide" action Hide(lang_mm_screen[preferences.language])

    fixed:
        xfit True
        yfit True

        ypos 100

        at mm_elements
        hbox:
            xpos 80
            ypos 100
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_01.png"
                if preferences.language != None:
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language(None)
                hovered ShowTransient("main_menu_language_message_rus")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "РУС":
                    xpos 40
                    ypos 105
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Русский"
                at mm_but_lang
            at mm_elements

        hbox:
            xpos 180
            ypos 200
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_02.png"
                if preferences.language != "english":
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language("english")
                hovered ShowTransient("main_menu_language_message_eng")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "ENG":
                    xpos 35
                    ypos 105
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "English"
                at mm_but_lang
            at mm_elements

        hbox:
            xpos 80
            ypos 300
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_04.png"
                if preferences.language != "chinese":
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language("chinese")
                hovered ShowTransient("main_menu_language_message_chi")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "{alt}中文"
                at mm_but_lang
            at mm_elements

        hbox:
            xpos 180
            ypos 400
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_02.png"
                if preferences.language != "italiano":
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language("italiano")
                hovered ShowTransient("main_menu_language_message_ita")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "ITA":
                    xpos 35
                    ypos 105
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Italiano"
                at mm_but_lang
            at mm_elements

        hbox:
            xpos 80
            ypos 500
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_01.png"
                if preferences.language != "turkish":
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language("turkish")
                hovered ShowTransient("main_menu_language_message_tur")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "TÜR":
                    xalign .5
                    xoffset 5
                    ypos 105
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Türkçe"
                at mm_but_lang
            at mm_elements

        hbox:
            xpos 180
            ypos 600
            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_02.png"
                if preferences.language != "japan":
                    hover_sound "sounds/menu/menu-button-select-3.ogg"
                else:
                    hover_sound None
                activate_sound "sounds/menu/language-sellect-1.ogg"
                action Language("japan")
                hovered ShowTransient("main_menu_language_message_jpn")
                unhovered ShowTransient(lang_mm_screen[preferences.language])
                text "JPN":
                    xalign .5
                    xoffset -5
                    ypos 105
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "日本語"
                at mm_but_lang
            at mm_elements

    vbox:
        xalign 0.47
        yalign 0.4
        textbutton _("Новая игра"):
            action Show("black_screen")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        textbutton _("Загрузить"):
            action ShowMenu("load")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        textbutton _("Настройки"):
            action ShowMenu("preferences")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        textbutton _("Об авторах"):
            action ShowMenu("about_me")
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        textbutton _("Выход"):
            action Quit(confirm=False)
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False
        at mm_elements

    vbox:
        xalign 0.47
        yalign 0.4
        button:
            background "interface/main_meny/plaska.png"
            text _("Новая игра"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Show("black_screen")
            default_focus True
        button:
            background "interface/main_meny/plaska.png"
            text _("Загрузить"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("load")
        button:
            background "interface/main_meny/plaska.png"
            text _("Настройки"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("preferences")
        button:
            background "interface/main_meny/plaska.png"
            text _("Об авторах"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action ShowMenu("about_me")
        button:
            background "interface/main_meny/plaska.png"
            text _("Выход"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Quit(confirm=False)
        at mm_elements

    key "game_menu" action Quit(confirm=True)

    if not config.developer:
        on "show" action Show("block_screen")
        timer 3.2 action Hide("block_screen")

    if config.developer:
        use devolver_menu()

screen about_me():
    tag menu
    modal True

    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")

    add "bg_menu_about" at conf_fon

    viewport id "autor":
        pagekeys True
        draggable True
        mousewheel True
        xsize 1600
        ysize 900
        xalign 0.5
        yalign 0.5

        has vbox
        xalign 0.5
        spacing 46
        xsize 1600

        vbox:
            style_group "about"
            xsize 1600
            xalign 0.5
            at for_yes_no_10

            for line in titles_content:
                if not isinstance(line, (tuple, list)):
                    null height 35

                    text "{size=+10}[line!t]" xalign 0.5:
                        if preferences.language == "japan":
                            font other_font_interface
                    null height 35

                else:
                    hbox:
                        $ section, people = line

                        text "[section!t]:":
                            if preferences.language == "japan":
                                font other_font_interface

                        null width 25

                        if section == "актеры озвучивания":
                            vbox:
                                spacing 5
                                for role in people:

                                    $ role_tl = __(role)

                                    text "{size=+10}" + role_tl.upper() xmaximum 1200:
                                        if preferences.language in ("japan", "chinese"):
                                            font other_font_interface

                        else:
                            $ prefix = "{size=+10}"
                            $ suffix = ", "
                            $ msg = prefix
                            for role in people:
                                $ role_tl = __(role)
                                $ msg += role_tl.upper() + suffix
                            $ msg = msg[:-2]

                            text msg xmaximum 1200:
                                if preferences.language in ("japan", "chinese"):
                                    font other_font_interface

    vbar:
        value YScrollValue("autor")
        xpos 1600
        yalign 0.5
        xsize 20
        ysize 900
        at for_yes_no_10
        keyboard_focus False

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            keysym "game_menu"
            at filepic_but3
            alt _("Назад")

screen file_slots(title):
    on "show" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")

    add "bg_menu_save_load" at conf_fon

    $ columns = 2
    $ rows = 2

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle Null(1920, 1080)
        hover "interface/save_load_menu/16.png"
        selected_idle "interface/save_load_menu/16.png"
        selected_hover "interface/save_load_menu/16.png"
        alpha False
        at for_show_save_load

        hotspot (310,126,415,107):
            action ShowMenu("save")
            sensitive is_save_allowed
            text _("Сохранить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "FFFFFF"
                if preferences.language == "japan":
                    font other_font_interface
                at filepic_elements
            at filepic_but4
            keyboard_focus False

        hotspot (310,126,415,107):
            action ShowMenu("save")
            sensitive is_save_allowed
            if renpy.get_screen("load"):
                hover_sound "sounds/menu/menu-button-select-1.ogg"
                activate_sound "sounds/menu/menu-button-click-1.ogg"
            text _("Сохранить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "000000"
                if preferences.language == "japan":
                    font other_font_interface
            at filepic_but4_2

        hotspot (965,126,415,107):
            action ShowMenu("load")
            text _("Загрузить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "FFFFFF"
                if preferences.language == "japan":
                    font other_font_interface
                at filepic_elements
            at filepic_but5
            keyboard_focus False

        hotspot (965,126,415,107):
            action ShowMenu("load")
            if renpy.get_screen("save"):
                hover_sound "sounds/menu/menu-button-select-1.ogg"
                activate_sound "sounds/menu/menu-button-click-1.ogg"
            text _("Загрузить"):
                xalign 0.4
                yalign 0.6
                style "text_font_interface"
                size 55
                color "000000"
                if preferences.language == "japan":
                    font other_font_interface
            at filepic_but5_2

    vbox:
        xpos 897
        ypos 821
        xminimum 100
        yminimum 100
        text FilePageName():
            xalign 0.5
            yalign 0.5
            size 55
            font "font/razor_k.ttf"
        at for_show_save_load

    imagemap:
        ground "interface/save_load_menu/01.png"
        insensitive "interface/save_load_menu/01.png"
        idle "interface/save_load_menu/14.png"
        hover "interface/save_load_menu/14.png"
        alpha True
        at for_show_save_load

        hotspot (1673,821,108,88):
            action Return()
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            at filepic_but3
            keysym "game_menu"
            alt _("Назад")

        hotspot (724,821,188,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            if int(FilePageName()) != 1:
                action FilePagePrevious()
            at filepic_but1

        hotspot (986,821,188,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action FilePageNext(999)
            at filepic_but2

        for i in range(1, columns * rows + 1):
            if i == 1:
                $ x = 356
                $ y = 275
            elif i == 2:
                $ x = 1034
                $ y = 275
            elif i == 3:
                $ x = 356
                $ y = 573
            elif i == 4:
                $ x = 1034
                $ y = 573

            $ file_name = FileSlotName(i, columns * rows)
            $ file_time = FileTime(i, empty=__("Слот пуст"))
            $ save_name = FileSaveName(i)
            $ nomber_of_del = i

            hotspot (x, y, config.thumbnail_width+6, config.thumbnail_height+6):
                action FileAction(i)
                add FileScreenshot(i):
                    xpos 3
                    ypos 2
                key "save_delete" action FileDelete(i)
                text "{alt}[file_time]\n[save_name]"

            vbox:
                xpos x + config.thumbnail_width + 15
                ypos y + 10
                xsize 140
                ysize 200
                text "[file_time!t]\n[save_name!t]" alt "":
                    style "text_font_interface"
                    size 30
                    xalign 0.5

                if file_time != _("Слот пуст"):
                    frame:
                        background Null()
                        yalign 1.0
                        textbutton _("УДАЛИТЬ") at filepic_but:
                            background Null()
                            hover_sound "sounds/menu/delete-1.ogg"
                            activate_sound "sounds/menu/menu-button-click-1.ogg"
                            text_style "text_font_interface"
                            text_size 40
                            text_color "FFFFFF"
                            action FileDelete(nomber_of_del, True)

    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")

screen preferences():
    tag menu
    modal True
    style_prefix "pref"

    on "show" action Play("test_five", "sounds/menu/menu-window-2.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-2.ogg")

    add "bg_menu_preferences" at conf_fon

    frame:
        background Null()
        style_group "pref"
        at for_yes_no_10

        vbox:
            ypos 150
            xpos 1000
            spacing 50

            hbox:
                xsize 600
                ysize 75

                text _("Громкость") alt "":
                    size 55

                hbox:
                    xalign 1.
                    spacing 50

                    text _("По умолчанию") yalign 1. alt ""

                    imagebutton:
                        idle "interface/preferences/button/00.png"
                        action (
                            SetMixer("music", 0.795),
                            SetMixer("sfx", 0.795),
                            SetMixer("voice", 1.0)
                        )
                        at transform:
                            zoom .75
                            on hover:
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
                                linear 0.01 xoffset 0 yoffset 0
                        alt _("Громкость по умолчанию")

            hbox:
                spacing 50
                xsize 600

                text _("Музыка") alt "":
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0

                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("music volume")

            hbox:
                spacing 50
                xsize 600

                text _("Звук") alt "":
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0

                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("sound volume")

            hbox:
                spacing 50
                xsize 600

                text _("Голос") alt "":
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0

                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("voice volume")

            null width 50

            text _("Скорость") alt "":
                size 55

            hbox:
                spacing 50
                xsize 600

                text _("Текст") alt "":
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0

                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("text speed")

            hbox:
                spacing 50
                xsize 600

                text _("Авточтение") alt "":
                    ypos 20

                frame:
                    background "interface/preferences/button/panel.png"
                    xalign 1.0

                    bar:
                        xpos 327
                        ypos 28
                        ysize 24
                        xsize 306
                        value Preference("auto-forward time")

        text _("Режим") alt "":
            xpos 400
            ypos 150
            size 55

        text _("Пропуск") alt "":
            xpos 400
            ypos 590
            size 55

    frame:
        background Null()
        style_prefix "main_menu"
        at for_yes_no_10

        vbox:
            xalign 0.2
            yalign 0.78

            textbutton _("Весь текст"):
                action Preference("skip", "all")
                keyboard_focus False
                xsize 350

            textbutton _("Прочитанный"):
                action Preference("skip", "seen")
                keyboard_focus False
                xsize 350

        vbox:
            xalign 0.2
            yalign 0.78

            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Весь текст")
                at mm_but
                xsize 350
                action Preference("skip", "all")

            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Прочитанный")
                at mm_but
                xsize 350
                action Preference("skip", "seen")

    frame:
        background Null()
        style_prefix "main_menu"
        at for_yes_no_10

        vbox:
            xalign 0.2
            yalign 0.3

            textbutton _("Оконный"):
                action Preference("display", "window")
                keyboard_focus False
                xsize 350

            textbutton _("Полноэкранный"):
                action Preference("display", "fullscreen")
                keyboard_focus False
                xsize 350

        vbox:
            xalign 0.2
            yalign 0.3

            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Оконный")
                at mm_but
                xsize 350
                action Preference("display", "window")

            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Полноэкранный")
                at mm_but
                xsize 350
                action Preference("display", "fullscreen")

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            keysym "game_menu"
            at filepic_but3
            alt _("Назад")

    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")

screen history():
    tag menu
    modal True

    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")

    predict False
    style_prefix "history"

    add "bg_menu_yes_no" at conf_fon

    text _("История"):
        xpos 800
        ypos 20
        size 60
        color "#FFFFFF"
        style "text_font_interface"
        at for_yes_no_10

    viewport at for_yes_no_10:
        xalign 0.1
        yalign 0.5
        xsize 1500
        ysize 780
        mousewheel True
        yinitial 1.0
        draggable True
        pagekeys True
        has vbox
        for h in _history_list:
            window:
                has fixed
                yfit True

                vbox:
                    if h.who:
                        label "{noalt}[h.who]":
                            style "history_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    textbutton what action RollbackToIdentifier(h.rollback_identifier):
                        style "history_text"
                        text_size 40
                        text_color "#bbb"
                        text_hover_color "#fff"
                        if h.who:
                            alt f"{renpy.filter_text_tags(h.who, ())}: {what}"

            null height 5

        if not _history_list:
            label _("История диалогов пуста.")

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            keysym "game_menu"
            at filepic_but3
            alt _("Назад")

init python:
    def add_text_to_dictionary(num):
        global dictionary_list, rus_dictionary, new_words

        if (rus_term := rus_dictionary[num]) not in dictionary_list:
            if _preferences.language is None:
                if rus_term not in nonrus_dict:
                    renpy.alt(_("Новая запись"))

            else:
                renpy.alt(_("Новая запись"))

            if rus_term not in nonrus_dict or _preferences.language in nonrus_dict[rus_term]:
                new_words = False

            dictionary_list.append(rus_term)
            
            if rus_term not in nonrus_dict or _preferences.language in nonrus_dict[rus_term]:
                renpy.show_screen('dict_timer')
                new_words = True

screen dictionary_scr():
    tag menu
    modal True

    on "show" action SetVariable("new_words", False), Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")

    predict False
    style_prefix "history"

    add "bg_menu_yes_no" at conf_fon

    text _("Словарь"):
        xpos 800
        ypos 20
        size 60
        color "#FFFFFF"
        style "text_font_interface"
        at for_yes_no_10

    viewport at for_yes_no_10:
        xalign 0.1
        yalign 0.5
        xsize 1500
        ysize 780
        mousewheel True
        yinitial 1.0
        draggable True
        pagekeys True
        has vbox
        for what in dictionary_list:
            if what not in nonrus_dict or _preferences.language in nonrus_dict[what]:
                vbox:
                    button:
                        action NullAction()
                        text what style "text_dict"
                        background None

                null height 30

        if not dictionary_list:
            text _("Словарь пуст.") style "text_dict"

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            keysym "game_menu"
            at filepic_but3
            alt _("Назад")

screen big_bro_see_you():
    vbox:
        xpos 1770
        ypos 20
        at for_look_buttons_0
        button:
            xsize 127
            ysize 69
            background "interface/05.png"
            hover_sound "sounds/menu/menu-button-select-new-3_3.ogg"
            activate_sound "sounds/menu/menu-button-push-1_1.ogg"
            add "interface/EYE.png":
                xalign 0.4
                yalign 0.5
            if eyes_visible == False:
                action [SetVariable('eyes_visible', True), Show('hide_eyes')]
                at for_look_buttons_1
            else:
                at for_look_buttons_2
            keyboard_focus False

screen initial_language_select():
    add "images/interface/Lang.jpg"

    vbox:
        xalign .5
        yalign .58
        spacing 1

        hbox:
            xalign .5
            spacing 100

            button:
                xminimum 103
                yminimum 192
                background "interface/main_meny/lapka_01.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_rus")
                sensitive True
                selected False
                action Return(), Language(None)
                text "РУС":
                    xalign .5
                    ypos 79
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Русский"
                at mm_but_lang

            button:
                xminimum 103
                yminimum 192
                background "interface/main_meny/lapka_02.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_eng")
                sensitive True
                selected False
                action Return(), Language("english")
                text "ENG":
                    xalign .5
                    ypos 79
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "English"
                at mm_but_lang

            button:
                xsize 103
                ysize 192
                background "interface/main_meny/lapka_04.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_chi")
                sensitive True
                selected False
                action Return(), Language("chinese")
                text "{alt}中文"
                at mm_but_lang

            button:
                xminimum 103
                yminimum 192
                background "interface/main_meny/lapka_02.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_ita")
                sensitive True
                selected False
                action Return(), Language("italiano")
                text "ITA":
                    xalign .5
                    ypos 79
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Italiano"
                at mm_but_lang

            button:
                xminimum 103
                yminimum 192
                background "interface/main_meny/lapka_01.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_tur")
                sensitive True
                selected False
                action Return(), Language("turkish")
                text "TÜR":
                    xalign .5
                    ypos 79
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "Türkçe"
                at mm_but_lang

            button:
                xminimum 103
                yminimum 192
                background "interface/main_meny/lapka_01.png"
                hover_sound "sounds/menu/menu-button-select-3.ogg"
                activate_sound "sounds/menu/language-sellect-1.ogg"
                hovered ShowTransient("initial_language_message_jpn")
                sensitive True
                selected False
                action Return(), Language("japan")
                text "JAP":
                    xalign .5
                    ypos 79
                    font "font/razor_k.ttf"
                    color "000000"
                    size 40
                    alt "日本語"
                at mm_but_lang

# episode 1
screen room_night_1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        hover "locate/home/in_side/2st_floor/anton_room/room_night_but1.png"
        alpha False

        hotspot (1450,0,470,1080):
            hover_sound "sounds/curtain-3.ogg"
            action Return()
            alt _("ОТКРЫТЬ")

    vbox:
        xpos 1600
        ypos 350
        xsize 245
        ysize 100
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

screen hall_day_1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (550,400,150,150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_hall_ula')
            hover_sound "sounds/Yla.ogg"
            alt _("Юла")

        hotspot (1250,105,80,130):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_hall_cross')
            hover_sound "sounds/cross-3.ogg"
            alt _("Крест")

        hotspot (1480,525,125,95):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_hall_telephone')
            hover_sound "sounds/phone-pickup-1.ogg"
            alt _("Телефон")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/hall/hall_but_idle.png"
        hover "locate/home/in_side/1st_floor/hall/hall_but_hover.png"
        alpha True

        hotspot (700,80,270,735):
            hover_sound "sounds/menu/button-click-4.ogg"
            action Jump('bunny_day1_kitchen')
            alt _("НА КУХНЮ")

        hotspot (1115,205,365,735):
            hover_sound "sounds/menu/button-click-4.ogg"
            if not SceneFlags.Has("mom talked"):
                action Return()
            else:
                action Jump('bunny_day1_open_door')
            alt _("ВО ДВОР")

        hotspot (0,170,455,910):
            hover_sound "sounds/kladovka.ogg"
            action Jump('bunny_pantry_day1')
            alt _("Кладовка")

    vbox:
        xpos 1200
        ypos 500
        xsize 200
        ysize 50
        text _("ВО ДВОР") alt "":
            style "imagemap_text"
            text_align 0.5

    vbox:
        xpos 730
        ypos 350
        xsize 200
        ysize 50
        text _("НА КУХНЮ") alt "":
            style "imagemap_text"

    vbox:
        xpos 100
        ypos 700
        xsize 200
        ysize 50
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

    use big_bro_see_you

screen kitchen_day_1():
    layer "master"

    default mom_hover = False

    if not SceneFlags.Has("mom talked"):
        if mom_hover:
            add "Mom Normal m_day 08 norm2 ahead" at mom_left
        else:
            add "Mom Normal m_day 01 norm aside" at mom_left

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (73,224,96,137):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_kitchen_kalendar')
            hover_sound "sounds/ka-fix-1.ogg"
            alt _("Календарь")

        hotspot (131,716,224,212):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_kitchen_radio')
            hover_sound "sounds/radio-short-1.ogg"
            alt __('Радио')

        hotspot (1057,895,306,126):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_kitchen_gazeta')
            hover_sound "sounds/gaz1-fix-1.ogg"
            alt _("Газета")

        if not SceneFlags.Has("mom talked"):
            hotspot (450,40,465,1040):
                hovered SetScreenVariable("mom_hover", True)
                unhovered SetScreenVariable("mom_hover", False)
                hover_sound "voice/karina/00 K.ogg"
                action Jump('bunny_talk_m_in_kitchen1')
                alt _("ОБМАНУТЬ")

        if not Flags.Has("number"):
            hotspot (1175,80,305,400):
                if eyes_visible == True:
                    add "interface/eye.png" at for_look_buttons
                else:
                    add "interface/eye.png" at for_hide_buttons
                action Jump('bunny_come_fridge')
                hover_sound "sounds/refrigerator-short-1.ogg"
                alt _("Боковина холодильника")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/kitchen/kitchen1_but0.png"
        hover "locate/home/in_side/1st_floor/kitchen/kitchen1_but1.png"
        alpha True

        hotspot (1700,0,220,1080):
            hover_sound "sounds/menu/button-click-4.ogg"
            action Jump('bunny_hall_day1_transition')
            alt _("ОБРАТНО")

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/kitchen/kitchen1_but3.png"
        hover im.MatrixColor("locate/home/in_side/1st_floor/kitchen/kitchen1_but3.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (1490,55,190,1025):
            hover_sound "sounds/menu/button-click-4.ogg"
            action [Play("test_five", "sounds/fridge-open-2.ogg"), Jump('bunny_in_fridge_transition')]
            alt _("Холодильник")

    if not SceneFlags.Has("mom talked"):
        vbox:
            xpos 600
            ypos 620
            text _("ОБМАНУТЬ") alt "":
                style "imagemap_text"

    vbox:
        xpos 1760
        ypos 570
        text _("ОБРАТНО") alt "":
            style "imagemap_text"

    vbox:
        xpos 1520
        ypos 320
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

    use big_bro_see_you

screen in_fridge_screen1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/kitchen/cold/door_01.png"
        hover im.MatrixColor("locate/home/in_side/1st_floor/kitchen/cold/door_01.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (165,120,1095,405):
            hover_sound "sounds/menu/button-click-4.ogg"
            action [Play("test_five", "sounds/freezer-open-1.ogg"), Jump('bunny_in_fridge2')]
            alt _("ОТКРЫТЬ")

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_1_but.png"
        hover im.MatrixColor("locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_1_but.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (1700,0,220,1080):
            hover_sound "sounds/menu/button-click-4.ogg"
            action [Play("test_five", "sounds/fridge-close-2.ogg"), Jump('bunny_day1_kitchen')]
            alt _("ОБРАТНО")

    vbox:
        xpos 600
        ypos 300
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

    vbox:
        xpos 1760
        ypos 570
        text _("ОБРАТНО") alt "":
            style "imagemap_text"

screen take_list1():
    layer "master"

    imagebutton idle "locate/home/in_side/1st_floor/kitchen/List002.png":
        action [Play("test_six","sounds/paper-take-4.ogg"), Return()]
        alt _("ВЗЯТЬ")

screen forest1_screen():
    layer "master"

    imagebutton idle "locate/home/out_side/h006.png" hover "locate/home/out_side/h006_1.png":
        focus_mask True
        hover_sound "sounds/menu/button-click-4.ogg"
        action Jump('run_anton')
        alt _("УБЕЖАТЬ")

    imagebutton idle "locate/home/out_side/varezka_but0.png" hover "locate/home/out_side/varezka_but1.png":
        focus_mask True
        hover_sound "sounds/menu/button-click-4.ogg"
        action Jump('take_anton')
        alt _("ВЗЯТЬ")

    vbox:
        xpos 1130
        ypos 620
        xsize 200
        ysize 50
        text _("ВЗЯТЬ") alt "":
            style "imagemap_text"

    vbox:
        xpos 950
        ypos 420
        xsize 200
        ysize 50
        text _("УБЕЖАТЬ") alt "":
            style "imagemap_text"

screen anton_room_day_1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (1485,0,435,870):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_anton_room_circle')
            hover_sound "sounds/curtain-3.ogg"
            alt _("Штора")

        hotspot (895,85,260,130):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_anton_room_toys')
            hover_sound "sounds/toy-short.ogg"
            alt _("Игрушки")

        hotspot (1020,382,255,243):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_anton_room_picture')
            hover_sound "sounds/wall-pics-short-1.ogg"
            alt _("Рисунки")

        hotspot (295,863,255,130):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_anton_room_book')
            hover_sound "sounds/book-short-2.ogg"
            alt _("Книга")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/2st_floor/anton_room/room_day/room_day_c_button1.png"
        hover im.MatrixColor("locate/home/in_side/2st_floor/anton_room/room_day/room_day_c_button1.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (935,685,225,65):
            hover_sound "sounds/desk-short-1.ogg"
            action [Jump('anton_room_continue1')]
            alt _("ОТКРЫТЬ")

    vbox:
        xpos 980
        ypos 685
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

    use big_bro_see_you

screen olya_room_day_1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (968,382,128,115):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_olya_room_circle')
            hover_sound "sounds/curtain-3.ogg"
            alt _("Штора")

        hotspot (1280,555,115,210):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_olya_room_bear')
            hover_sound "sounds/teddybear-short-1.ogg"
            alt _("Мишка")

        hotspot (1630,160,113,85):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_olya_room_pig')
            hover_sound "sounds/coins-select-01.ogg"
            alt _("Копилка")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/2st_floor/olga_room/photon_but1.png"
        hover im.MatrixColor("locate/home/in_side/2st_floor/olga_room/photon_but1.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (465,460,285,240):
            hover_sound "sounds/tv-static-1.ogg"
            action [Jump('bunny_day1_olya_room_photon')]
            alt _("ВКЛЮЧИТЬ")

    vbox:
        xpos 535
        ypos 570
        xsize 180
        text _("ВКЛЮЧИТЬ") alt "":
            style "imagemap_text"

    use big_bro_see_you

screen olya_room_day_1_close_circle():
    layer "master"

    imagemap:
        ground "bg_Olga_room_n_1_back"
        idle "locate/home/in_side/2st_floor/olga_room/Olga_room_n_001.png"
        hover im.MatrixColor("locate/home/in_side/2st_floor/olga_room/Olga_room_n_001.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (620,100,820,755):
            hover_sound "sounds/curtain-3.ogg"
            action [Return()]
            alt _("ЗАКРЫТЬ")

    add "Olga_room_Light"

    vbox:
        xpos 620
        ypos 100
        xsize 820
        ysize 755
        text _("ЗАКРЫТЬ") alt "":
            style "imagemap_text"

# episode 2
screen day2_choice_candy_or_refuse():
    layer "master"

    default candy_take_hover = False
    default candy_refuse_hover = False

    if not (candy_take_hover or candy_refuse_hover):
        add "Fox_give_candy_01"
        add "Fox_give_candy_gum"
    elif candy_take_hover:
        add "Fox_give_candy_05":
            at transform:
                matrixcolor BrightnessMatrix(0.1)
        add "Fox_give_candy_gum"
    elif candy_refuse_hover:
        add "Fox_give_candy_04"

    button:
        xpos 1150
        ypos 550
        xsize 350
        ysize 400
        hover_sound "sounds/menu/button-click-4.ogg"
        action Jump('bunny2_take1')
        hovered SetScreenVariable("candy_take_hover", True)
        unhovered SetScreenVariable("candy_take_hover", False)
        text _("ВЗЯТЬ"):
            style "imagemap_text"
            at conf_fon
            yalign .0
            xalign .25

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 1250
            ypos 120
            anchor (.5, .5)
            hover_sound "sounds/menu/button-click-4.ogg"
            action Jump('bunny2_cancel1')
            hovered SetScreenVariable("candy_refuse_hover", True)
            unhovered SetScreenVariable("candy_refuse_hover", False)
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ОТКАЗАТЬСЯ")

        text _("ОТКАЗАТЬСЯ") alt "":
            xpos 1250
            ypos 120
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen school_night_1():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (950,665,130,130):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_school_night_gopniks')
            hover_sound "sounds/sfx_boys_laugh.ogg"
            alt _("Старшеклассники")

        if not Flags.Has("witness school"):
            hotspot (575,615,120,415):
                if eyes_visible == True:
                    add "interface/eye.png" at for_look_buttons offset (0, -100)
                else:
                    add "interface/eye.png" at for_hide_buttons offset (0, -100)
                action Jump('bunny_school_night_witness')
                hover_sound "sounds/sfx_man_cough.ogg"
                alt _("Мужчина")

        hotspot (315,258,127,106):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('bunny_school_night_nest')
            hover_sound "sounds/sfx_nest_creaking.ogg"
            alt _("Гнездо")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/school/out_side/school02.png"
        hover "locate/school/out_side/school02.png"
        alpha True

        hotspot (1215,530,700,555):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (100, 50)
            else:
                add "interface/eye.png" at for_hide_buttons offset (100, 50)
            hover_sound "sounds/sfx_volga.ogg"
            action [Jump('bunny_school_night_dog')]
            alt _("Автомобиль")

        at for_look_buttons_3

    imagemap:
        ground Null(1920,1080)
        idle "locate/school/out_side/door1.png"
        hover im.MatrixColor("locate/school/out_side/door1.png",
            im.matrix.brightness(0.10))
        alpha True

        hotspot (1145,625,170,125):
            hover_sound "sounds/sfx_school_door.ogg"
            action [Jump('bunny_school_inside1')]
            alt _("ВОЙТИ")

        at for_look_buttons_3

    vbox:
        xpos 1174
        ypos 660
        text _("ВОЙТИ") alt "":
            style "imagemap_text"

    use big_bro_see_you

screen read_attention():
    layer "master"

    fixed:
        imagebutton:
            idle "locate/school/in_side/raspisanie_but.png"
            hover im.MatrixColor("locate/school/in_side/raspisanie_but.png",
                im.matrix.brightness(0.20))
            focus_mask True
            action Return()
            at transform:
                zoom 0.83
                xalign 0.32
                yalign 0.5
            alt _("ПРОЧИТАТЬ")

        text _("ПРОЧИТАТЬ") alt "":
            xpos 600
            ypos 350
            anchor (.5,.5)
            style "imagemap_text"
            at transform:
                zoom 1.3

screen day2_choice_polina_or_fox():
    layer "master"

    button:
        pos (1579-400, 842)
        xysize (1704-1579, 934-842)
        hover_sound "sounds/Sumka_1.ogg"
        action Jump('shoes_see')
        if eyes_visible == True:
            add "interface/eye.png" at for_look_buttons
        else:
            add "interface/eye.png" at for_hide_buttons
        at for_look_buttons_3
        alt _("Обувь")

    button:
        pos (656-400, 534)
        xysize (779-656, 945-534)
        hover_sound "sounds/vedro_1.ogg"
        action Jump('bucket_see')
        if eyes_visible == True:
            add "interface/eye.png" at for_look_buttons
        else:
            add "interface/eye.png" at for_hide_buttons
        at for_look_buttons_3
        alt _("Ведёрко")

    button:
        pos (1308-400, 853)
        xysize (1384-1308, 902-853)
        hover_sound "sounds/samolet_1.ogg"
        action Jump('airplane_see')
        if eyes_visible == True:
            add "interface/eye.png" at for_look_buttons
        else:
            add "interface/eye.png" at for_hide_buttons
        at for_look_buttons_3
        alt _("Самолётик")

    button:
        pos (997-400, 410)
        xysize (464, 370)
        idle_background None
        hover_background 'locate/school/in_side/school_hall/new/003.png'
        hover_sound "sounds/menu/button-click-4.ogg"
        action Jump('bunny2_polina_win')
        text __("ПОЛИНА"):
            style "imagemap_text"
            xpos 300
            xanchor .5
            ypos 100
        at conf_fon_slow

    button:
        pos (1713-400, 332)
        xysize (134, 580)
        idle_background None
        hover_background 'locate/school/in_side/school_hall/new/004.png'
        hover_sound "sounds/menu/button-click-4.ogg"
        action Jump('bunny2_fox_win')
        at conf_fon_slow
        alt __("АЛИСА")

    vbox:
        xpos 1320
        ypos 390
        text __("АЛИСА") alt "":
            style "imagemap_text"
        at conf_fon_slow

    use big_bro_see_you

screen school2_near():
    layer "master"

    on "show":
        action SetVariable("eyes_visible", False)

    add "bg school_corner_day":
        xpos 0
    add "school_coner_01":
        xpos 0

    if Flags.Has("myth2"):
        add "day2_myth":
            xpos 0

    if not SceneFlags.Has("hangman"):
        imagemap:
            ground Null(1920,1080)
            idle Null(1920,1080)
            alpha False

            hotspot (1231,483,236,205):
                if eyes_visible == True:
                    add "interface/eye.png" at for_look_buttons
                else:
                    add "interface/eye.png" at for_hide_buttons
                action Jump('bunny2_school_near4')
                hover_sound "sounds/sfx_chalk_1.ogg"
                alt _("Повешенный")

            hotspot (1300,780,236,205):
                if eyes_visible == True:
                    add "interface/eye.png" at for_look_buttons
                else:
                    add "interface/eye.png" at for_hide_buttons
                action Jump('bunny2_school_near5')
                hover_sound "sounds/sfx_syringe.ogg"
                alt _("Шприц")

            hotspot (630,45,236,205):
                if eyes_visible == True:
                    add "interface/eye.png" at for_look_buttons
                else:
                    add "interface/eye.png" at for_hide_buttons
                action Jump('bunny2_school_near6')
                hover_sound "sounds/sfx_squirrel_chirp.ogg"
                alt _("Белка")

            at for_look_buttons_3

    if not SceneFlags.Has("witness2 school"):
        imagebutton:
            idle "locate/school/out_side/school_coner/school_coner_02.png"
            focus_mask True
            hover_sound "sounds/sfx_man_cough.ogg"
            action [Jump('bunny2_school_near2')]
            alt _("Мужчина")

        frame:
            xysize (1920,1080)
            background Null()
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons pos (940, 580)
            else:
                add "interface/eye.png" at for_hide_buttons pos (940, 580)
            at for_look_buttons_3

    if SceneFlags.Has("hangman"):
        imagebutton:
            idle "locate/school/out_side/school_coner/school_coner_01.png"
            hover im.MatrixColor("locate/school/out_side/school_coner/school_coner_01.png",
                im.matrix.brightness(0.10))
            focus_mask True
            hover_sound "sounds/touch_snow_5-1.ogg"
            activate_sound "sounds/tolchki_1.ogg"
            action [Jump('bunny2_school_near1')]
            alt _("ПРОВЕРИТЬ")

    if SceneFlags.Has("hangman"):
        vbox:
            xpos 440
            ypos 765
            text _("ПРОВЕРИТЬ") alt "":
                style "imagemap_text"

    if not SceneFlags.Has("hangman"):
        use big_bro_see_you

screen witness_walkaway(spr, blur, timeout):
    layer "master"

    default ms = __("Изучите сцену")

    text "{alt}[ms]"

    imagebutton:
        if blur:
            idle im.Blur(spr, blur)
            hover im.Blur(im.MatrixColor(spr,
                im.matrix.brightness(0.10)), blur)
        else:
            idle spr
            hover im.MatrixColor(spr,
                im.matrix.brightness(0.10))
        focus_mask True
        action Function(SceneFlags.Raise, "witness tapped"), Return("tap")
        at transform:
            zoom 0.80
            ypos 200
            xpos -203
            linear delay3 xpos 1920-203
            linear delay3 xpos 2*1920-203
        alt _("Мужчина")

    timer (delay2*timeout) action Hide("witness_walkaway"), Return()
    timer 18 action Hide("witness_walkaway"), Return()

screen day2_garage_open():
    layer "master"

    fixed:
        imagebutton:
            idle "locate/street/garage/The_garage_but.png"
            focus_mask True
            action Return()
            at transform:
                on hover:
                    alpha .5
                on idle:
                    alpha .0
            alt _("ПОСТУЧАТЬ")

        text _("ПОСТУЧАТЬ") alt "":
            xpos 917
            ypos 662
            anchor (.5,.5)
            style "imagemap_text"

screen day2_nightmare_open():
    layer "master"

    fixed:
        imagebutton:
            idle "locate/home/in_side/2st_floor/anton_room/room_day/room_day_but.png"
            focus_mask True
            action Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .0
            alt _("ОТКРЫТЬ")

        text _("ОТКРЫТЬ") alt "":
            xpos 635
            ypos 492
            anchor (.5,.5)
            style "imagemap_text"

screen day2_album_paint():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 1200
            ypos 580
            anchor (.5,.5)
            hover_sound "sounds/menu/button-click-4.ogg"
            action Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("РИСОВАТЬ")

        text _("РИСОВАТЬ") alt "":
            xpos 1200
            ypos 580
            anchor (.5,.5)
            style "imagemap_text"
            color "#000000"
            outlines [ (absolute(1), "#FFFFFF", absolute(0), absolute(0)) ]

# episode 3
screen day3_observe():
    layer "master"

    default sit_hover = False

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (320-75, 300-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d3_look_projector')
            hover_sound day3_observe_sfx_projector
            alt _("Проектор")

        hotspot (1260-75, 220-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d3_look_esenin')
            hover_sound day3_observe_sfx_esenin
            alt _("Портреты")

        hotspot (1430-75, 780-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d3_look_box')
            hover_sound day3_observe_sfx_box
            alt _("Петарды")

        at for_look_buttons_3

    if sit_hover:
        add "empty_desk_sem":
            xpos -3911 + 1920 + 300
        add "classroom_chair":
            xpos -3911 + 1920 + 300 - 20
            ypos 20

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 920
            ypos 920
            anchor (.5,.5)
            hover_sound day3_observe_sfx_sit_hover
            hovered SetScreenVariable("sit_hover", True)
            unhovered SetScreenVariable("sit_hover", False)
            action Play("test_two", day3_observe_sfx_sit_action), Jump('day_3_continue')
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("СЕСТЬ")

        text _("СЕСТЬ") alt "":
            xpos 920
            ypos 920
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

    use big_bro_see_you

screen minigame_case():
    layer "master"

    add "case_bg"
    add "chalk_writings"
    add "guard":
        id "guard"
        if phase == 1:
            at phase1
        if phase == 2:
            at phase2
        if phase == 3:
            at phase3
    add "teah_win" xpos -1688
    add "case_fg"

    imagebutton:
        idle "case_folder_idle"
        hover "case_folder_hover"
        selected False
        focus_mask True
        if case_sfx_folder:
            hover_sound case_sfx_folder
        if guard_state == 0:
            action Return("hit")
        else:
            action Return("fail")
        alt _("ОТКРЫТЬ")

    text _("ОТКРЫТЬ") alt "":
        xpos 940
        ypos 936
        anchor (.5,.5)
        style "imagemap_text"

    textbutton _("ПРОПУСТИТЬ"):
        xpos 1022
        ypos 118
        anchor (.5,.5)
        if case_sfx_clock_hover:
            hover_sound case_sfx_clock_hover
        hovered SetVariable("case_mng_hightlight_clock", True)
        unhovered SetVariable("case_mng_hightlight_clock", False)
        action Play("test_six", case_sfx_clock_action), Return("full_timeout")
        text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        style "imagemap_text"

    use clock_timer(phase)

    if phase == 1:
        timer 21.0 action Return("timeout")

    if phase == 2:
        timer 11.0 action Return("timeout")

    if phase == 3:
        timer 11.0 action Return("timeout")

screen photorobot_b5():
    vbox:
        xpos 780
        ypos -40

        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            action [Hide('photorobot_b5'), Return()]
            if photorobot_sfx_finish:
                hover_sound photorobot_sfx_finish
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .0
            alt _("ОТДАТЬ")

    vbox:
        xalign 0.5
        ypos 54
        xsize 250
        ysize 50
        text _("ОТДАТЬ") alt "":
            size 50
            style "imagemap_text"
            color "#000000"
            outlines [ (absolute(1), "#FFFFFF", absolute(0), absolute(0)) ]

init python:
    def start_photorobot_game():
        lst = [
            (_("Лиса"), (6, 2, 4, 3)),
            (_("Летов"), (4, 1, 3, 6)),
            (_("Цой"), (5, 3, 1, 4)),
            (_("Бодров"), (1, 6, 6, 2)),
            (_("Трудовик"), (1, 1, 1, 1))
        ]

        if is_tapped == "tap" or Flags.Has("witness tapped"):
            lst.insert(0, (_("Подозреваемый"), (3, 4, 2, 5)))

        renpy.show_screen('photorobot')
        rv = renpy.display_menu(lst)

        for i, n in enumerate(rv):
            setattr(store, f'face{i + 1}', photorobot_face[i][n])

        renpy.sound.queue([renpy.random.choice(photorobot_sfx_arrow_list) for _ in range(4)])
        renpy.call_screen('photorobot_b5')


screen start_suefa(first_time=False):
    layer "master"

    add "interface/suefa/01.png":
        if first_time:
            at for_frame_suefa_1
        else:
            at for_frame_suefa_2
    add f"interface/suefa/R_0{suefa_r}.png":
        if first_time:
            at for_left_hand_suefa_1
        else:
            at for_left_hand_suefa_2
    add f"interface/suefa/A_0{suefa_a}.png":
        if first_time:
            at for_right_hand_suefa_1
        else:
            at for_right_hand_suefa_2

    default gestures = _("Ножницы"), _("Бумага"), _("Камень")

    for i in range(3):
        imagebutton:
            idle f"interface/suefa/{i + 1}.png"
            focus_mask True
            if first_time:
                at for_button_suefa_1
            else:
                at for_button_suefa_2
            action Function(choice_suefa, i + 1), Hide("start_suefa"), Show("end_suefa")
            if suefa_sfx_hover:
                hover_sound suefa_sfx_hover
            alt gestures[i]

    timer 0.01 action Hide("end_suefa", transition = dissolve)

screen day3_open_box():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 854
            ypos 722
            anchor (.5,.5)
            hover_sound day3_open_box_sfx_open
            action Jump('open_box_table')
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ОТКРЫТЬ")

        text _("ОТКРЫТЬ") alt "":
            xpos 854
            ypos 722
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen day3_dendy_btn():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 1000
            ypos 450
            anchor (.5,.5)
            hover_sound day3_dendy_btn_sfx_play
            action Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ИГРАТЬ")

        text _("ИГРАТЬ") alt "":
            xpos 1000
            ypos 450
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen goosehunt_ui(game):
    layer "master"
    zorder 2

    frame:
        xpos 90 + goosegame_xoffset
        ypos 750 + goosegame_yoffset
        xsize 270
        ysize 60
        background Frame("images/goosehunt/frame1.png", 20, 20)
        has hbox
        align 0.5, 0.5
        spacing 10
        text "SHOT:" alt "":
            xalign 0.0
            yalign 0.5
            size 30
            font "font/Retro Gaming.ttf"
        hbox:
            xalign 1.0
            yalign 0.5
            for i in range(3):
                if i < game.ammo:
                    add "goosehunt/01.png"
                else:
                    add Null(40,40)

    frame:
        xpos 620 + goosegame_xoffset
        ypos 750 + goosegame_yoffset
        xsize 450
        ysize 60
        background Frame("images/goosehunt/frame1.png", 20, 20)
        has hbox
        align 0.5, 0.5
        spacing 10
        text "HIT:" alt "":
            xalign 0.0
            yalign 0.5
            size 30
            font "font/Retro Gaming.ttf"

        hbox:
            xalign 1.0
            yalign 0.5
            for i in range(8):
                if i < len(game.goose_statuses):
                    $ status = game.goose_statuses[i]
                    if status is None:
                        add "goosehunt/03.png":
                            at transform:
                                alpha 1
                                .5
                                alpha 0
                                .5
                                repeat
                    elif status is True:
                        add "goosehunt/02.png"
                    else:
                        null width 40 height 40
                else:
                    add "goosehunt/03.png"

    $ points = game.points[game.player - 1]
    text f"{points:07}":
        xpos 1070 + goosegame_xoffset
        xalign 1.
        ypos 730 + goosegame_yoffset
        yalign 1.
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
        alt f"hit {points}"

screen goosehunt_hunting(game):
    layer "master"
    zorder 1
    add "goosehunt_bg"

    button:
        if goose_cursor == "goosehunt_cursor 0":
            xsize 1920
            ysize 1080
        else:
            xpos goosegame_xoffset
            ypos goosegame_yoffset
            xsize 1130
            ysize 960
        background Null()
        if game.ammo>0:
            action SetField(game, "ammo", game.ammo-1), Show("flash"), Play("sound", "audio/huntgoose/shot.ogg")
        elif goose_cursor == "goosehunt_cursor 0":
            action NullAction()
        mouse goose_cursor
        keyboard_focus False

    for i, goose in enumerate(game.active_gooses, 1):
        button:
            id goose
            xsize goosegame_goosesize
            ysize goosegame_goosesize
            xpos goose.x + goosegame_xoffset
            ypos goose.y + goosegame_yoffset
            xanchor .5
            yanchor .5
            background goose.img
            sensitive game.ammo > 0 and goose.state in (GOOSE_ACTIVE, GOOSE_FLYING_AWAY)
            action [
                Function(goose.strike),
                SetField(game, "ammo", game.ammo - 1),
                Show("flash"),
                Play("sound", "audio/huntgoose/shot.ogg"),
                Show(f"points_reward_goose{i}", pos=(goose.x + goosegame_xoffset, goose.y + goosegame_yoffset - 100)),
                Function(game.AddPoints)
            ]
            mouse goose_cursor
            at transform:
                linear spf xoffset goose.dx yoffset goose.dy
            alt f"goose {i}"

    add "goosehunt_fg"

    timer spf:
        action Function(game.Update)
        repeat True

screen day3_choice_polina_call():
    layer "master"

    default polcall_betray_hover = False
    default polcall_friend_hover = False

    imagebutton:
        focus_mask True
        idle "polina_call_friend_idle"
        hover "polina_call_friend_hover"
        action Jump('bunny3_betray_false')
        hover_sound day3_choice_polina_call_sfx_romka
        alt _("РОМКА")

    text _("РОМКА") alt "":
        xpos 800+150
        ypos 125+100
        anchor (.5,.5)
        style "imagemap_text"
        color "#000000"
        outlines [ (absolute(1), "#ffffff", absolute(0), absolute(0)) ]
        at conf_fon

    imagebutton:
        focus_mask True
        idle "polina_call_betray_idle"
        hover "polina_call_betray_hover"
        action Jump('bunny3_betray_true')
        hover_sound day3_choice_polina_call_sfx_polina
        alt __("ПОЛИНА")

    text _("ПОЛИНА") alt "":
        xpos 140 + 150
        ypos 125 + 100
        anchor (.5,.5)
        style "imagemap_text"
        color "#000000"
        outlines [ (absolute(1), "#ffffff", absolute(0), absolute(0)) ]

screen day3_door_peephole():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos .5
            ypos .5
            anchor (.5,.5)
            hover_sound day3_door_peephole_sfx_look_hover
            action Play("test_two", day3_door_peephole_sfx_look_action), Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ПОСМОТРЕТЬ")

        text _("ПОСМОТРЕТЬ") alt "":
            xpos .5
            ypos .5
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

# episode 4
screen day4_garage_lighton():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 1000
            ypos 200
            anchor (.5,.5)
            hover_sound day4_garage_sfx_lighton
            action Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ВКЛЮЧИТЬ")

        text _("ВКЛЮЧИТЬ") alt "":
            xpos 1000
            ypos 200
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen day4_garagein_observe():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (200-75, 500-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.junk')
            hover_sound day4_observe_garage_junk
            alt _("Хлам")

        hotspot (919-75, 619-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.car')
            hover_sound day4_observe_garage_car
            alt _("Автомобиль")

        hotspot (1000-75, 300-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.tools')
            hover_sound day4_observe_garage_tools
            alt _("Инструменты")

        hotspot (1500-75, 100-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.shelf')
            hover_sound day4_observe_garage_shelf
            alt _("Полка")

        hotspot (1839-75, 539-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.tiski')
            hover_sound day4_observe_garage_tiski
            alt _("Тиски")

        hotspot (200-75, 811-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons
            else:
                add "interface/eye.png" at for_hide_buttons
            action Jump('d4_garage_lookaround.boxes')
            hover_sound day4_observe_garage_boxes
            alt _("Ящики")

        at for_look_buttons_3

    default roma_hover = False

    if len(SceneFlags.vault) >= 2:
        fixed:
            if roma_hover:
                add "d4_garage_romka 1":
                    align (1., 1.)
                    matrixcolor BrightnessMatrix(0.1)

            button:
                xpos 1230
                ypos 300
                anchor (.5, .5)
                xysize (300, 350)
                action Jump('d4_garage_followup')
                hovered SetScreenVariable("roma_hover", True)
                unhovered SetScreenVariable("roma_hover", False)
                hover_sound day4_observe_garage_roma
                text _("ПОГОВОРИТЬ"):
                    anchor (.5,.5)
                    style "imagemap_text"
                    color "#ffffff"
                    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                    at conf_fon

    use big_bro_see_you

init python:
    class puzKatya(puzKatya):
        def update(self, dt, is_boosted=None):
            if (lbl := super().update(dt, is_boosted)) is not None:
                renpy.alt(_("Этап пройден"))

            return lbl

screen d4_make_photo(photo):
    use d4_polaroid(photo)

    button:
        xfill True
        yfill True
        action Jump(photo.data.next_label)
        alt _("СДЕЛАТЬ ФОТО")

    if not photo.interactive:
        text polaroid_text_ready_to_action_btn alt "":
            align (.5, .23)
            xoffset 10

screen day4_police_observe():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (1635, 535, 75, 75):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('d4_police_lookaround.cage')
            hover_sound day4_observe_police_cage
            alt _("Камера")

        hotspot (1220, 575, 75, 75):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 20)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 20)
            action Jump('d4_police_lookaround.mask')
            hover_sound day4_observe_police_mask
            alt _("Противогаз")

    button:
        xpos -75
        ypos 250
        xsize 360
        ysize 284
        text _("ОСМОТРЕТЬ"):
            xalign .5
            yalign .5
            style "imagemap_text"
        focus_mask True
        idle_background None
        background None
        hover_background "interface/intercative_button.png"
        hover_sound day4_observe_police_notices
        action Jump("d4_police_followup")

    use big_bro_see_you

screen day4_polhouse_observe():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (417, 388, 85, 262):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('d4_polhouse_lookaround.mirror')
            hover_sound day4_observe_polhouse1_mirror
            alt _("Зеркало")

        hotspot (624, 214, 105, 119):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 20)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 20)
            action Jump('d4_polhouse_lookaround.horns')
            hover_sound day4_observe_polhouse1_horns
            alt _("Рога")

        hotspot (1048, 225, 160, 197):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 22)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 22)
            action Jump('d4_polhouse_lookaround.portrait')
            hover_sound day4_observe_polhouse1_portrait
            alt _("Портрет")

        hotspot (1303, 343, 113, 368):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (24, -32)
            else:
                add "interface/eye.png" at for_hide_buttons offset (24, -32)
            action Jump('d4_polhouse_lookaround.ski')
            hover_sound day4_observe_polhouse1_ski
            alt _("Лыжи")

        hotspot (1492, 234, 101, 492):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (2, -120)
            else:
                add "interface/eye.png" at for_hide_buttons offset (2, -120)
            action Jump('d4_polhouse_lookaround.grandfather')
            hover_sound day4_observe_polhouse1_grandfather
            alt _("Комната")

        hotspot (1654, 528, 89, 177):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (-6, 10)
            else:
                add "interface/eye.png" at for_hide_buttons offset (-6, 10)
            action Jump('d4_polhouse_lookaround.telephone')
            hover_sound day4_observe_polhouse1_telephone
            alt _("Телефон")

        at for_look_buttons_3

    vbox:
        xpos 780
        ypos 790
        button:
            xsize 360
            ysize 284
            text _("ПОДОЖДАТЬ"):
                xalign .5
                yalign .5
                style "imagemap_text"
            focus_mask True
            idle_background None
            background None
            hover_background "interface/intercative_button.png"
            hover_sound day4_observe_polhouse1_wait
            action Jump("d4_polhouse_followup")

    use big_bro_see_you

screen day4_ded_door():
    layer "master"

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            xpos 1920//2
            ypos 1080//2
            anchor (.5,.5)
            hover_sound day4_ded_door_sfx
            action Return()
            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            alt _("ОТКРЫТЬ")

        text _("ОТКРЫТЬ") alt "":
            xpos 1920//2
            ypos 1080//2
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen day4_polhouse_observe2():
    layer "master"

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (430-75, 600-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('d4_polhouse_lookaround2.player')
            hover_sound day4_observe_polhouse2_player
            alt _("Проигрыватель")

        hotspot (960-75, 690-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('d4_polhouse_lookaround2.piano')
            hover_sound day4_observe_polhouse2_piano
            alt _("Пианино")

        hotspot (1500-75, 510-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('d4_polhouse_lookaround2.poster')
            hover_sound day4_observe_polhouse2_poster
            alt _("Плакат")

        at for_look_buttons_3

    default photo_hover = False

    fixed:
        if photo_hover:
            add "d4_polhouse_photo":
                align (1., 1.)
                matrixcolor BrightnessMatrix(0.1)

        button:
            xpos 835
            ypos 415
            anchor (.5, .5)
            xysize (300, 200)
            action Jump('d4_polhouse_followup2')
            hover_sound day4_observe_polhouse2_photo
            hovered SetScreenVariable("photo_hover", True)
            unhovered SetScreenVariable("photo_hover", False)
            text _("ОСМОТРЕТЬ"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                at conf_fon

    use big_bro_see_you

screen puzzle_cipher(puzzle, debug=False):
    layer "master1"
    add puzzle.background

    if debug:
        vbox:
            xalign 1.
            xanchor 1.
            textbutton "Solve":
                action Function(puzzle.force_solve)

            text "------"

            for k in puzzle.pieces:
                text f"{k}: {puzzle.pieces[k].is_valid}"

    textbutton _("ПРОПУСТИТЬ"):
        action (Function(puzzle.force_solve), Jump(puzzle.label))
        default_focus True

    draggroup:
        for k in puzzle.pieces:
            drag:
                focus_mask True
                drag_name k
                draggable True
                droppable False
                activated drag_activated_sound
                dragged puzzle.dragged, drag_dragged_sound
                pos puzzle.pieces[k].pos
                add puzzle.pieces[k].img

screen day4_open_stora():
    layer "master"

    default olya_glaza = False

    button:
        xpos 1450
        ypos 0
        xsize 470
        ysize 1080
        background "locate/home/in_side/2st_floor/anton_room/room_night_but0.png"
        hovered SetScreenVariable("olya_glaza", True)
        unhovered SetScreenVariable("olya_glaza", False)
        hover_sound day4_shtora_sfx
        action Return()
        alt _("ОТКРЫТЬ")

    if olya_glaza:
        add "locate/home/in_side/2st_floor/anton_room/room_night_but1.png"
        add "d4_Olya_Weeps_m_dark_good_aside_04":
            pos (.5, 1.)
            yanchor .711
            xanchor (1-.5)

    vbox:
        xpos 1600
        ypos 350
        xsize 245
        ysize 100
        text _("ОТКРЫТЬ") alt "":
            style "imagemap_text"

screen day4_treat_take_or_refuse_2():
    layer "master"

    default treat_refuse_hover = False

    if treat_refuse_hover:
        add "interface/intercative_button.png":
            xpos 1000
            ypos 950
            anchor (.5,.5)
        add "d4_treat_choice2_refuse_short":
            yalign 1.

    button:
        xpos 960
        ypos 50
        anchor (.5, .0)
        xysize (500, 650)
        action Jump('d4_beasts_choice_take')
        hover_sound day4_choice_marmelade_sfx_take
        if not treat_take_hover:
            hovered SetVariable("treat_take_hover", True), Jump("d4_beasts_choice2.take_hover")
        else:
            unhovered SetVariable("treat_take_hover", False), Jump("d4_beasts_choice2.take_unhover")
        alt _("ПРИНЯТЬ")

    text _("ПРИНЯТЬ") alt "":
        xpos 1000
        ypos 200
        anchor (.5,.5)
        style "imagemap_text"
        color "#fff"
        outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        if treat_take_hover:
            at transform:
                matrixcolor TintMatrix("#ffffff")
                linear 1. matrixcolor TintMatrix("#ffd429")
        else:
            at transform:
                matrixcolor TintMatrix("#ffffff")

    button:
        xpos 1000
        ypos 950
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('d4_beasts_choice2_refuse')
        hover_sound day4_choice_marmelade_sfx_refuse
        hovered SetScreenVariable("treat_refuse_hover", True)
        unhovered SetScreenVariable("treat_refuse_hover", False)
        text _("ОТКАЗАТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#fff"
            outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

# episode 5
screen day5_interactive_button(settings):
    layer "master"
    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True

            pos settings.pos
            anchor (.5,.5)

            hover_sound settings.hover_sound

            action Return()

            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            
            alt renpy.filter_text_tags(renpy.translate_string(settings.caption), ())

        text settings.caption alt "":
            pos settings.pos
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen day5_interactive_button_in_dark(settings):

    fixed:
        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True

            pos settings.pos
            anchor (.5,.5)

            hover_sound settings.hover_sound

            action Return()

            at transform:
                matrixcolor BrightnessMatrix(-.5)
                on hover:
                    alpha .8
                on idle:
                    alpha .01
            
            alt renpy.filter_text_tags(renpy.translate_string(settings.caption), ())

        text settings.caption alt "":
            pos settings.pos
            anchor (.5,.5)
            style "imagemap_text"
            color "#fff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen day5_freezer():
    imagemap:
        ground Null(1920,1080)
        idle "locate/home/in_side/1st_floor/kitchen/cold/door_01.png"
        hover im.MatrixColor("locate/home/in_side/1st_floor/kitchen/cold/door_01.png",
            im.matrix.brightness(0.10))
        alpha True
        hotspot(165,120,1095,405):
            hover_sound day5_freezer_sfx
            action [Play("test_five", day5_freezer_open_sfx), Return()]
            alt _("ОТКРЫТЬ")

    text _("ОТКРЫТЬ{#Freezer}") alt "":
        xpos 650
        ypos 350
        style "imagemap_text"

screen d5_polina_phone_display():
    layer "master"

    text str(phone_display()) alt "":
        anchor (1., .5)
        pos (1210, 312)
        size 30
        color "#000"
        font "font/JDK Don Digit.ttf"
        outlines [(1, "#666", 0, 0)]

screen d5_polina_phone_interactive():
    modal True
    layer "master"

    default phone_reset_hover = False

    text "{alt}3: 03: 95"

    for i in range(10):
        imagebutton:
            focus_mask True
            idle "d5_polina_phone_k_" + str(i) + "_idle"
            hover "d5_polina_phone_k_" + str(i) + "_hover"
            activate_sound day5_m_polina_phone_sfx_key
            action Function(phone_Add, i), Return("digit")
            keysym [f"K_{i}", f"KP_{i}"]
            alt str(i)

    if phone_reset_hover:
        add "d5_polina_phone_k_reset_hover"
    else:
        add "d5_polina_phone_k_reset_idle"

    if phone_number:
        button:
            anchor (.5, .5)
            pos (925, 350)
            xysize (200, 200)
            hovered SetScreenVariable("phone_reset_hover", True)
            unhovered SetScreenVariable("phone_reset_hover", False)
            activate_sound day5_m_polina_phone_sfx_reset
            action Return("reset")

            text _("СБРОС"):
                align (.5, 1.)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

    if config.developer:
        button:
            xpos 1400
            ypos 500
            anchor (.5, .5)
            xysize (200, 150)
            action Return()
            hovered SetScreenVariable("phone_hover", True)
            unhovered SetScreenVariable("phone_hover", False)

            text _("ДАЛЬШЕ"):
                align (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                hover_color "#ffff00"
                outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
                at conf_fon
        
        button:
            xpos 1400
            ypos 700
            anchor (.5, .5)
            xysize (200, 150)
            action Function(polina_phone.ResetOveruse), Function(SceneFlags.Reset)
            hovered SetScreenVariable("phone_hover", True)
            unhovered SetScreenVariable("phone_hover", False)

            text _("СБРОС ПРОГРЕССА"):
                align (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                hover_color "#ff00ff"
                outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
                at conf_fon

screen day5_katya_observe():
    default photo_hover = False

    if photo_hover:
        add "d5_katya_room_photo":
            matrixcolor BrightnessMatrix(0.10)

    imagemap:
        ground Null(1920,1080)
        idle Null(1920,1080)
        alpha False

        hotspot (516-75, 546-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('event_m_katya_lookaround.aqua') #aqua
            hover_sound day5_observe_katya_aqua
            alt _("Аквариум")
        
        hotspot (135-75, 646-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('event_m_katya_lookaround.mirror') #mirror
            hover_sound day5_observe_katya_mirror
            alt _("Зеркало")

        hotspot (453-75, 843-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('event_m_katya_lookaround.dollh') #dollh
            hover_sound day5_observe_katya_dollh
            alt _("Дом Барби")

        hotspot (1444-75, 297-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('event_m_katya_lookaround.certif') #certif
            hover_sound day5_observe_katya_certif
            alt _("Награды")

        hotspot (1687-75, 653-75, 150, 150):
            if eyes_visible == True:
                add "interface/eye.png" at for_look_buttons offset (0, 30)
            else:
                add "interface/eye.png" at for_hide_buttons offset (0, 30)
            action Jump('event_m_katya_lookaround.musicb') #musicb
            hover_sound day5_observe_katya_musicb
            alt _("Музыкальный центр")
        

        at for_look_buttons_3

    button:
        xpos 1350
        ypos 540
        xsize 360
        ysize 150
        anchor (.5, .5)
        text _("ОСМОТРЕТЬ"):
            xalign .5
            yalign .5
            style "imagemap_text"
        idle_background None
        background None
        hovered SetScreenVariable("photo_hover", True)
        unhovered SetScreenVariable("photo_hover", False)
        hover_sound day5_observe_katya_photo
        action Jump("event_m_katya_followup")

    use big_bro_see_you

screen cook_g(game):
    layer "master"
    add CookingDisplayable(game):
        align .5,.5

    button:
        background None
        xfill True
        yfill True
        action Function(game.PressKey)
        keyboard_focus False

    $ ms = __("Изучите сцену")
    text "{alt}[ms]"

    style_prefix "quick"

    hbox:
        align (0.5, 1.0)

        textbutton _("Успех") action Return(Cooking_Good)
        textbutton _("Провал") action Return(Cooking_Bad)
        textbutton _("ПРОПУСТИТЬ") action Return(Cooking_Skip)

screen d5_guitar_minigame():
    layer "master"
    default string_hover = False

    if string_hover == 1:
        add "guitar_string_1_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitar_string_2_idle"
        add "guitar_string_3_idle"
        add "guitar_string_4_idle"
        add "guitar_string_5_idle"
        add "guitar_string_6_idle"
        add "guitarplay ant_1_prep"
    elif string_hover == 2:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitar_string_3_idle"
        add "guitar_string_4_idle"
        add "guitar_string_5_idle"
        add "guitar_string_6_idle"
        add "guitarplay ant_2_prep"
    elif string_hover == 3:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle"
        add "guitar_string_3_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitar_string_4_idle"
        add "guitar_string_5_idle"
        add "guitar_string_6_idle"
        add "guitarplay ant_3_prep"
    elif string_hover == 4:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle"
        add "guitar_string_3_idle"
        add "guitar_string_4_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitar_string_5_idle"
        add "guitar_string_6_idle"
        add "guitarplay ant_4_prep"
    elif string_hover == 5:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle"
        add "guitar_string_3_idle"
        add "guitar_string_4_idle"
        add "guitar_string_5_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitar_string_6_idle"
        add "guitarplay ant_5_prep"
    elif string_hover == 6:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle"
        add "guitar_string_3_idle"
        add "guitar_string_4_idle"
        add "guitar_string_5_idle"
        add "guitar_string_6_idle" matrixcolor BrightnessMatrix(0.1)
        add "guitarplay ant_6_prep"
    else:
        add "guitar_string_1_idle"
        add "guitar_string_2_idle"
        add "guitar_string_3_idle"
        add "guitar_string_4_idle"
        add "guitar_string_5_idle"
        add "guitar_string_6_idle"
        add "guitarplay ant_6_up"

    imagebutton:
        idle "guitar_button_1"
        focus_mask True
        hovered SetScreenVariable("string_hover", 1)
        action Return(1)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    imagebutton:
        idle "guitar_button_2"
        focus_mask True
        hovered SetScreenVariable("string_hover", 2)
        action Return(2)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    imagebutton:
        idle "guitar_button_3"
        focus_mask True
        hovered SetScreenVariable("string_hover", 3)
        action Return(3)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    imagebutton:
        idle "guitar_button_4"
        focus_mask True
        hovered SetScreenVariable("string_hover", 4)
        action Return(4)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    imagebutton:
        idle "guitar_button_5"
        focus_mask True
        hovered SetScreenVariable("string_hover", 5)
        action Return(5)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    imagebutton:
        idle "guitar_button_6"
        focus_mask True
        hovered SetScreenVariable("string_hover", 6)
        action Return(6)
        at transform:
            on idle:
                matrixcolor BrightnessMatrix(0.0)
            on hover:
                matrixcolor BrightnessMatrix(0.1)
        keyboard_focus False

    button:
        xpos 1700
        ypos 200
        xsize 360
        ysize 284
        anchor (.5, .5)
        text _("ЗАВЕРШИТЬ"):
            xalign .5
            yalign .5
            style "imagemap_text"
        idle_background None
        hover_background "cloud_half"
        action Return("abort")
        keyboard_focus False

    $ ms = __("Изучите сцену")
    text "{alt}[ms]"

    style_prefix "quick"

    hbox:
        align (0.5, 1.0)

        textbutton _("Успех") action Return("correct")
        textbutton _("Провал") action Return(renpy.random.randint(1, 6))
        textbutton _("ПРОПУСТИТЬ") action Return("abort")

default focus_buttons = ['focus_left', 'focus_right', 'focus_up', 'focus_down']

screen day5_med_katya_or_polina():
    default focused = 0

    button:
        xpos 575
        ypos 550
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_katya')
        hover_sound day5_med_waifu_sfx_katya
        if not med_katya_hover:
            hovered SetVariable("med_katya_hover", True), Jump("d5_choice_polkatya.katya_hover")
        else:
            unhovered SetVariable("med_katya_hover", False), Jump("d5_choice_polkatya.unhover")

        text _("ПОЙТИ С КАТЕЙ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        xpos 1300
        ypos 550
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_polina')
        hover_sound day5_med_waifu_sfx_polina
        if not med_polina_hover:
            hovered SetVariable("med_polina_hover", True), Jump("d5_choice_polkatya.polina_hover")
        else:
            unhovered SetVariable("med_polina_hover", False), Jump("d5_choice_polkatya.unhover")

        text _("ПОЙТИ С ПОЛИНОЙ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("ПОЙТИ С КАТЕЙ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_med_waifu_sfx_katya) ),
        (
            Function(renpy.alt, _("ПОЙТИ С ПОЛИНОЙ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_med_waifu_sfx_polina) )
    )

    if focused == 1:
        key 'dismiss' action             Jump('event_m_katya')
    elif focused == 2:
        key 'dismiss' action Jump('event_m_polina')

screen day5_choice_m_polina_drug():
    default focused = 0

    button:
        xpos 575
        ypos 600
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_polina_accept')
        hover_sound day5_choice_m_polina_drug_sfx_accept
        if not d5_md_drug_hover:
            hovered SetVariable("d5_md_drug_hover", True), Jump("d5_choice_m_polina_drug.drug_hover")
        else:
            unhovered SetVariable("d5_md_drug_hover", False), Jump("d5_choice_m_polina_drug.drug_unhover")

        text _("ПРИНЯТЬ{#Drug}"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            at conf_fon
        keyboard_focus False

    button:
        xpos 1500
        ypos 700
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_polina_refuse')
        hover_sound day5_choice_m_polina_drug_sfx_refuse
        if not d5_md_olya_hover:
            hovered SetVariable("d5_md_olya_hover", True), Jump("d5_choice_m_polina_drug.olya_hover")
        else:
            unhovered SetVariable("d5_md_olya_hover", False), Jump("d5_choice_m_polina_drug.olya_unhover")

        text _("ОТКАЗАТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("ПРИНЯТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_choice_m_polina_drug_sfx_accept) ),
        (
            Function(renpy.alt, _("ОТКАЗАТЬСЯ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_choice_m_polina_drug_sfx_refuse) )
    )

    if focused == 1:
        key 'dismiss' action             Jump('event_m_polina_accept')
    elif focused == 2:
        key 'dismiss' action Jump('event_m_polina_refuse')

screen day5_choice_m_katya_drug():
    default focused = 0

    button:
        xpos 1350
        ypos 500
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_katya_accept')
        hover_sound day5_choice_m_katya_drug_sfx_accept
        if not d5_md_drug_hover:
            hovered SetVariable("d5_md_drug_hover", True), Jump("d5_choice_m_katya_drug.drug_hover")
        else:
            unhovered SetVariable("d5_md_drug_hover", False), Jump("d5_choice_m_katya_drug.drug_unhover")

        text _("ПРИНЯТЬ{#Drug}"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        xpos 575
        ypos 450
        anchor (.5, .5)
        xysize (300, 200)
        action Jump('event_m_katya_refuse')
        hover_sound day5_choice_m_katya_drug_sfx_refuse
        if not d5_md_olya_hover:
            hovered SetVariable("d5_md_olya_hover", True), Jump("d5_choice_m_katya_drug.olya_hover")
        else:
            unhovered SetVariable("d5_md_olya_hover", False), Jump("d5_choice_m_katya_drug.olya_unhover")

        text _("ОТКАЗАТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("ПРИНЯТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_choice_m_katya_drug_sfx_accept) ),
        (
            Function(renpy.alt, _("ОТКАЗАТЬСЯ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_choice_m_katya_drug_sfx_refuse) )
    )

    if focused == 1:
        key 'dismiss' action             Jump('event_m_katya_accept')
    elif focused == 2:
        key 'dismiss' action Jump('event_m_katya_refuse')

screen day5_choice_door(is_zulka_here):
    default focused = 0

    button:
        xpos 1150
        ypos 275
        anchor (.5, .5)
        xysize (360, 284)

        hover_background "ui_cloud 50"
        action Jump('event_invited')
        hover_sound day5_choice_door_invite
        if not invite_invite_hover:
            hovered SetVariable("invite_invite_hover", True), Jump("day5_choice_door_invite.invite_hover")
        else:
            unhovered SetVariable("invite_invite_hover", False), Jump("day5_choice_door_invite.unhover")

        text _("ВПУСТИТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        if is_zulka_here:
            xpos 500
            ypos 550
        else:
            xpos 400
            ypos 750

        anchor (.5, .5)
        xysize (360, 284)

        hover_background "ui_cloud 50"
        action Jump('event_closed_door')
        hover_sound day5_choice_door_hermit
        if not invite_hermit_hover:
            hovered SetVariable("invite_hermit_hover", True), Jump("day5_choice_door_invite.hermit_hover")
        else:
            unhovered SetVariable("invite_hermit_hover", False), Jump("day5_choice_door_invite.unhover")

        text _("НЕ ВПУСКАТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("ВПУСТИТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_choice_door_invite) ),
        (
            Function(renpy.alt, _("НЕ ВПУСКАТЬ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_choice_door_hermit) )
    )

    if focused == 1:
        key 'dismiss' action             Jump('event_invited')
    elif focused == 2:
        key 'dismiss' action Jump('event_closed_door')

screen day5_choice_polina_cross_1():
    default focused = 0

    button:
        xpos 1575
        ypos 250
        anchor (.5, .5)
        xysize (360, 284)

        action Jump('event_monsters_polina_cross_choice_1.run_trigger')
        hover_sound day5_cross_choice_sfx_run_1

        if not d5_polina_cross_run_hover:
            hovered SetVariable("d5_polina_cross_run_hover", True), Jump("event_monsters_polina_cross_choice_1.run_hover")
        else:
            unhovered SetVariable("d5_polina_cross_run_hover", False), Jump("event_monsters_polina_cross_choice_1.run_unhover")

        text _("БЕЖАТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        xpos 400
        ypos 250
        anchor (.5, .5)
        xysize (360, 284)

        action Jump('event_monsters_polina_cross_2')
        hover_sound day5_cross_choice_sfx_pray_1
        if not d5_polina_cross_pray_hover:
            hovered SetVariable("d5_polina_cross_pray_hover", True), Jump("event_monsters_polina_cross_choice_1.pray_hover")
        else:
            unhovered SetVariable("d5_polina_cross_pray_hover", False), Jump("event_monsters_polina_cross_choice_1.pray_unhover")

        text _("МОЛИТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("БЕЖАТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_cross_choice_sfx_run_1) ),
        (
            Function(renpy.alt, _("МОЛИТЬСЯ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_cross_choice_sfx_pray_1) )
    )

    if focused == 1:
        key 'dismiss' action Jump('event_monsters_polina_cross_choice_1.run_trigger')
    elif focused == 2:
        key 'dismiss' action Jump('event_monsters_polina_cross_2')

screen day5_choice_polina_cross_2():
    default focused = 0

    button:
        xpos 1575 + 100
        ypos 250 + 600
        anchor (.5, .5)
        xysize (360, 284)
        hover_background "ui_cloud 100"
        action Jump('event_monsters_polina_cross_choice_2.run_trigger')
        hover_sound day5_cross_choice_sfx_run_2

        if not d5_polina_cross2_run_hover:
            hovered SetVariable("d5_polina_cross2_run_hover", True), Jump("event_monsters_polina_cross_choice_2.run_hover")
        else:
            unhovered SetVariable("d5_polina_cross2_run_hover", False), Jump("event_monsters_polina_cross_choice_2.run_unhover")

        text _("БЕЖАТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        xpos 400 +450
        ypos 250 +150
        anchor (.5, .5)
        xysize (360, 284)

        action Jump('event_monsters_polina_cross_3')
        hover_sound day5_cross_choice_sfx_pray_2
        if not d5_polina_cross2_pray_hover:
            hovered SetVariable("d5_polina_cross2_pray_hover", True), Jump("event_monsters_polina_cross_choice_2.pray_hover")
        else:
            unhovered SetVariable("d5_polina_cross2_pray_hover", False), Jump("event_monsters_polina_cross_choice_2.pray_unhover")

        text _("МОЛИТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("БЕЖАТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_cross_choice_sfx_run_2) ),
        (
            Function(renpy.alt, _("МОЛИТЬСЯ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_cross_choice_sfx_pray_2) )
    )

    if focused == 1:
        key 'dismiss' action Jump('event_monsters_polina_cross_choice_2.run_trigger')
    elif focused == 2:
        key 'dismiss' action Jump('event_monsters_polina_cross_3')

screen day5_choice_polina_cross_3():
    default focused = 0

    button:
        xpos 1675
        ypos 430
        anchor (.5, .5)
        xysize (360, 284)
        hover_background "ui_cloud 70"
        action Jump('event_monsters_polina_cross_choice_3.run_trigger')
        hover_sound day5_cross_choice_sfx_run_3

        if not d5_polina_cross3_run_hover:
            hovered SetVariable("d5_polina_cross3_run_hover", True), Jump("event_monsters_polina_cross_choice_3.run_hover")
        else:
            unhovered SetVariable("d5_polina_cross3_run_hover", False), Jump("event_monsters_polina_cross_choice_3.run_unhover")

        text _("БЕЖАТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    button:
        xpos 300
        ypos 450
        anchor (.5, .5)
        xysize (360, 284)

        action Jump('d5_ending_still_water')
        hover_sound day5_cross_choice_sfx_pray_3
        if not d5_polina_cross3_pray_hover:
            hovered SetVariable("d5_polina_cross3_pray_hover", True), Jump("event_monsters_polina_cross_choice_3.pray_hover")
        else:
            unhovered SetVariable("d5_polina_cross3_pray_hover", False), Jump("event_monsters_polina_cross_choice_3.pray_unhover")

        text _("МОЛИТЬСЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
        keyboard_focus False

    key focus_buttons action If(
        focused != 1,
        (
            Function(renpy.alt, _("БЕЖАТЬ"), _update_screens=False),
            SetScreenVariable('focused', 1),
            Play('audio', day5_cross_choice_sfx_run_3) ),
        (
            Function(renpy.alt, _("МОЛИТЬСЯ"), _update_screens=False),
            SetScreenVariable('focused', 2),
            Play('audio', day5_cross_choice_sfx_pray_3) )
    )

    if focused == 1:
        key 'dismiss' action Jump('event_monsters_polina_cross_choice_3.run_trigger')
    elif focused == 2:
        key 'dismiss' action Jump('d5_ending_still_water')

screen day5_choice_polina_amulet():
    default focused = 0

    button:
        xpos 800 +100
        ypos 750
        anchor (.5, .5)
        xysize (360, 284)
        hover_background "ui_cloud 50"
        action Jump('d5_ending_pack_of')
        hover_sound day5_amulet_choice_sfx_refuse
        hovered SetScreenVariable('focused', 0)

        text _("НЕБРАТЬ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]


    button:
        xpos 1200 +100
        ypos 250
        anchor (.5, .5)
        xysize (360, 284)
        hover_background "ui_cloud 50"
        action Jump('d5_ending_among_us')
        hover_sound day5_amulet_choice_sfx_self
        hovered SetScreenVariable('focused', 0)

        text _("ЗАБРАТЬ СЕБЕ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    button:
        xpos 400 +100
        ypos 250
        anchor (.5, .5)
        xysize (360, 284)
        hover_background "ui_cloud 50"
        action Jump('d5_ending_bloody_claw')
        hover_sound day5_amulet_choice_sfx_olya
        if not d5_polina_amulet_oly_hover:
            hovered SetVariable("d5_polina_amulet_oly_hover", True), SetScreenVariable('focused', 1), Jump("event_monsters_polina_amulet_choice.oly_hover")
        else:
            unhovered SetVariable("d5_polina_amulet_oly_hover", False), Jump("event_monsters_polina_amulet_choice.oly_unhover")

        text _("ОТДАТЬ ОЛЕ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    if focused == 1:
        key 'dismiss' action Jump('d5_ending_bloody_claw')

screen day5_monsters_refuse_choice(anton, roma, polina, meat, zhulka):
    layer "master"

    if meat:
        if d5_monsters_ref_meat_hover:
            add "d5_monchoice_fridge_hover"

    if d5_monsters_ref_oly_hover:
        add "d5_monchoice_oly_hover"
    else:
        add "d5_monchoice_oly_idle"

    if roma:
        if d5_monsters_ref_rom_hover:
            add "d5_monchoice_rom_hover"
        else:
            add "d5_monchoice_rom_idle"

    if polina:
        if d5_monsters_ref_pol_hover:
            add "d5_monchoice_pol_hover"
        else:
            add "d5_monchoice_pol_idle"

    if d5_monsters_ref_ant_hover:
        add "d5_monchoice_ant_hover"
    else:
        add "d5_monchoice_ant_idle"

    if zhulka:
        add "d5_zhulka dark"

    add "bg_black":

        at transform:
            alpha .6

    if meat:
        button:
            xpos 875
            ypos 200
            anchor (.5, .5)
            xysize (360, 284)
            action Jump('event_monsters_dog_refuse')
            hover_sound day5_monsters_choice_sfx_meat

            hovered SetVariable("d5_monsters_ref_meat_hover", True)
            unhovered SetVariable("d5_monsters_ref_meat_hover", False)

            text _("СОБАЧАТИНА"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                at conf_fon


    button:
        xpos 700 +100
        ypos 900 +25
        anchor (.5, .5)
        xysize (360, 284)
        action Jump('event_monsters_olya_choice')
        hover_sound day5_monsters_choice_sfx_olya

        hovered SetVariable("d5_monsters_ref_oly_hover", True)
        unhovered SetVariable("d5_monsters_ref_oly_hover", False)

        text __("ОЛЯ"):
            anchor (.5,.5)
            style "imagemap_text"
            color "#ffffff"
            outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            at conf_fon


    if roma:
        button:
            xpos 1350 -50
            ypos 500
            anchor (.5, .5)
            xysize (360, 284)
            action Jump('event_monsters_roma')
            hover_sound day5_monsters_choice_sfx_roma

            hovered SetVariable("d5_monsters_ref_rom_hover", True)
            unhovered SetVariable("d5_monsters_ref_rom_hover", False)

            text __("РОМА"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                at conf_fon


    if polina:
        button:
            xpos 1750 +25
            ypos 400
            anchor (.5, .5)
            xysize (360, 284)
            action Jump('event_monsters_polina_choice')
            hover_sound day5_monsters_choice_sfx_polina

            hovered SetVariable("d5_monsters_ref_pol_hover", True)
            unhovered SetVariable("d5_monsters_ref_pol_hover", False)

            text __("ПОЛИНА"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                at conf_fon


    if anton:
        button:
            xpos 300
            ypos 400
            anchor (.5, .5)
            xysize (360, 284)
            action Jump('event_monsters_anton_refuse')
            hover_sound day5_monsters_choice_sfx_anton

            hovered SetVariable("d5_monsters_ref_ant_hover", True)
            unhovered SetVariable("d5_monsters_ref_ant_hover", False)

            text __("АНТОН"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                at conf_fon


    if zhulka:
        button:
            xpos 800
            ypos 600
            anchor (.5, .5)
            xysize (360, 284)
            action Return()
            hover_sound day5_monsters_choice_sfx_zhulka
            alt _("Жулька")

# achievements
init python:
    def get_translated_notify(ach_id):
        ms = __("Достижение")
        ach = renpy.translate_string(achievement_names[ach_id])

        return f"{ms}: {ach}"
        

    def achievement_grant(ach_id):
        pause = False

        if not achievement.has(ach_id):
            renpy.stop_skipping()
            renpy.alt(get_translated_notify(ach_id))
            pause = True

        achievement.grant(ach_id)

        if pause:
            pause = False
            renpy.pause(3.25, hard=True)

        all_granted = True
        for ach_id in achievement_list:
            if ach_id == "ach_collector":
                continue
            
            if not achievement.has(ach_id):
                all_granted = False
        
        if all_granted:
            if not achievement.has("ach_collector"):
                renpy.stop_skipping()
                renpy.alt(get_translated_notify("ach_collector"))
                pause = True

            achievement.grant("ach_collector")
            achievement.sync()

            if pause:
                renpy.pause(3.25, hard=True)


define achievement_names = {
    "ach_detective_1": _("Настоящий детектив 1"),
    "ach_number": _("Полезные связи"),
    "ach_Vova": _("Где же ты, Вова?"),
    "ach_escaped": _("Беги, спасайся"),
    "ach_tape": _("Чертова кассета"),
    "ach_neverland": _("Небыляндия"),
    "ach_radio": _("Тайное послание"),

    "ach_accepted_treat": _("Сладость"),
    "ach_rejected_treat": _("Гадость"),
    "ach_detective_2": _("Настоящий детектив 2"),
    "ach_force": _("Левый коронный"),
    "ach_fight": _("Правый похоронный"),
    "ach_insulted": _("Униженный и оскорбленный"),
    "ach_knigh": _("Рыцарь!"),
    "ach_adventure": _("Авантюрист!"),
    "ach_masquerade": _("Маски-шоу"),
    "ach_tough_luck": _("Не фартануло"),

    "ach_amulet": _("Шаман Кинг"),
    "ach_sceptic": _("Скептик"),
    "ach_duckinator": _("Утилизатор"),
    "ach_quiet": _("Рот на замок"),
    "ach_van_gogh": _("Ван Гог"),
    "ach_meanie": _("Бяка"),
    "ach_bro": _("Братик"),
    "ach_voltron": _("Команда Вольтрона"),
    "ach_muse": _("Муза"),
    "ach_ring": _("Моя прелесть!"),
    "ach_missed": _("Раззява"),
    "ach_victory": _("О, счастливчик!"),
    "ach_defeat": _("Лопух"),
    "ach_detective_3": _("Настоящий детектив 3"),

    "ach_pig": _("Дементий!"),
    "ach_Haide": _("Мистер Хайд"),
    "ach_Djakel": _("Доктор Джекил"),
    "ach_musketeers": _("Три мушкетера"),
    "ach_no": _("Третий лишний"),
    "ach_strawberry": _("Клубника"),
    "ach_meat": _("Фарш"),
    "ach_end1": _("Школяр-убийца"),
    "ach_secret": _("Секретные материалы"),
    "ach_dicaprio": _("Выживший"),
    "ach_cops": _("Дядя Стёпа"),
    "ach_true4": _("Настоящий детектив 4"),

    "ach_amur": _("Хромой амур"),
    "ach_melo": _("Мелодия любви"),
    "ach_smak": _("Смак!"),
    "ach_blevan": _("Блеванже"),
    "ach_lapke": _("У меня лапки"),
    "ach_fish": _("Аквамен"),
    "ach_bard": _("Бард"),
    "ach_punk": _("Панк"),
    "ach_bezdar": _("Бездарь"),
    "ach_red": _("Красная таблетка"),
    "ach_zoh": _("ЗОЖ"),
    "ach_blue": _("Синяя таблетка"),
    "ach_natur": _("Натуропатия"),
    "ach_P_R": _("Ромео+Джульета"),
    "ach_P": _("Джентльмен"),
    "ach_hodor": _("Ходор"),
    "ach_gerasim": _("Герасим"),
    "ach_pavlov": _("Доктор Павлов"),
    "ach_love": _("Любовь"),
    "ach_family": _("Семья"),
    "ach_beast": _("Зверь"),
    "ach_human": _("Человек"),
    "ach_kill_rom": _("Вкус предательства"),
    "ach_kill_polina": _("Вкус разлуки"),
    "ach_kill_olya": _("Вкус утраты"),
    "ach_hot": _("Хот-дог"),
    "ach_sherlok": _("Шерлок"),
    "ach_stanislavski": _("Не верю!"),
    "ach_yaz": _("Язычник"),
    "ach_cross": _("Экзорцист"),
    "ach_star": _("Звезда Полынь"),
    "ach_ego": _("Эгоист"),
    "ach_altruist": _("Альтруист"),
    "ach_light": _("Путь света"),
    "ach_dark": _("Путь тьмы"),
    "ach_norm": _("Нормис"),
    "ach_sigma": _("Сигма бой"),
    "ach_1890": _("Апокалипсис сегодня"),
    "ach_light_off": _("Погасший свет"),
    "ach_P_end": _("Без лишних глаз"),
    "ach_grey": _("Серенький волчок"),
    "ach_reunification": _("Воссоединение"),
    "ach_blood": _("Кровь за кровь"),
    "ach_hell": _("Адский пикник"),
    "ach_madhouse": _("Дурка зовёт"),
    "ach_alien": _("Чужой"),
    "ach_ratatouille": _("Рататуй"),
    "ach_canned": _("Консерва"),
    "ach_solid": _("Цельный Зайчик"),
    "ach_last_spurt": _("Последний рывок"),
    "ach_abyss": _("Бег по краю пропасти"),
    "ach_last_hero": _("Последний герой"),
    "ach_bodrov": _("Не брат ты мне..."),
    "ach_letov": _("Винтовка - это праздник!"),
    "ach_darkness": _("Вместилище тьмы"),
    "ach_Davie504": _("Слабо, Davie504?"),
    "ach_zulka": _("Жулька против"),
    "ach_detective_5": _("Настоящий детектив 5"),
    "ach_collector": _("Властелин Ачивок")
}

# flowchart
init python:
    def purify_brackets(text):
        result = ""
        state = 0

        for char in text:
            if char == "{":
                state = 1
                continue
            if char == "}":
                state = 0
                continue
            if state == 1:
                continue
            
            result += char
        return result

screen StoryExplainer_NarrativeSegment(story_manager, kday, kevent, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)

        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent))

        tooltip (story_manager.day_code, kevent)


        background None
        
        if story_manager.IsMarkedPersist((story_manager.day_code, kevent)) or forced:
            $ caption = event["caption"]
            $ alt_caption = purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

        else:
            $ caption = "???"
            $ alt_caption = "Не открыто"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)) or forced:
            add "flowchart_white" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
                alt alt_caption
        else:
            add "flowchart_gray" align (.5, .5):
                at transform:
                    alpha 0.7
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
                alt alt_caption

screen StoryExplainer_NarrativeSegment_Extended(story_manager, kday, kevent, kopt, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)
        
        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent, kopt))
        
        tooltip (story_manager.day_code, kevent, kopt)

        background None
        
        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = event["caption"]
            $ alt_caption = purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent, kopt):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

        else:
            $ caption = "???"
            $ alt_caption = "Не открыто"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            add "flowchart_white" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
                alt alt_caption
        else:
            add "flowchart_gray" align (.5, .5):
                at transform:
                    alpha 0.7
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
                alt alt_caption

screen StoryExplainer_EndingSegment(story_manager, kday, kevent, kopt, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize (400, 85)
        xanchor .5
        yanchor .5
        padding (0, 0)

        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent, kopt))

        tooltip (story_manager.day_code, kevent, kopt)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = __("{size=-5}конец:{/size} ") + __(event["caption"])
            $ alt_caption = purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent, kopt):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

        else:
            $ caption = __("{size=-5}конец:{/size} ") + "???"
            $ alt_caption = __("{size=-5}конец:{/size} ") + "Не открыто"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            add "flowchart_ending" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
                alt alt_caption
        else:
            add "flowchart_ending_dim" align (.5, .5):
                at transform:
                    alpha 0.65
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
                alt alt_caption

screen StoryExplainer_ChoiceSegment(story_manager, kday, kevent, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)
        
        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent))
        
        tooltip (story_manager.day_code, kevent)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent)) or forced:
            $ caption = event["caption"]
            $ alt_caption = "Выбор: " + purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

        else:
            $ caption = "???"
            $ alt_caption = "Выбор: " + "Не открыто"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)) or forced:
            add "flowchart_black" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#fff"
                alt alt_caption
        else:
            add "flowchart_black" align (.5, .5) alpha 0.65
            text caption:
                align (.5, .5)
                size 50
                color "#ccc"
                alt alt_caption

screen StoryExplainer_OptionSegment(story_manager, kday, kevent, xypos, kopt, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos
    
    $ option = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x_opt = _x + option["pos"][0]
    $ _y_opt = _y + option["pos"][1]

    button:
        pos (_x_opt, _y_opt)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)
        
        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent, kopt))

        tooltip (story_manager.day_code, kevent, kopt)

        background None
        

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = option["caption"]
            $ alt_caption = "Опция: " + purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent, kopt):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

        else:
            $ caption = "???"
            $ alt_caption = "Опция: " + "Не открыто"
        
        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            $ alt_caption = alt_caption + ": Выбрано"
            add "flowchart_black" align (.5, .5)
            add "flowchart_frame" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#fff"
                alt alt_caption
        else:
            add "flowchart_dark" align (.5, .5):
                at transform:
                    alpha 0.5
            text caption:
                align (.5, .5)
                size 50
                color "#bdbdbd"
                alt alt_caption

screen StoryExplainer_LookaroundSegment(story_manager, kday, kevent, xypos, xysize, items):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize xysize
        padding (0, 0)
        background None
        
        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent))
        
        tooltip (story_manager.day_code, kevent)

        add "flowchart_corner_topleft"      align (0., 0.)
        add "flowchart_corner_topright"     align (1., 0.)
        add "flowchart_corner_bottomleft"   align (0., 1.)
        add "flowchart_corner_bottomright"  align (1., 1.)

        $ caption = event["caption"]
        $ alt_caption = "Блок: " + purify_brackets(__(caption))

        if story_manager.last_added == (story_manager.day_code, kevent):
            $ caption = "> " + caption + " <"
            $ alt_caption = "Сейчас здесь: " + alt_caption

        if not story_manager.IsMarkedPersist((story_manager.day_code, kevent)):
            $ caption = "???"
            $ alt_caption = "Блок: " + "Не открыто"


        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)):
            add "flowchart_eye" align (.5, 0.)
            text caption ypos 25 xalign .5 color "#fff" alt alt_caption

        else:
            add "flowchart_eye" align (.5, 0.):
                at transform:
                    alpha .7
            text caption ypos 25 xalign .5 color "#bdbdbd" alt alt_caption:
                at transform:
                    alpha .7

    for it in items:
        $ item = story_manager.story_db[story_manager.day_code][kevent][it]
        $ _x_it = _x + item["pos"][0]
        $ _y_it = _y + item["pos"][1]

        button:
            pos (_x_it, _y_it)
            xysize (400, 75)
            xanchor .5
            yanchor .5
            padding (0, 0)

            if config.developer == True:
                action Function(story_manager.Toggle, (story_manager.day_code, kevent, it))
            
            tooltip (story_manager.day_code, kevent, it)

            background None

            $ caption = item["caption"]
            $ alt_caption = "Предмет: " + purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent, it):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

            if not story_manager.IsMarkedPersist((story_manager.day_code, kevent, it)):
                $ caption = "???"
                $ alt_caption = "Не открыто"

            if story_manager.IsMarkedLocal((story_manager.day_code, kevent, it)):
                $ alt_caption = alt_caption + ": Осмотрено"
                add "flowchart_white" align (.5, .5)
                text caption:
                    align (.5, .5)
                    size 50
                    color "#000"
                    alt alt_caption
            else:
                add "flowchart_gray" align (.5, .5):
                    at transform:
                        alpha 0.7
                text caption:
                    align (.5, .5)
                    size 50
                    color "#303030"
                    alt alt_caption

screen StoryExplainer_GameSegment(story_manager, kday, kevent, xypos, xysize, items):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    button:
        pos (_x, _y)
        xysize xysize
        padding (0, 0)

        if config.developer == True:
            action Function(story_manager.Toggle, (story_manager.day_code, kevent))
        
        tooltip (story_manager.day_code, kevent)

        background None

        add "flowchart_corner_topleft"      align (0., 0.)
        add "flowchart_corner_topright"     align (1., 0.)
        add "flowchart_corner_bottomleft"   align (0., 1.)
        add "flowchart_corner_bottomright"  align (1., 1.)

        
        $ caption = event["caption"]
        $ alt_caption = "Миниигра: " + purify_brackets(__(caption))

        if story_manager.last_added == (story_manager.day_code, kevent):
            $ caption = "> " + caption + " <"
            $ alt_caption = "Сейчас здесь: " + alt_caption

        if not story_manager.IsMarkedPersist((story_manager.day_code, kevent)):
            $ caption = "???"
            $ alt_caption = "Не открыто"


        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)):
            add "flowchart_joystick" align (.5, 0.) matrixcolor BrightnessMatrix(1.0)
            text caption ypos 25 xalign .5 color "#fff" alt alt_caption

        else:
            add "flowchart_joystick" align (.5, 0.):
                matrixcolor BrightnessMatrix(1.0)
                at transform:
                    alpha .7
            text caption ypos 25 xalign .5 color "#bdbdbd" alt alt_caption:
                at transform:
                    alpha .7
        
    for it in items:
        $ item = story_manager.story_db[story_manager.day_code][kevent][it]
        $ _x_it = _x + item["pos"][0]
        $ _y_it = _y + item["pos"][1]

        button:
            pos (_x_it, _y_it)
            xysize (400, 75)
            xanchor .5
            yanchor .5
            padding (0, 0)

            if config.developer == True:
                action Function(story_manager.Toggle, (story_manager.day_code, kevent, it))
            
            tooltip (story_manager.day_code, kevent, it)

            background None

            $ caption = item["caption"]
            $ alt_caption = purify_brackets(__(caption))

            if story_manager.last_added == (story_manager.day_code, kevent, it):
                $ caption = "> " + caption + " <"
                $ alt_caption = "Сейчас здесь: " + alt_caption

            if not story_manager.IsMarkedPersist((story_manager.day_code, kevent, it)):
                $ caption = "???"
                $ alt_caption = "Не открыто"

            if story_manager.IsMarkedLocal((story_manager.day_code, kevent, it)):
                add "flowchart_white" align (.5, .5)
                text caption:
                    align (.5, .5)
                    size 50
                    color "#000"
                    alt alt_caption
            else:
                add "flowchart_gray" align (.5, .5):
                    at transform:
                        alpha 0.7
                text caption:
                    align (.5, .5)
                    size 50
                    color "#303030"
                    alt alt_caption


# translation
translate english strings:
    old "Громкость по умолчанию"
    new "Default volume"

    old "Новая запись"
    new "New recording"

    old "Юла"
    new "Spinning top"

    old "Крест"
    new "Cross"

    old "Телефон"
    new "Phone"

    old "Кладовка"
    new "Storage room"

    old "Календарь"
    new "Calendar"
    old "Газета"
    new "Newspaper"

    old "Боковина холодильника"
    new "Side of the refrigerator"

    old "Холодильник"
    new "Refrigerator"

    old "Штора"
    new "Curtain"

    old "Игрушки"
    new "Toys"

    old "Рисунки"
    new "Drawings"

    old "Книга"
    new "Book"

    old "Мишка"
    new "Teddy bear"

    old "Копилка"
    new "Piggy bank"

    old "Старшеклассники"
    new "High school students"

    old "Мужчина"
    new "Man"

    old "Гнездо"
    new "Nest"

    old "Автомобиль"
    new "Car"

    old "Обувь"
    new "Shoes"

    old "Ведёрко"
    new "Bucket"

    old "Самолётик"
    new "Toy plane"

    old "Повешенный"
    new "Hanged man"

    old "Шприц"
    new "Syringe"

    old "Белка"
    new "Squirrel"

    old "Изучите сцену"
    new "Examine the scene"

    old "Проектор"
    new "Projector"

    old "Портреты"
    new "Portraits"

    old "Петарды"
    new "Firecrackers"

    old "Летов"
    new "Letov"

    old "Цой"
    new "Tsoi"

    old "Бодров"
    new "Bodrov"

    old "Трудовик"
    new "Shop teacher"

    old "Подозреваемый"
    new "Suspect"

    old "Ножницы"
    new "Scissors"

    old "Бумага"
    new "Paper"

    old "Камень"
    new "Stone"

    old "Хлам"
    new "Junk"

    old "Инструменты"
    new "Tools"

    old "Полка"
    new "Shelf"

    old "Тиски"
    new "Vise"

    old "Ящики"
    new "Boxes"

    old "Этап пройден"
    new "Stage completed"

    old "Камера"
    new "Prison cell"

    old "Противогаз"
    new "Gas mask"

    old "Зеркало"
    new "Mirror"

    old "Рога"
    new "Horns"

    old "Портрет"
    new "Portrait"

    old "Лыжи"
    new "Skis"

    old "Комната"
    new "Room"

    old "Проигрыватель"
    new "Player"

    old "Пианино"
    new "Piano"

    old "Плакат"
    new "Poster"

    old "Аквариум"
    new "Aquarium"

    old "Дом Барби"
    new "Barbie house"

    old "Награды"
    new "Awards"

    old "Музыкальный центр"
    new "Music system"

    # old "Жулька"
    # new "Zhulka"

    old "Успех"
    new "Success"

    old "Провал"
    new "Failure"

    old "Достижение"
    new "Achievement"

    old "Взять крест"
    new "Take the Cross"

    old "Взять амулет"
    new "Take the Amulet"

    old "Приглушить музыку и звуки"
    new "Lower music and sound effects"

    old "Произнести последнюю реплику"
    new "Say the Final Line"

translate chinese strings:
    old "Громкость по умолчанию"
    new "默认音量"

    old "Новая запись"
    new "新录音"

    old "Юла"
    new "陀螺"

    old "Крест"
    new "十字架"

    old "Телефон"
    new "电话"

    old "Кладовка"
    new "储藏室"

    old "Календарь"
    new "日历"

    old "Газета"
    new "报纸"

    old "Боковина холодильника"
    new "冰箱侧面"

    old "Холодильник"
    new "冰箱"

    old "Штора"
    new "窗帘"

    old "Игрушки"
    new "玩具"

    old "Рисунки"
    new "图画"

    old "Книга"
    new "书"

    old "Мишка"
    new "泰迪熊"

    old "Копилка"
    new "储蓄罐"

    old "Старшеклассники"
    new "高中生"

    old "Мужчина"
    new "男人"

    old "Гнездо"
    new "巢"

    old "Автомобиль"
    new "汽车"

    old "Обувь"
    new "鞋"

    old "Ведёрко"
    new "小桶"

    old "Самолётик"
    new "小飞机"

    old "Повешенный"
    new "上吊的人"

    old "Шприц"
    new "注射器"

    old "Белка"
    new "松鼠"

    old "Изучите сцену"
    new "查看现场"

    old "Проектор"
    new "投影仪"

    old "Портреты"
    new "肖像"

    old "Петарды"
    new "鞭炮"

    old "Летов"
    new "列托夫"

    old "Цой"
    new "崔"

    old "Бодров"
    new "博德罗夫"

    old "Трудовик"
    new "劳动课老师"

    old "Подозреваемый"
    new "嫌疑人"

    old "Ножницы"
    new "剪刀"

    old "Бумага"
    new "纸"

    old "Камень"
    new "石头"

    old "Хлам"
    new "杂物"

    old "Инструменты"
    new "工具"

    old "Полка"
    new "架子"

    old "Тиски"
    new "台钳"

    old "Ящики"
    new "箱子"

    old "Этап пройден"
    new "阶段完成"

    old "Камера"
    new "牢房"

    old "Противогаз"
    new "防毒面具"

    old "Зеркало"
    new "镜子"

    old "Рога"
    new "角"

    old "Портрет"
    new "肖像"

    old "Лыжи"
    new "滑雪板"

    old "Комната"
    new "房间"

    old "Проигрыватель"
    new "播放器"

    old "Пианино"
    new "钢琴"

    old "Плакат"
    new "海报"

    old "Аквариум"
    new "水族箱"

    old "Дом Барби"
    new "芭比娃娃屋"

    old "Награды"
    new "奖项"

    old "Музыкальный центр"
    new "音乐中心"

    # old "Жулька"
    # new "朱尔卡"

    old "Успех"
    new "成功"

    old "Провал"
    new "失败"

    old "Достижение"
    new "成就"

    old "Взять крест"
    new "背起十字架"

    old "Взять амулет"
    new "拿起护身符"

    old "Приглушить музыку и звуки"
    new "降低音乐和音效"

    old "Произнести последнюю реплику"
    new "说出最后一句台词"

translate italiano strings:
    old "Громкость по умолчанию"
    new "Volume predefinito"

    old "Новая запись"
    new "Nuova registrazione"

    old "Юла"
    new "Trottola"

    old "Крест"
    new "Croce"

    old "Телефон"
    new "Telefono"

    old "Кладовка"
    new "Ripostiglio"

    old "Календарь"
    new "Calendario"

    old "Газета"
    new "Giornale"

    old "Боковина холодильника"
    new "Fianco del frigorifero"

    old "Холодильник"
    new "Frigorifero"

    old "Штора"
    new "Tenda"

    old "Игрушки"
    new "Giocattoli"

    old "Рисунки"
    new "Disegni"

    old "Книга"
    new "Libro"

    old "Мишка"
    new "Orsacchiotto"

    old "Копилка"
    new "Salvadanaio"

    old "Старшеклассники"
    new "Studenti delle superiori"

    old "Мужчина"
    new "Uomo"

    old "Гнездо"
    new "Nido"

    old "Автомобиль"
    new "Automobile"

    old "Обувь"
    new "Scarpe"

    old "Ведёрко"
    new "Secchio"

    old "Самолётик"
    new "Aereoplanino"

    old "Повешенный"
    new "Impiccato"

    old "Шприц"
    new "Siringa"

    old "Белка"
    new "Scoiattolo"

    old "Изучите сцену"
    new "Esamina la scena"

    old "Проектор"
    new "Proiettore"

    old "Портреты"
    new "Ritratti"

    old "Петарды"
    new "Petardi"

    old "Летов"
    new "Letov"

    old "Цой"
    new "Tsoi"

    old "Бодров"
    new "Bodrov"

    old "Трудовик"
    new "Insegnante di tecnologia"

    old "Подозреваемый"
    new "Sospettato"

    old "Ножницы"
    new "Forbici"

    old "Бумага"
    new "Carta"

    old "Камень"
    new "Pietra"

    old "Хлам"
    new "Rottami"

    old "Инструменты"
    new "Attrezzi"

    old "Полка"
    new "Mensola"

    old "Тиски"
    new "Morsa"

    old "Ящики"
    new "Casse"

    old "Этап пройден"
    new "Livello completato"

    old "Камера"
    new "Cella di prigione"

    old "Противогаз"
    new "Maschera antigas"

    old "Зеркало"
    new "Specchio"

    old "Рога"
    new "Corna"

    old "Портрет"
    new "Ritratto"

    old "Лыжи"
    new "Sci"

    old "Комната"
    new "Stanza"

    old "Проигрыватель"
    new "Lettore"

    old "Пианино"
    new "Pianoforte"

    old "Плакат"
    new "Poster"

    old "Аквариум"
    new "Acquario"

    old "Дом Барби"
    new "Casa di Barbie"

    old "Награды"
    new "Premi"

    old "Музыкальный центр"
    new "Impianto stereo"

    # old "Жулька"
    # new "Zhulka"

    old "Успех"
    new "Successo"

    old "Провал"
    new "Fallimento"

    old "Достижение"
    new "Traguardo"

    old "Взять крест"
    new "Prendere la croce"

    old "Взять амулет"
    new "Prendere l'amuleto"

    old "Приглушить музыку и звуки"
    new "Abbassare la musica e i suoni"

    old "Произнести последнюю реплику"
    new "Pronunciare l’ultima battuta"

translate turkish strings:
    old "Громкость по умолчанию"
    new "Varsayılan ses düzeyi"

    old "Новая запись"
    new "Yeni kayıt"

    old "Юла"
    new "Topaç"

    old "Крест"
    new "Haç"

    old "Телефон"
    new "Telefon"

    old "Кладовка"
    new "Kiler"

    old "Календарь"
    new "Takvim"

    old "Газета"
    new "Gazete"

    old "Боковина холодильника"
    new "Buzdolabı yanı"

    old "Холодильник"
    new "Buzdolabı"

    old "Штора"
    new "Perde"

    old "Игрушки"
    new "Oyuncaklar"

    old "Рисунки"
    new "Çizimler"

    old "Книга"
    new "Kitap"

    old "Мишка"
    new "Oyuncak ayı"

    old "Копилка"
    new "Kumbara"

    old "Старшеклассники"
    new "Lise öğrencileri"

    old "Мужчина"
    new "Erkek"

    old "Гнездо"
    new "Yuva"

    old "Автомобиль"
    new "Otomobil"

    old "Обувь"
    new "Ayakkabı"

    old "Ведёрко"
    new "Kova"

    old "Самолётик"
    new "Küçük uçak"

    old "Повешенный"
    new "Asılmış adam"

    old "Шприц"
    new "Enjektör"

    old "Белка"
    new "Sincap"

    old "Изучите сцену"
    new "Sahneyi incele"

    old "Проектор"
    new "Projektör"

    old "Портреты"
    new "Portreler"

    old "Петарды"
    new "Maytaplar"

    old "Летов"
    new "Letov"

    old "Цой"
    new "Tsoi"

    old "Бодров"
    new "Bodrov"

    old "Трудовик"
    new "El işi öğretmeni"

    old "Подозреваемый"
    new "Şüpheli"

    old "Ножницы"
    new "Makas"

    old "Бумага"
    new "Kağıt"

    old "Камень"
    new "Taş"

    old "Хлам"
    new "Hurda"

    old "Инструменты"
    new "Aletler"

    old "Полка"
    new "Raf"

    old "Тиски"
    new "Mengene"

    old "Ящики"
    new "Kutular"

    old "Этап пройден"
    new "Aşama tamamlandı"

    old "Камера"
    new "Hücre"

    old "Противогаз"
    new "Gaz maskesi"

    old "Зеркало"
    new "Ayna"

    old "Рога"
    new "Boynuzlar"

    old "Портрет"
    new "Portre"

    old "Лыжи"
    new "Kayaklar"

    old "Комната"
    new "Oda"

    old "Проигрыватель"
    new "Oynatıcı"

    old "Пианино"
    new "Piyano"

    old "Плакат"
    new "Afiş"

    old "Аквариум"
    new "Akvaryum"

    old "Дом Барби"
    new "Barbie evi"

    old "Награды"
    new "Ödüller"

    old "Музыкальный центр"
    new "Müzik seti"

    # old "Жулька"
    # new "Zhulka"

    old "Успех"
    new "Başarı"

    old "Провал"
    new "Başarısızlık"

    old "Достижение"
    new "Başarı"

    old "Взять крест"
    new "Haçı almak"

    old "Взять амулет"
    new "Tılsımı almak"

    old "Приглушить музыку и звуки"
    new "Müziği ve sesleri kıs"

    old "Произнести последнюю реплику"
    new "Son repliği söyle"

translate japan strings:
    old "Громкость по умолчанию"
    new "デフォルト音量"

    old "Новая запись"
    new "新しい録音"

    old "Юла"
    new "こま"

    old "Крест"
    new "十字架"

    old "Телефон"
    new "電話"

    old "Кладовка"
    new "物置"

    old "Календарь"
    new "カレンダー"

    old "Газета"
    new "新聞"

    old "Боковина холодильника"
    new "冷蔵庫の側面"

    old "Холодильник"
    new "冷蔵庫"

    old "Штора"
    new "カーテン"

    old "Игрушки"
    new "おもちゃ"

    old "Рисунки"
    new "絵"

    old "Книга"
    new "本"

    old "Мишка"
    new "くまのぬいぐるみ"

    old "Копилка"
    new "貯金箱"

    old "Старшеклассники"
    new "高校生"

    old "Мужчина"
    new "男"

    old "Гнездо"
    new "巣"

    old "Автомобиль"
    new "自動車"

    old "Обувь"
    new "靴"

    old "Ведёрко"
    new "バケツ"

    old "Самолётик"
    new "おもちゃの飛行機"

    old "Повешенный"
    new "吊るされた人"

    old "Шприц"
    new "注射器"

    old "Белка"
    new "リス"

    old "Изучите сцену"
    new "シーンを調べてください"

    old "Проектор"
    new "プロジェクター"

    old "Портреты"
    new "肖像画"

    old "Петарды"
    new "爆竹"

    old "Летов"
    new "レトフ"

    old "Цой"
    new "ツォイ"

    old "Бодров"
    new "ボドロフ"

    old "Трудовик"
    new "技術科の教師"

    old "Подозреваемый"
    new "容疑者"

    old "Ножницы"
    new "はさみ"

    old "Бумага"
    new "紙"

    old "Камень"
    new "石"

    old "Хлам"
    new "がらくた"

    old "Инструменты"
    new "工具"

    old "Полка"
    new "棚"

    old "Тиски"
    new "万力"

    old "Ящики"
    new "箱"

    old "Этап пройден"
    new "ステージクリア"

    old "Камера"
    new "刑務所の独房"

    old "Противогаз"
    new "ガスマスク"

    old "Зеркало"
    new "鏡"

    old "Рога"
    new "角"

    old "Портрет"
    new "肖像画"

    old "Лыжи"
    new "スキー"

    old "Комната"
    new "部屋"

    old "Проигрыватель"
    new "プレーヤー"

    old "Пианино"
    new "ピアノ"

    old "Плакат"
    new "ポスター"

    old "Аквариум"
    new "水槽"

    old "Дом Барби"
    new "バービーハウス"

    old "Награды"
    new "賞"

    old "Музыкальный центр"
    new "ミニコンポ"

    # old "Жулька"
    # new "ジュルカ"

    old "Успех"
    new "成功"

    old "Провал"
    new "失敗"

    old "Достижение"
    new "達成"

    old "Взять крест"
    new "十字架を背負う"

    old "Взять амулет"
    new "お守りを取る"

    old "Приглушить музыку и звуки"
    new "音楽と効果音を下げる"

    old "Произнести последнюю реплику"
    new "最後のセリフを言う"

# translate  achievements
translate english strings:
    old "Настоящий детектив 1"
    new "True Detective 1"

    old "Полезные связи"
    new "Useful Connections"

    old "Где же ты, Вова?"
    new "Where Are You, Vova?"

    old "Беги, спасайся"
    new "Run, Save Yourself"

    old "Чертова кассета"
    new "Damned Cassette"

    old "Небыляндия"
    new "Land of Tall Tales"

    old "Тайное послание"
    new "Secret Message"

    old "Сладость"
    new "Sweetness"

    old "Гадость"
    new "Disgusting Thing"

    old "Настоящий детектив 2"
    new "True Detective 2"

    old "Левый коронный"
    new "Left Hook"

    old "Правый похоронный"
    new "Right Finisher"

    old "Униженный и оскорбленный"
    new "Humiliated and Insulted"

    old "Рыцарь!"
    new "Knight!"

    old "Авантюрист!"
    new "Adventurer!"

    old "Маски-шоу"
    new "Mask Show"

    old "Не фартануло"
    new "No Luck"

    old "Шаман Кинг"
    new "Shaman King"

    old "Скептик"
    new "Skeptic"

    old "Утилизатор"
    new "Disposer"

    old "Рот на замок"
    new "Keep Your Mouth Shut"

    old "Ван Гог"
    new "Van Gogh"

    old "Бяка"
    new "Yucky"

    old "Братик"
    new "Bro"

    old "Команда Вольтрона"
    new "Voltron Team"

    old "Муза"
    new "Muse"

    old "Моя прелесть!"
    new "My Precious!"

    old "Раззява"
    new "Scatterbrain"

    old "О, счастливчик!"
    new "Oh, Lucky One!"

    old "Лопух"
    new "Loser"

    old "Настоящий детектив 3"
    new "True Detective 3"

    old "Дементий!"
    new "Dementor!"

    old "Мистер Хайд"
    new "Mr. Hyde"

    old "Доктор Джекил"
    new "Dr. Jekyll"

    old "Три мушкетера"
    new "Three Musketeers"

    old "Третий лишний"
    new "Third Wheel"

    old "Клубника"
    new "Strawberry"

    old "Фарш"
    new "Minced Meat"

    # old "Школяр-убийца"
    # new "Schoolkiller"

    old "Секретные материалы"
    new "The X-Files"

    old "Выживший"
    new "Survivor"

    old "Дядя Стёпа"
    new "Uncle Styopa"

    old "Настоящий детектив 4"
    new "True Detective 4"

    old "Хромой амур"
    new "Lame Cupid"

    old "Мелодия любви"
    new "Melody of Love"

    old "Смак!"
    new "Delicious!"

    old "Блеванже"
    new "Vomit Feast"

    old "У меня лапки"
    new "I Have Paws"

    old "Аквамен"
    new "Aquaman"

    old "Бард"
    new "Bard"

    old "Панк"
    new "Punk"

    old "Бездарь"
    new "Talentless"

    old "Красная таблетка"
    new "Red Pill"

    old "ЗОЖ"
    new "Healthy Lifestyle"

    old "Синяя таблетка"
    new "Blue Pill"

    old "Натуропатия"
    new "Naturopathy"

    old "Ромео+Джульета"
    new "Romeo + Juliet"

    old "Джентльмен"
    new "Gentleman"

    old "Ходор"
    new "Hodor"

    old "Герасим"
    new "Gerasim"

    old "Доктор Павлов"
    new "Doctor Pavlov"

    old "Любовь"
    new "Love"

    old "Семья"
    new "Family"

    old "Зверь"
    new "Beast"

    old "Человек"
    new "Human"

    old "Вкус предательства"
    new "Taste of Betrayal"

    old "Вкус разлуки"
    new "Taste of Separation"

    old "Вкус утраты"
    new "Taste of Loss"

    old "Хот-дог"
    new "Hot Dog"

    old "Шерлок"
    new "Sherlock"

    old "Не верю!"
    new "I Don't Believe It!"

    old "Язычник"
    new "Pagan"

    old "Экзорцист"
    new "Exorcist"

    old "Звезда Полынь"
    new "Wormwood Star"

    old "Эгоист"
    new "Egoist"

    old "Альтруист"
    new "Altruist"

    old "Путь света"
    new "Path of Light"

    old "Путь тьмы"
    new "Path of Darkness"

    old "Нормис"
    new "Normie"

    old "Сигма бой"
    new "Sigma Boy"

    # old "Апокалипсис сегодня"
    # new "Apocalypse Now"

    old "Погасший свет"
    new "Extinguished Light"

    old "Без лишних глаз"
    new "No Extra Eyes"

    old "Серенький волчок"
    new "Little Grey Wolf"

    old "Воссоединение"
    new "Reunion"

    old "Кровь за кровь"
    new "Blood for Blood"

    old "Адский пикник"
    new "Hellish Picnic"

    old "Дурка зовёт"
    new "The Madhouse Calls"

    old "Чужой"
    new "Alien"

    old "Рататуй"
    new "Ratatouille"

    old "Консерва"
    new "Tin Can"

    old "Цельный Зайчик"
    new "Whole Bunny"

    old "Последний рывок"
    new "Final Dash"

    old "Бег по краю пропасти"
    new "Running on the Edge"

    old "Последний герой"
    new "The Last Hero"

    old "Не брат ты мне..."
    new "You're No Brother of Mine..."

    old "Винтовка - это праздник!"
    new "A Rifle Is a Celebration!"

    old "Вместилище тьмы"
    new "Vessel of Darkness"

    old "Слабо, Davie504?"
    new "Too Weak, Davie504?"

    old "Жулька против"
    new "Zhulka vs"

    old "Настоящий детектив 5"
    new "True Detective 5"

    old "Властелин Ачивок"
    new "Lord of Achievements"

translate chinese strings:
    old "Настоящий детектив 1"
    new "真探1"

    old "Полезные связи"
    new "有用的人脉"

    old "Где же ты, Вова?"
    new "你在哪儿，沃瓦？"

    old "Беги, спасайся"
    new "快跑，逃命"

    old "Чертова кассета"
    new "恶魔磁带"

    old "Небыляндия"
    new "童话国度"

    old "Тайное послание"
    new "秘密信息"

    old "Сладость"
    new "甜蜜"

    old "Гадость"
    new "恶心的东西"

    old "Настоящий детектив 2"
    new "真探2"

    old "Левый коронный"
    new "左勾拳"

    old "Правый похоронный"
    new "右终结拳"

    old "Униженный и оскорбленный"
    new "受辱与侮辱"

    old "Рыцарь!"
    new "骑士！"

    old "Авантюрист!"
    new "冒险家！"

    old "Маски-шоу"
    new "假面秀"

    old "Не фартануло"
    new "运气不好"

    old "Шаман Кинг"
    new "通灵王"

    old "Скептик"
    new "怀疑论者"

    old "Утилизатор"
    new "处理者"

    old "Рот на замок"
    new "守口如瓶"

    old "Ван Гог"
    new "梵高"

    old "Бяка"
    new "讨厌鬼"

    old "Братик"
    new "小兄弟"

    old "Команда Вольтрона"
    new "百兽王战队"

    old "Муза"
    new "缪斯"

    old "Моя прелесть!"
    new "我的宝贝！"

    old "Раззява"
    new "冒失鬼"

    old "О, счастливчик!"
    new "哦，幸运儿！"

    old "Лопух"
    new "傻瓜"

    old "Настоящий детектив 3"
    new "真探3"

    old "Дементий!"
    new "摄魂怪！"

    old "Мистер Хайд"
    new "海德先生"

    old "Доктор Джекил"
    new "杰基尔博士"

    old "Три мушкетера"
    new "三个火枪手"

    old "Третий лишний"
    new "多余的第三者"

    old "Клубника"
    new "草莓"

    old "Фарш"
    new "肉馅"

    # old "Школяр-убийца"
    # new "学生杀手"

    old "Секретные материалы"
    new "X档案"

    old "Выживший"
    new "幸存者"

    old "Дядя Стёпа"
    new "斯佳帕大叔"

    old "Настоящий детектив 4"
    new "真探4"

    old "Хромой амур"
    new "跛脚丘比特"

    old "Мелодия любви"
    new "爱的旋律"

    old "Смак!"
    new "美味！"

    old "Блеванже"
    new "呕吐盛宴"

    old "У меня лапки"
    new "我有爪子"

    old "Аквамен"
    new "海王"

    old "Бард"
    new "吟游诗人"

    old "Панк"
    new "朋克"

    old "Бездарь"
    new "废物"

    old "Красная таблетка"
    new "红色药丸"

    old "ЗОЖ"
    new "健康生活方式"

    old "Синяя таблетка"
    new "蓝色药丸"

    old "Натуропатия"
    new "自然疗法"

    old "Ромео+Джульета"
    new "罗密欧与朱丽叶"

    old "Джентльмен"
    new "绅士"

    old "Ходор"
    new "霍多尔"

    old "Герасим"
    new "格拉西姆"

    old "Доктор Павлов"
    new "巴甫洛夫博士"

    old "Любовь"
    new "爱"

    old "Семья"
    new "家庭"

    old "Зверь"
    new "野兽"

    old "Человек"
    new "人类"

    old "Вкус предательства"
    new "背叛的滋味"

    old "Вкус разлуки"
    new "离别的滋味"

    old "Вкус утраты"
    new "失去的滋味"

    old "Хот-дог"
    new "热狗"

    old "Шерлок"
    new "夏洛克"

    old "Не верю!"
    new "我不相信！"

    old "Язычник"
    new "异教徒"

    old "Экзорцист"
    new "驱魔人"

    old "Звезда Полынь"
    new "苦艾星"

    old "Эгоист"
    new "自私的人"

    old "Альтруист"
    new "利他主义者"

    old "Путь света"
    new "光之路"

    old "Путь тьмы"
    new "黑暗之路"

    old "Нормис"
    new "普通人"

    old "Сигма бой"
    new "西格玛男孩"

    # old "Апокалипсис сегодня"
    # new "现代启示录"

    old "Погасший свет"
    new "熄灭的光"

    old "Без лишних глаз"
    new "没有多余的眼睛"

    old "Серенький волчок"
    new "小灰狼"

    old "Воссоединение"
    new "重逢"

    old "Кровь за кровь"
    new "以血还血"

    old "Адский пикник"
    new "地狱野餐"

    old "Дурка зовёт"
    new "精神病院在召唤"

    old "Чужой"
    new "异形"

    old "Рататуй"
    new "料理鼠王"

    old "Консерва"
    new "罐头"

    old "Цельный Зайчик"
    new "完整的兔子"

    old "Последний рывок"
    new "最后的冲刺"

    old "Бег по краю пропасти"
    new "悬崖边奔跑"

    old "Последний герой"
    new "最后的英雄"

    old "Не брат ты мне..."
    new "你不是我兄弟…"

    old "Винтовка - это праздник!"
    new "步枪就是庆典！"

    old "Вместилище тьмы"
    new "黑暗的容器"

    old "Слабо, Davie504?"
    new "Davie504，怂了吗？"

    old "Жулька против"
    new "茹尔卡对决"

    old "Настоящий детектив 5"
    new "真探5"

    old "Властелин Ачивок"
    new "成就之王"

translate italiano strings:
    old "Настоящий детектив 1"
    new "True Detective 1"

    old "Полезные связи"
    new "Relazioni utili"

    old "Где же ты, Вова?"
    new "Dove sei, Vova?"

    old "Беги, спасайся"
    new "Corri, salvati"

    old "Чертова кассета"
    new "Cassetta demoniaca"

    old "Небыляндия"
    new "Il paese delle favole"

    old "Тайное послание"
    new "Messaggio segreto"

    old "Сладость"
    new "Dolcezza"

    old "Гадость"
    new "Schifezza"

    old "Настоящий детектив 2"
    new "True Detective 2"

    old "Левый коронный"
    new "Gancio sinistro"

    old "Правый похоронный"
    new "Destro mortale"

    old "Униженный и оскорбленный"
    new "Umiliato e offeso"

    old "Рыцарь!"
    new "Cavaliere!"

    old "Авантюрист!"
    new "Avventuriero!"

    old "Маски-шоу"
    new "Spettacolo delle maschere"

    old "Не фартануло"
    new "Niente fortuna"

    old "Шаман Кинг"
    new "Shaman King"

    old "Скептик"
    new "Scettico"

    old "Утилизатор"
    new "Smaltitore"

    old "Рот на замок"
    new "Bocca chiusa"

    old "Ван Гог"
    new "Van Gogh"

    old "Бяка"
    new "Brutto affare"

    old "Братик"
    new "Fratellino"

    old "Команда Вольтрона"
    new "Squadra Voltron"

    old "Муза"
    new "Musa"

    old "Моя прелесть!"
    new "Mio tesoro!"

    old "Раззява"
    new "Sbadatello"

    old "О, счастливчик!"
    new "Oh, fortunato!"

    old "Лопух"
    new "Allocco"

    old "Настоящий детектив 3"
    new "True Detective 3"

    old "Дементий!"
    new "Dissennatore!"

    old "Мистер Хайд"
    new "Mr. Hyde"

    old "Доктор Джекил"
    new "Dr. Jekyll"

    old "Три мушкетера"
    new "I tre moschettieri"

    old "Третий лишний"
    new "Terzo incomodo"

    old "Клубника"
    new "Fragola"

    old "Фарш"
    new "Carne macinata"

    # old "Школяр-убийца"
    # new "Studente assassino"

    old "Секретные материалы"
    new "X-Files"

    old "Выживший"
    new "Sopravvissuto"

    old "Дядя Стёпа"
    new "Zio Styopa"

    old "Настоящий детектив 4"
    new "True Detective 4"

    old "Хромой амур"
    new "Cupido zoppo"

    old "Мелодия любви"
    new "Melodia d'amore"

    old "Смак!"
    new "Che gusto!"

    old "Блеванже"
    new "Festa del vomito"

    old "У меня лапки"
    new "Ho le zampette"

    old "Аквамен"
    new "Aquaman"

    old "Бард"
    new "Bardo"

    old "Панк"
    new "Punk"

    old "Бездарь"
    new "Senza talento"

    old "Красная таблетка"
    new "Pillola rossa"

    old "ЗОЖ"
    new "Stile di vita sano"

    old "Синяя таблетка"
    new "Pillola blu"

    old "Натуропатия"
    new "Naturopatia"

    old "Ромео+Джульета"
    new "Romeo + Giulietta"

    old "Джентльмен"
    new "Gentiluomo"

    old "Ходор"
    new "Hodor"

    old "Герасим"
    new "Gerasim"

    old "Доктор Павлов"
    new "Dottor Pavlov"

    old "Любовь"
    new "Amore"

    old "Семья"
    new "Famiglia"

    old "Зверь"
    new "Bestia"

    old "Человек"
    new "Umano"

    old "Вкус предательства"
    new "Sapore del tradimento"

    old "Вкус разлуки"
    new "Sapore dell'addio"

    old "Вкус утраты"
    new "Sapore della perdita"

    old "Хот-дог"
    new "Hot dog"

    old "Шерлок"
    new "Sherlock"

    old "Не верю!"
    new "Non ci credo!"

    old "Язычник"
    new "Pagano"

    old "Экзорцист"
    new "Esorcista"

    old "Звезда Полынь"
    new "Stella Assenzio"

    old "Эгоист"
    new "Egoista"

    old "Альтруист"
    new "Altruista"

    old "Путь света"
    new "Via della luce"

    old "Путь тьмы"
    new "Via dell'oscurità"

    old "Нормис"
    new "Normie"

    old "Сигма бой"
    new "Ragazzo sigma"

    # old "Апокалипсис сегодня"
    # new "Apocalypse Now"

    old "Погасший свет"
    new "Luce spenta"

    old "Без лишних глаз"
    new "Niente occhi indiscreti"

    old "Серенький волчок"
    new "Lupetto grigio"

    old "Воссоединение"
    new "Riunione"

    old "Кровь за кровь"
    new "Sangue per sangue"

    old "Адский пикник"
    new "Picnic infernale"

    old "Дурка зовёт"
    new "Il manicomio chiama"

    old "Чужой"
    new "Alien"

    old "Рататуй"
    new "Ratatouille"

    old "Консерва"
    new "Scatoletta"

    old "Цельный Зайчик"
    new "Coniglietto intero"

    old "Последний рывок"
    new "Ultimo slancio"

    old "Бег по краю пропасти"
    new "Correre sul bordo"

    old "Последний герой"
    new "L'ultimo eroe"

    old "Не брат ты мне..."
    new "Non sei mio fratello..."

    old "Винтовка - это праздник!"
    new "Il fucile è una festa!"

    old "Вместилище тьмы"
    new "Ricettacolo di oscurità"

    old "Слабо, Davie504?"
    new "Ti manca il coraggio, Davie504?"

    old "Жулька против"
    new "Zhulka contro"

    old "Настоящий детектив 5"
    new "True Detective 5"

    old "Властелин Ачивок"
    new "Signore delle imprese"

translate turkish strings:
    old "Настоящий детектив 1"
    new "Gerçek Dedektif 1"

    old "Полезные связи"
    new "Faydalı bağlantılar"

    old "Где же ты, Вова?"
    new "Neredesin, Vova?"

    old "Беги, спасайся"
    new "Kaç, kendini kurtar"

    old "Чертова кассета"
    new "Şeytan kaseti"

    old "Небыляндия"
    new "Masallar diyarı"

    old "Тайное послание"
    new "Gizli mesaj"

    old "Сладость"
    new "Tatlılık"

    old "Гадость"
    new "İğrençlik"

    old "Настоящий детектив 2"
    new "Gerçek Dedektif 2"

    old "Левый коронный"
    new "Sol kroşe"

    old "Правый похоронный"
    new "Sağ ölümcül darbe"

    old "Униженный и оскорбленный"
    new "Aşağılanmış ve hakarete uğramış"

    old "Рыцарь!"
    new "Şövalye!"

    old "Авантюрист!"
    new "Macera arayıcısı!"

    old "Маски-шоу"
    new "Maske şovu"

    old "Не фартануло"
    new "Şans yoktu"

    old "Шаман Кинг"
    new "Shaman King"

    old "Скептик"
    new "Şüpheci"

    old "Утилизатор"
    new "İmha edici"

    old "Рот на замок"
    new "Ağzını kilitle"

    old "Ван Гог"
    new "Van Gogh"

    old "Бяка"
    new "Iğrenç şey"

    old "Братик"
    new "Kardeşim"

    old "Команда Вольтрона"
    new "Voltron Takımı"

    old "Муза"
    new "İlham perisi"

    old "Моя прелесть!"
    new "Kıymetlim!"

    old "Раззява"
    new "Dalgın"

    old "О, счастливчик!"
    new "Ah, şanslı!"

    old "Лопух"
    new "Saf"

    old "Настоящий детектив 3"
    new "Gerçek Dedektif 3"

    old "Дементий!"
    new "Dementor!"

    old "Мистер Хайд"
    new "Bay Hyde"

    old "Доктор Джекил"
    new "Dr. Jekyll"

    old "Три мушкетера"
    new "Üç Silahşörler"

    old "Третий лишний"
    new "Fazlalık üçüncü"

    old "Клубника"
    new "Çilek"

    old "Фарш"
    new "Kıyma"

    # old "Школяр-убийца"
    # new "Öğrenci katil"

    old "Секретные материалы"
    new "Gizli Dosyalar"

    old "Выживший"
    new "Hayatta kalan"

    old "Дядя Стёпа"
    new "Styopa Amca"

    old "Настоящий детектив 4"
    new "Gerçek Dedektif 4"

    old "Хромой амур"
    new "Topal Cupido"

    old "Мелодия любви"
    new "Aşk melodisi"

    old "Смак!"
    new "Lezzet!"

    old "Блеванже"
    new "Kusmuk ziyafeti"

    old "У меня лапки"
    new "Patiğim var"

    old "Аквамен"
    new "Aquaman"

    old "Бард"
    new "Ozan"

    old "Панк"
    new "Punk"

    old "Бездарь"
    new "Yeteneksiz"

    old "Красная таблетка"
    new "Kırmızı hap"

    old "ЗОЖ"
    new "Sağlıklı yaşam"

    old "Синяя таблетка"
    new "Mavi hap"

    old "Натуропатия"
    new "Natüropati"

    old "Ромео+Джульета"
    new "Romeo + Juliet"

    old "Джентльмен"
    new "Beyefendi"

    old "Ходор"
    new "Hodor"

    old "Герасим"
    new "Gerasim"

    old "Доктор Павлов"
    new "Dr. Pavlov"

    old "Любовь"
    new "Aşk"

    old "Семья"
    new "Aile"

    old "Зверь"
    new "Canavar"

    old "Человек"
    new "İnsan"

    old "Вкус предательства"
    new "İhanetin tadı"

    old "Вкус разлуки"
    new "Ayrılığın tadı"

    old "Вкус утраты"
    new "Kaybın tadı"

    old "Хот-дог"
    new "Sosisli sandviç"

    old "Шерлок"
    new "Sherlock"

    old "Не верю!"
    new "İnanmıyorum!"

    old "Язычник"
    new "Putperest"

    old "Экзорцист"
    new "Şeytan çıkaran"

    old "Звезда Полынь"
    new "Pelin Yıldızı"

    old "Эгоист"
    new "Bencil"

    old "Альтруист"
    new "Özgeci"

    old "Путь света"
    new "Işığın yolu"

    old "Путь тьмы"
    new "Karanlığın yolu"

    old "Нормис"
    new "Normal tip"

    old "Сигма бой"
    new "Sigma çocuk"

    # old "Апокалипсис сегодня"
    # new "Apocalypse Now"

    old "Погасший свет"
    new "Sönmüş ışık"

    old "Без лишних глаз"
    new "Fazla göz yok"

    old "Серенький волчок"
    new "Küçük gri kurt"

    old "Воссоединение"
    new "Yeniden birleşme"

    old "Кровь за кровь"
    new "Kana kan"

    old "Адский пикник"
    new "Cehennem pikniği"

    old "Дурка зовёт"
    new "Tımarhane çağırıyor"

    old "Чужой"
    new "Yaratık"

    old "Рататуй"
    new "Ratatuy"

    old "Консерва"
    new "Konserve"

    old "Цельный Зайчик"
    new "Bütün tavşan"

    old "Последний рывок"
    new "Son atılım"

    old "Бег по краю пропасти"
    new "Uçurum kenarında koşmak"

    old "Последний герой"
    new "Son kahraman"

    old "Не брат ты мне..."
    new "Kardeşim değilsin..."

    old "Винтовка - это праздник!"
    new "Tüfek bayramdır!"

    old "Вместилище тьмы"
    new "Karanlık kabı"

    old "Слабо, Davie504?"
    new "Yok mu cesaretin, Davie504?"

    old "Жулька против"
    new "Zhulka'ya karşı"

    old "Настоящий детектив 5"
    new "Gerçek Dedektif 5"

    old "Властелин Ачивок"
    new "Başarıların efendisi"

translate japan strings:
    old "Настоящий детектив 1"
    new "トゥルー・ディテクティブ1"

    old "Полезные связи"
    new "有益な人脈"

    old "Где же ты, Вова?"
    new "どこだ、ヴォヴァ？"

    old "Беги, спасайся"
    new "逃げろ、助かれ"

    old "Чертова кассета"
    new "悪魔のカセット"

    old "Небыляндия"
    new "おとぎの国"

    old "Тайное послание"
    new "秘密の伝言"

    old "Сладость"
    new "甘さ"

    old "Гадость"
    new "嫌なもの"

    old "Настоящий детектив 2"
    new "トゥルー・ディテクティブ2"

    old "Левый коронный"
    new "左フック"

    old "Правый похоронный"
    new "右の致命打"

    old "Униженный и оскорбленный"
    new "屈辱と侮辱"

    old "Рыцарь!"
    new "騎士！"

    old "Авантюрист!"
    new "冒険者！"

    old "Маски-шоу"
    new "マスクショー"

    old "Не фартануло"
    new "ツイてない"

    old "Шаман Кинг"
    new "シャーマンキング"

    old "Скептик"
    new "懐疑主義者"

    old "Утилизатор"
    new "処分者"

    old "Рот на замок"
    new "口を閉ざせ"

    old "Ван Гог"
    new "ゴッホ"

    old "Бяка"
    new "いやなやつ"

    old "Братик"
    new "弟分"

    old "Команда Вольтрона"
    new "ボルトロンチーム"

    old "Муза"
    new "ミューズ"

    old "Моя прелесть!"
    new "愛しいしと！"

    old "Раззява"
    new "うっかり者"

    old "О, счастливчик!"
    new "おお、幸運なやつ！"

    old "Лопух"
    new "間抜け"

    old "Настоящий детектив 3"
    new "トゥルー・ディテクティブ3"

    old "Дементий!"
    new "ディメンター！"

    old "Мистер Хайд"
    new "ハイド氏"

    old "Доктор Джекил"
    new "ジキル博士"

    old "Три мушкетера"
    new "三銃士"

    old "Третий лишний"
    new "余計な三人目"

    old "Клубника"
    new "いちご"

    old "Фарш"
    new "ひき肉"

    # old "Школяр-убийца"
    # new "学生殺し屋"

    old "Секретные материалы"
    new "Xファイル"

    old "Выживший"
    new "生存者"

    old "Дядя Стёпа"
    new "ステョーパおじさん"

    old "Настоящий детектив 4"
    new "トゥルー・ディテクティブ4"

    old "Хромой амур"
    new "足の不自由なキューピッド"

    old "Мелодия любви"
    new "愛の旋律"

    old "Смак!"
    new "うまい！"

    old "Блеванже"
    new "嘔吐宴"

    old "У меня лапки"
    new "手が使えない"

    old "Аквамен"
    new "アクアマン"

    old "Бард"
    new "吟遊詩人"

    old "Панк"
    new "パンク"

    old "Бездарь"
    new "無能"

    old "Красная таблетка"
    new "赤い薬"

    old "ЗОЖ"
    new "健康的生活"

    old "Синяя таблетка"
    new "青い薬"

    old "Натуропатия"
    new "自然療法"

    old "Ромео+Джульета"
    new "ロミオ＋ジュリエット"

    old "Джентльмен"
    new "紳士"

    old "Ходор"
    new "ホドール"

    old "Герасим"
    new "ゲラシム"

    old "Доктор Павлов"
    new "パブロフ博士"

    old "Любовь"
    new "愛"

    old "Семья"
    new "家族"

    old "Зверь"
    new "獣"

    old "Человек"
    new "人間"

    old "Вкус предательства"
    new "裏切りの味"

    old "Вкус разлуки"
    new "別れの味"

    old "Вкус утраты"
    new "喪失の味"

    old "Хот-дог"
    new "ホットドッグ"

    old "Шерлок"
    new "シャーロック"

    old "Не верю!"
    new "信じない！"

    old "Язычник"
    new "異教徒"

    old "Экзорцист"
    new "エクソシスト"

    old "Звезда Полынь"
    new "ニガヨモギの星"

    old "Эгоист"
    new "利己主義者"

    old "Альтруист"
    new "利他主義者"

    old "Путь света"
    new "光の道"

    old "Путь тьмы"
    new "闇の道"

    old "Нормис"
    new "一般人"

    old "Сигма бой"
    new "シグマ男"

    # old "Апокалипсис сегодня"
    # new "地獄の黙示録"

    old "Погасший свет"
    new "消えた光"

    old "Без лишних глаз"
    new "余計な目なし"

    old "Серенький волчок"
    new "小さな灰色の狼"

    old "Воссоединение"
    new "再会"

    old "Кровь за кровь"
    new "血には血を"

    old "Адский пикник"
    new "地獄のピクニック"

    old "Дурка зовёт"
    new "精神病院が呼んでいる"

    old "Чужой"
    new "エイリアン"

    old "Рататуй"
    new "レミーのおいしいレストラン"

    old "Консерва"
    new "缶詰"

    old "Цельный Зайчик"
    new "まるごとウサギ"

    old "Последний рывок"
    new "最後の突進"

    old "Бег по краю пропасти"
    new "崖っぷちの疾走"

    old "Последний герой"
    new "最後の英雄"

    old "Не брат ты мне..."
    new "お前はもう兄弟じゃない…"

    old "Винтовка - это праздник!"
    new "ライフルは祭りだ！"

    old "Вместилище тьмы"
    new "闇の器"

    old "Слабо, Davie504?"
    new "Davie504、無理か？"

    old "Жулька против"
    new "ジュルカ対"

    old "Настоящий детектив 5"
    new "トゥルー・ディテクティブ5"

    old "Властелин Ачивок"
    new "実績の王"
