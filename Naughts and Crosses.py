board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] # empty naughts and crosses board
playerOne = True # sets the condition for player one to play first
Turns = 0

def displayBoard():
    for row in board:
        print(" ".join(row)) # gets rid of the square brackets and quotations in the array

def Turn(Turns, playerOne):
    
    if playerOne == True:
        print("Player 1 (X)'s turn!\n")
    else:
        print("Player 2 (O)'s turn!\n")

    while True:
        rowInput = input("Enter a row ")
        columnInput = input("Enter a column ")
        try: # checks that the data entered is an integer otherwise asks the user to re enter it
            rowInput = int(rowInput)
            columnInput = int(columnInput)
            try: # checks that the row and column are in the range of the array or asks you to re enter
                board[rowInput][columnInput]
                break # break the infinite while loop allowing the program to continue as the data entered is valid
            except:
                print("Invalid row or column entered, try again")
        except:
            print("One or more invalid values entered")

    if board[rowInput][columnInput] != "-": # checks if the position inputted by the user already contains an x or o
        print("Position already taken")
    else:
        if playerOne == True:
            board[rowInput][columnInput] = "x"
            playerOne = False
        elif playerOne == False:
            board[rowInput][columnInput] = "o"
            playerOne = True

    Turns +=1 # incriments turn
    displayBoard()
    
    if isWin():
        if playerOne:
            print("\nPlayer 2 (O) wins!")
        else:
            print("\nPlayer 1 (X) wins!")
        playAgain(Turns, playerOne)
    
    return Turns, playerOne

def isWin():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-": # checks if any row is not equal to an empty space
            return True
    
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != "-":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True
    
    return False

def main(Turns, playerOne):
    print("-------Noughts and Crosses-------\n") #title screen
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper == "R":

    displayBoard()
    while Turns != 9: # turns repeat 9 times as there are 9 board spaces
        Turns, playerOne = Turn(Turns, playerOne)
    
    playAgain(Turns, playerOne) # asks user to play again

def playAgain(Turns, playerOne):
    Again = input("Would you like to play again? Type Y or N ") # up to the user to start a new game
    
    if Again.upper() == "Y":
        playerOne = True
        displayBoard()
        while Turns != 9:
            Turns, playerOne = Turn(Turns, playerOne)
    elif Again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        
        print("Invalid data entered, please try again")
main(Turns, playerOne)