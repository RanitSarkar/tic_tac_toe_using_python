list=["_","|","_","|","_","_","|","_","|","_","_","|","_","|","_"]
index=0
player1move=[]
move=0
listofmoves=[0,2,4,5,7,9,10,12,14]
movesdone=[]
listofoutput=[[0,7,14],[0,2,4],[5,7,9],[10,12,14],[0,5,10],[2,7,12],[4,9,14],[4,7,10]]
game_on=True


def result_check():
    global list, listofoutput,game_on
    newlist=[]
    for output in listofoutput:
        for dashes in output:
            newlist.append(list[dashes])
        if newlist.count("X")==3:
            game_on=False
            print ("\n *********** Player1 is winner **********r")
        else:
            newlist.clear()


    for output in listofoutput:
        for dashes in output:
            newlist.append(list[dashes])
        if newlist.count("O")==3:
            game_on = False
            print("\n *********** Player2 is winner **********")
        else:
            newlist.clear()

    if len(listofmoves) == 0:
        game_on=False
        print("\n ********** its a tie *********")
    else:
        pass


def moveavilable(move):
    global listofmoves, movesdone
    legal_move=0
    legal=True
    while legal:
        if move in listofmoves:
            listofmoves.remove(move)
            legal_move = move
            legal=False
            movesdone.append(move)
        else:
            move=int(input(f"\n enter your move in bettween \n 0 | 2 | 4 \n 5 | 7 | 9 \n 10 | 12 | 14 \n --->"))
    return legal_move


def show():
    global index
    index=0
    for _ in range(0,15):
        if index==5 or index==10:
            print("\n")
            print(list[index], end="")
            index += 1
        else:
            print(list[index],end="")
            index += 1


def player1():
    global player1move, move, listofmoves
    move=int(input(f"\n player1 enter your move in bettween \n 0 | 2 | 4 \n 5 | 7 | 9 \n 10 | 12 | 14 \n --->"))
    list[moveavilable(move)]="X"
    move = 0
    show()
    result_check()


def player2():
    global player1move, move
    move = int(input(f"\n player2 enter your move in bettween \n 0 | 2 | 4 \n 5 | 7 | 9 \n 10 | 12 | 14 \n ---> "))
    if move in player1move:
        move = 0
        player2()
    else:
        list[moveavilable(move)] = "O"
        show()
        result_check()


while game_on:
    player1()
    if game_on==True:
        player2()
    else:
        pass
