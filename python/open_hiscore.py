def open_hiscore():

    top_3 = ""                          #definierar top_3
    file = open("C:/Users/axel/Desktop/Prog1/VT Slutprojekt/txt/score.txt", "r")       #Öppnar
    readthefile = file.readlines()      #Läser
    sortedData = sorted(readthefile)    #Sorterar, lägst till störst
    
    for line in range(3):               #Väljer de tre lägsta värdena
        top_list = str("Pos\tPoints\n" + str(line+1)+"\t"+str(sortedData[line])) #Gör till en string
        top_3 = top_3 + top_list        #uppdaterar top_3

    return top_3                        #Returnerar top_3
