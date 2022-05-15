def file_score_upd(score):

    file = open("score.txt", "a")   #Öppnar filen score.txt
    file.write(str(score)+"\n")     #Skriver i filen
    file.close()                    #Stänger filen

