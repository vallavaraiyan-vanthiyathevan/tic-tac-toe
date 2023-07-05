#FORM THE BOARD

board=["-","-","-",
     "-","-","-",
     "-","-","-"]
turn="X"

#printboard

def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])

winner=None
ct=0
#getinput

def getinput(board):
    inp=int(input("enter a number from 1 to 9:"))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=turn
    else:
        print("enter valid number again")
        getinput(board)
    
#determine win or draw and switch turn

def checkwin(board):
    #horizontal
    if board[0] == board[1]== board[2] and board[0]!= '-':
        return True
    elif board[3] == board[4]== board[5] and board[3]!= '-':
        return True
    elif board[6] == board[7]== board[8] and board[6]!= '-':
        return True
    #vertical
    elif board[0] == board[3]== board[6] and board[6]!= '-':
        return True
    elif board[1] == board[4]== board[7] and board[7]!= '-':
        return True
    elif board[2] == board[5]== board[8] and board[8]!= '-':
        return True
    elif board[0] == board[4]== board[8] and board[8]!= '-':
        return True
    elif board[2] == board[4]== board[6] and board[6]!= '-':
        return True
    else:
        return False
    
     

while winner==None and ct<9:
    getinput(board)
    if checkwin(board)==True:
        winner=turn
        print("The winner is",winner)
        break
    else:
        if turn=="X":
            turn="O"
        else:
            turn="X"
    printboard(board)
    ct+=1
if winner==None:
    print("the match is Drawn")
    
