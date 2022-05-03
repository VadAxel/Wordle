import PySimpleGUI as sg
import SwedishWordle
from start_layout import TextChar

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

sg.theme('Dark Blue')

def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100),  disabled_readonly_background_color='gray', border_width=5,  p=1, enable_events=True, disabled=True)

layout = [
    [sg.Text("Wooordle", font='_21')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string1')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string2')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string3')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string4')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string5')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string6')],
    [sg.HorizontalSeparator(color='black')],
    [sg.B('Enter', bind_return_key=True, key='confirm_button')],
    [sg.InputText( key='input_box')],
    [sg.Text('Eller tryck enter', font='_ 15')],
    ]

window = sg.Window("Wordle SE", layout)

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "confirm_button":
    
        gissing = values['input_box']
        answer = game.Guess(gissing)
        window['string'+str(1)].update(str(answer))
        
        

    """window["word_output"].update("Choktorsk")"""

window.close()
