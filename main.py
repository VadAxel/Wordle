import SwedishWordle
import wordleGUI

#Skapa ett nytt wordlespel med ord som är 5 långa
wordleGUI.game = SwedishWordle.Game(5)

#Starta GUI
wordleGUI.wordle_func()
