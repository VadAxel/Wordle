import os
def open_hiscore():

    top_3 = ""                          #definierar top_3
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'txt/score.txt')
    file = open(filename, "r")       #Öppnar
    readthefile = file.readlines()      #Läser
    sortedData = sorted(readthefile)    #Sorterar, lägst till störst
    
    for line in range(3):               #Väljer de tre lägsta värdena
        top_list = str("Pos\tPoints\n" + str(line+1) + "\t" + str(sortedData[line])) #Gör till en string
        top_3 = top_3 + top_list        #uppdaterar top_3

    return top_3                        #Returnerar top_3