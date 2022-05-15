import PySimpleGUI as sg
import SwedishWordle
from file_score_upd import file_score_upd
from open_hiscore import open_hiscore
from layout import layout_func
from layout import layout2_func
from result_text_func import result_text_func

#Skapa ett nytt wordlespel med ord som är 5 långa
game = SwedishWordle.Game(5)

#Definierar grundläggande grafik
def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(10,100), border_width=5,  p=1, enable_events=True, disabled=True)

#Funktion för uppdatering av score, för kompression av kod
def visual_score_update(score, window):
    window['yiscore'].update(score)                                            #Aktuellt score
    window['High_Score'].update((open_hiscore()))                              #High Score

#Hanterar skapandet av fönster
def wordle_func():  
    score = 0                                                                  #Score på varje enskilt game
    i = 1                                                                      #Spelsekvens, veriabel för stegen i spelet. (Ta bort, kanske använda "game"/L)
    sg.theme('Dark blue')                                                      
    window = sg.Window("Wordle SE", layout_func(), finalize=True)
    
    while True:
        
        event, values = window.read()                                          #Inleder, window
        guess = values['input_box']                                            #Input från användare får en variabel
        result = game.Guess(guess)                                             #Result definieras
        text_output = result_text_func(result)                                 #Grafiken för din skrivna text

        #Om ogiltigt ord
        if len(guess) != 5 and i <= 5 and event == "confirm_button":
            window['string'+str(i)].update("Felaktig längd på ord. Du gissade " + guess + ". Detta spel är om ord som är 5 i längd")

        #Inställningar    
        elif event == "settings_button":
            window_theme = sg.Window('Wordle Wizard', layout2_func()) #kanske return sg.Window('Wordle Wizard', layout2_func()) bara
            
            #Funktioner för olika knapptryck för wordle wizard
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
                        
        #Nytt spel
        elif event == "new_game_button":
            window.close()

            #Skapa ett nytt wordlespel med ord som är 5 långa
            SwedishWordle.Game(5)

            #Starta GUI
            wordle_func()

        #Vid korrekt svar
        elif sum(result) == 0:                
            window['string'+str(6)].update("Knasvinst län")                    #Grafik meddelande vinst
            visual_score_update(score, window)                                 #Grafik uppdateas för score      
            file_score_upd(score) 
            
        #Vanlig gissning
        elif event == "confirm_button" and i <= len(result):           
            
            #Om gränsen för antalet gissningar överskrids, förlorar du
            if i == len(result):
                window['string'+str(6)].update("Choktorsk bram")
                visual_score_update(score, window)                              #Grafik uppdateras för score
            
            #Grafisk validering av gissade ordet                                        
            score = score + sum(result)                                         #Score uppdateras
            window['string'+str(i)].update((text_output,guess))                 #Grafik uppdateras för svar
            visual_score_update(score, window)                                  #Grafik uppdateas för score
            i += 1
            
        #Om man stänger wordle
        elif event == sg.WIN_CLOSED:
            window.close()


