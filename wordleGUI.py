import PySimpleGUI as sg
import SwedishWordle
from file_score_upd import file_score_upd
from open_hiscore import open_hiscore
from layout import layout_func
from layout import layout2_func

#high score, snyggt uppdelat för A/L

#skapa ett nytt wordlespel med ord som är 5 långa
game = SwedishWordle.Game(5)


def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100), border_width=5,  p=1, enable_events=True, disabled=True)

#importerar layout för wordleGUI
layout = layout_func()

#Definierar top_3 mha funktionen
top_3 = open_hiscore() 

def score_update_visual(score, window):
    window['yiscore'].update(score)
    window['High_Score'].update((top_3))

def make_window_theme(theme=None):
    if theme:
        score = 0 #Score på varje enskilt game
        i = 1 #Ta bort, kanske använda "game"/L
        sg.theme(theme)
        window = sg.Window("Wordle SE", layout, finalize=True)
        while True:
            event, values = window.read()
            guess = values['input_box']

                #Om ogiltigt ord
            if len(guess) != 5 and i <=5 and event == "confirm_button":
                window['string'+str(i)].update("Felaktig längd på ord. Du gissade " + guess + ". Detta spel är om ord som är 5 i längd")
                continue 
              
                #Vid korrekt svar
            elif sum(game.Guess(guess)) == 0:
                window['string'+str(6)].update("Knasvinst län")
                score_update_visual(score, window)      

                #om programmet klickas utan att ha vunnit
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
    else:
        #Layout2 definieras
        layout2 = layout2_func()

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

main_theme()