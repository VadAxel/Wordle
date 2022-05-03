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
        for i in range(6):
            answer = sg.Print(game.Guess(values['input_box']))
            window["output_box"].update(answer)
        

    """window["word_output"].update("Choktorsk")"""

window.close()

guess1 = game.Guess('mössa')
print(f'Den första gissningen var \"mössa\". Det resulterade i {guess1}. En siffra för varje bokstav i gissningen. 2 är rätt bokstav på rätt plats, 1 bokstaven finns i ordet, 0 bokstaven finns ej med i ordet. ')

guess2 = game.Guess('skylt')
print(f'Den andra gissningen var \"skylt\". Det resulterade i {guess2}.')

print(f'Den har gjort {game.num_guesses} stycken gissningar.')

# det går att starta ett nytt game med, om man så vill, ny ord längd
game.Start_new_game(10)
print(f'Den har gjort {game.num_guesses} stycken gissningar.')

guess3 = game.Guess('överträffa')
print(f'Den första gissningen i andra gamet var \"överträffa\". Det resulterade i {guess3}.')

# det går att hämta och alla ord som är 10 tecken långa
print(f'Det finns {len(game.words_in_game)} ord som är 10 bokstäver. Några av dom är {game.words_in_game[0:14]}')

# det är viktigt att man gissar ett riktigt ord som finns i listan och är rätt längd annars ger spelet ett exception
game.Guess('läderlappen')