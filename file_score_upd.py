def file_score_upd(score):
    file = open("score.txt", "a")   #Öppnar filen score.txt, skriver
    file.write(str(score)+"\n")
    file.close()

