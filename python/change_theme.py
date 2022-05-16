import PySimpleGUI as sg
from layout import layout_func

def change_theme(window, window_theme):
    while True:
        event, values = window_theme.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Ändra tema':
            event, values = sg.Window('Ändra tema',[[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(), sg.Cancel()]]).read(close=True)
                    
                    #Startar make_window_theme funktionen med valt tema
            if event == 'OK':
                window_theme.close()                                   
                window.close()
                sg.theme(values['-THEME LIST-'])
                window = sg.Window("Wordle SE", layout_func(), finalize=True)
    return window,event