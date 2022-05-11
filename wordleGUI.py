import PySimpleGUI as sg
import SwedishWordle
from file_score_upd import file_score_upd
from open_hiscore import open_hiscore

#high score, snyggt uppdelat för A/L

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100), border_width=5,  p=1, enable_events=True, disabled=True)

layout = [
    [sg.Text("Wooordle", font='_21')],  
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string1')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string2')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string3')],
    [sg.HorizontalSeparator(color='black')],    #Få kortare, en string/L
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


#Definierar top_3 mha funktionen
top_3 = open_hiscore() 

def make_window_theme(theme=None):
    if theme:
        score = 0 #Score på varje enskilt game
        i = 1 #Ta bort, kanske använda "game"/L
        sg.theme(theme)
        window = sg.Window("Wordle SE", layout, finalize=True)
        while True:
            event, values = window.read()
            guess = values['input_box']
            """
            if event == "darkpurple6_button":
                main_theme()

            elif event == "lightblue_button":
                main_theme()
            
            elif event == "brightcolors_button":
                main_theme()

            elif event == "darkblue":
                main_theme()
            """

            #Om ogiltigt ord
            if len(guess) != 5 and i <=5 and event == "confirm_button":
                window['string'+str(i)].update("Felaktig längd på ord. Du gissade " + guess + ". Detta spel är om ord som är 5 i längd")
                continue    
            
            #Vid korrekt svar
            elif sum(game.Guess(guess)) == 0:
                window['string'+str(6)].update("Knasvinst län")
                score_update_visual(score, window)      
            

            elif sum(game.Guess(guess)) != 0 and event == sg.WIN_CLOSED:
                #värdet 99 ges till den som inte klara spelet, topplista är för de som lyckas
                score = 99
                break
            
            #Vanlig gissning
            elif event == "confirm_button" and i <= 5:           
                
                #Om gränsen för antalet gissningar överskrids, förlorar du
                if i == 5:
                    window['string'+str(6)].update("Choktorsk bram")
                    score_update_visual(score, window)
                
                #Grafisk validering av gissade ordet
                guess_split = guess.split()  #Skall bli funktion
                score = score + sum(game.Guess(guess))
                window['string'+str(i)].update((game.Guess(guess),guess_split))
                score_update_visual(score, window)
                i += 1
            #Om man stänger wordle efter vinst
            elif event == sg.WIN_CLOSED:
                break


            file_score_upd(score)
    layout2 = [[sg.T('Denna ruta representerar valt tema')],
              [sg.Button('Ok'), sg.Button('Ändra tema'), sg.Button('Avsluta')]]

    return sg.Window('Wordle Wizard', layout2)

def score_update_visual(score, window):
    window['yiscore'].update(score)
    window['High_Score'].update((top_3))


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

main_theme()