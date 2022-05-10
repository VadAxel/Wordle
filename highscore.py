

def open_score():
    top_3 = ""
    file = open("score.txt", "r") #Öppnar
    readthefile = file.readlines() #Läser
    sortedData = sorted(readthefile) #Sorterar, lägst till störst
    
    for line in range(3): #Väljer de tre lägsta värdena
        top_list = str("Pos\tPoints\n" + str(line+1)+"\t"+str(sortedData[line]))
        top_3 = top_3 + top_list
    return top_3

top_3 = open_score()
