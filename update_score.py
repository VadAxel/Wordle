
def update_score(score):
    file = open("score.txt", "a")   #Öppnar filen score.txt, skriver
    file.write(str(score)+"\n")
    file.close()
