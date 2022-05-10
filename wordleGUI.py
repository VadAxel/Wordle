import PySimpleGUI as sg
import SwedishWordle
from file_score_upd import file_score_upd
from open_hiscore import open_hiscore
from score_output import score_output

#from word_eva import answer_list_converter,guess_split   #high score, snyggt uppdelat för A

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

sg.theme('Dark Blue')

def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100),  disabled_readonly_background_color='gray', border_width=5,  p=1, enable_events=True, disabled=True)



""""
def stringlayout():
    for i in range(7):
        [sg.HorizontalSeparator(color='black')],
        [sg.Text('', key='string'+i)],
       
    """ 
layout = [
    
    [sg.Text("Wooordle", font='_21')], 
    [sg.B('Inställningar', key='inställningar_button')],
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
"""
layout2 = [
    
    [sg.Text("Ändra tema", font='_21')],
    [sg.HorizontalSeparator(color='black')],
    [sg.B('Dark Purple', bind_return_key=True, key='darkpurple6_button')], [sg.B('Light Blue', bind_return_key=True, key='lightblue_button')], [sg.B('Bright Colors', bind_return_key=True, key='brightcolors_button')]
   
    
    ]

"""
window = sg.Window("Wordle SE", layout, finalize=True)

#Definierar top_3 mha funktionen
top_3 = open_hiscore() 

#uppdaterar grafiken
def score_update():
    window['yiscore'].update(score)
    window['High_Score'].update((top_3))

score = 0 #Score på varje enskilt game
i = 1 #Ta bort, kanske använda "game"


while True:
    event, values = window.read()
    
    if event == "confirm_button" and i <= 5:
        answer, guess_split = score_output(game, score, values)             
        window['string'+str(i)].update((answer,guess_split))
        score_update()
        i += 1

    elif answer == [0,0,0,0,0]:
        window['string'+str(6)].update("Knasvinst län")
        score_update()
        i += 1
        
    elif answer != [0,0,0,0,0] and event == sg.WIN_CLOSED:
        #värdet 99 ges till den som inte klara spelet, toppliste är för de som lyckas
        score = 99
        break
 
    elif i == 6:
        window['string'+str(6)].update("Choktorsk bram")
        score_update()
    
    elif event == sg.WIN_CLOSED:
        break

    """
    if event == "inställningar_button":
        window_inställningar = sg.Window("Inställningar", layout2, finalize=True)
        """

file_score_upd(score)


window.close()
