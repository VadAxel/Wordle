import PySimpleGUI as sg
import SwedishWordle
from start_layout import TextChar

#from word_eva import answer_list_converter,guess_split   #high score, snyggt uppdelat för A

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

sg.theme('Dark Blue')

def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100),  disabled_readonly_background_color='gray', border_width=5,  p=1, enable_events=True, disabled=True)
"""
def stringlayout():
    for i in range(7):
        [sg.HorizontalSeparator(color='black')],
        [sg.Text('', key='string'+i)],
        """
layout = [
    
    [sg.Text("Wooordle", font='_21')],
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

window = sg.Window("Wordle SE", layout, finalize=True)

def open_score():
    top_3 = ""
    file = open("score.txt", "r") #Öppnar
    readthefile = file.readlines() #Läser
    sortedData = sorted(readthefile) #Sorterar, lägst till störst
    
    for line in range(3): #Väljer de tre lägsta värdena
        top_list = str("Pos\tPoints\n" + str(line+1)+"\t"+str(sortedData[line]))
        top_3 = top_3 + top_list
    return top_3

top_3 = open_score()

def score_update():
    window['yiscore'].update(score)
    window['High_Score'].update((top_3))



score = 0 #Score på varje enskilt game
i = 1 #Ta bort, kanske använda "game"

while True:
    event, values = window.read()
    
    if event == "confirm_button" and i <= 5:
        guess = values['input_box']
        answer = game.Guess(guess)
        guess_split = guess.split()
        score = score + sum(answer)             
        window['string'+str(i)].update((answer,guess_split))
        score_update()
        i += 1

    elif answer == [0,0,0,0,0]:
        window['string'+str(6)].update("Knasvinst län")
        score_update()
        i += 1
        
    elif answer != [0,0,0,0,0] and event == sg.WIN_CLOSED:
        score = 99
        break
 
    elif i == 6:
        window['string'+str(6)].update("Choktorsk bram")
        score_update()
    
    elif event == sg.WIN_CLOSED:
        break


def file_score_upd(score):
    file = open("score.txt", "a")   #Öppnar filen score.txt, skriver
    file.write(str(score)+"\n")
    file.close()
file_score_upd(score)



window.close()
