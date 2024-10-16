board = [
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-",], ["-", "-", "-"], ["-", "-", "-"]]   
    ],
    [  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-",], ["-", "-", "-"], ["-", "-", "-"]]   
    ],
    [  # Layer 2
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-",], ["-", "-", "-"], ["-", "-", "-"]]   
    ]
]
playerOne = True
Turns = 0
wins = 0
filename = 'XOSquaredWinRecord.txt'

def dictFile(filename): # opens the file as a dictionary
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            dict[key] = value
        return dict

WinRecord = dictFile(filename)

def displayBoard(board):
    for layer in range(3):
        for row in range(3):
            print("   ".join(" ".join(board[layer][grid][row]) for grid in range(3)))
        print()  # separate layers with a blank line



def Turn(Turns, playerOne):
    if playerOne:
        print("Player 1 (X)'s turn!\n")
    else:
        print("Player 2 (O)'s turn!\n")
    
    while True:
            layerInput = input("Enter a layer ")
            gridInput = input("Enter a grid ")
            rowInput = input("Enter a row ")
            columnInput = input("Enter a column ")
            try: # checks that the data entered is an integer otherwise asks the user to re enter it
                layerInput = int(layerInput)
                gridInput = int(gridInput)
                rowInput = int(rowInput)
                columnInput = int(columnInput)
                try: # checks that the row and column are in the range of the array or asks you to re enter
                    board[layerInput][gridInput][rowInput][columnInput]
                    break # break the infinite while loop allowing the program to continue as the data entered is valid
                except:
                    print("Invalid row or column entered, try again")
            except:
                print("One or more invalid values entered")
                
    if board[layerInput][gridInput][rowInput][columnInput] != "-": # checks if the position inputted by the user already contains an x or o
        print("Position already taken")
    else:
        if playerOne == True:
            board[layerInput][gridInput][rowInput][columnInput] = "x"
            playerOne = False
        elif playerOne == False:
            board[layerInput][gridInput][rowInput][columnInput] = "o"
            playerOne = True

    Turns +=1 # increments turn
    displayBoard(board)
    
    if isWin(wins):
        if playerOne:
            print("\nPlayer 2 (O) wins!")
            if len(WinRecord) == 0: # checks dictionaries length is empty
                WinRecord.update({0: "Player 2 Win"}) # writes to the record that this was a player 2 win to key 0
            else:
                WinRecord.update({len(WinRecord): "Player 2 Win"}) # writes to the record that this was a player 2 win
            with open(filename, 'w') as f:  
                for key, value in WinRecord.items():  
                    f.write('%s:%s\n' % (key, value))
        # no file written to if the game is a draw
        else:
            print("\nPlayer 1 (X) wins!")
            if len(WinRecord) == 0: # checks dictionaries length is empty
                WinRecord.update({0: "Player 1 Win"}) # writes to the record that this was a player 1 win to the key 0
            else:
                WinRecord.update({len(WinRecord): "Player 1 Win"}) # writes to the record that this was a player 1 win
            with open(filename, 'w') as f:  
                for key, value in WinRecord.items():  
                    f.write('%s:%s\n' % (key, value))
        f.close() # closes the file
        playAgain(Turns, playerOne)
    
    return Turns, playerOne

def isWin(wins):
    for layer in range(3):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != "-": # checks if any row is not equal to an empty space
                if wins !=3:
                    wins=wins+1
                else:
                    return True
        
        for column in range(3):
            if board[0][column] == board[1][column] == board[2][column] and board[0][column] != "-":
                if wins !=3:
                    wins=wins+1
                else:
                    return True
        
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
            if wins !=3:
                    wins=wins+1
            else:
                return True
        
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
            if wins !=3:
                wins=wins+1
            else:
                return True
        
        return False

def main(Turns, playerOne):
    print("-------Noughts and Crosses Squared-------\n")
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper() == "R":
        with open(filename, "r") as f:
            for line in f:
                print(line)
    displayBoard(board)
    while True:
        Turns, playerOne = Turn(Turns, playerOne)

    playAgain(Turns, playerOne)

def playAgain(Turns, playerOne):
    global board

    Again = input("Would you like to play again? Type Y or N ")
    if Again.upper() == "Y":
        playerOne = True
        displayBoard()
    elif Again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        print("Invalid data entered, please try again")

main(Turns, playerOne)
