def checkwin(row,tempGroup):
    
    CrossWin = 0
    CircleWin = 0
    for block in tempGroup:
        if block.data ==1:
            CrossWin+=1
        if block.data ==2:
            CircleWin +=1
        if CrossWin ==3:
            print("Cross Wins")
        if CircleWin ==3 :
            print("Circle Wins")


#checkWin Basic need more improvements