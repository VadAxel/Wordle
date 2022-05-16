def file_score_upd(score):

    file = open("C:/Users/axel/Desktop/Prog1/VT Slutprojekt/txt/score.txt", "a")   #Öppnar filen score.txt
    file.write(str(score)+"\n")     #Skriver i filen
    file.close()                    #Stänger filen

