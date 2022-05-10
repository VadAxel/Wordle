import PySimpleGUI as sg

layout = [
    [sg.Text("Wooordle", font='_21')], #sg.Text('Teman: ', font='_19'), sg.B('Dark Purple', key='darkpurple6_button'), sg.B('Light Blue', key='lightblue_button'), sg.B('Bright Colors', key='brightcolors_button'), sg.B('Dark Blue', key='darkblue')], 
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string1')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string2')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string3')],
    [sg.HorizontalSeparator(color='black')],    #Få kortare, en string
    [sg.Text('', key='string4')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string5')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string6')],
    [sg.HorizontalSeparator(color='black')],
    [sg.B('Enter', bind_return_key=True, key='confirm_button')],
    [sg.InputText( key='input_box', do_not_clear = False)],
    [sg.Text('Eller tryck enter\nDitt Score: ', font='_ 15')],
    [sg.Text('_____ ', font='_ 15', key = 'yiscore')],
    [sg.Text('Top 3! - High Score: ', font='_ 15')],
    [sg.Text('\n\n\n', font='_ 10', key = 'High_Score')], 
    ]

def make_window_theme(theme=None):
    if theme:
        sg.theme(theme)
        window = sg.Window("Wordle SE", layout, finalize=True)
    layout2 = [[sg.T('Denna ruta representerar valt tema')],
              [sg.Button('Ok'), sg.Button('Ändra tema'), sg.Button('Avsluta')]]

    return sg.Window('Wordle Wizard', layout2)


def main_theme():
    window_theme = make_window_theme()

    while True:
        event, values = window_theme.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Ändra tema':
            event, values = sg.Window('Ändra tema',
                                      [[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(), sg.Cancel()]]
                                      ).read(close=True)
            if event == 'OK':
                window_theme.close()
                window = make_window_theme(values['-THEME LIST-'])

    window.close()