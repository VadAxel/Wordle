import os
def file_score_upd(score):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'txt/score.txt')
    file = open(filename, "a")   #Öppnar filen score.txt
    file.write(str(score)+"\n")     #Skriver i filen
    file.close()                    #Stänger filen

