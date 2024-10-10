board = [
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    ],
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    ],
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    ]
]

playerOne = True # sets the condition for player one to play first
Turns = 0

filename = 'XOSquaredWinRecord.txt'

f = open(filename, "a") # opens the file to check if it exists, it will create it
f.close()

def dictFile(filename): # opens the file as a dictionary
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            dict[key] = value
        return dict

WinRecord = dictFile(filename)

def displayBoard():
    for layer in board:
        for row in range(3):  
            print("    ".join(" | ".join(layer[i][row]) for i in range(3)))

def Turn(Turns, playerOne):
    
    if playerOne == True:
        print("Player 1 (X)'s turn!\n")
    elif playerOne == False:
        print("Player 2 (O)'s turn!\n")
    else:
        print("Draw")
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

    Turns +=1 # increments turn
    displayBoard()

def main(Turns, playerOne):
    print("-------Noughts and Crosses-------\n") #title screen
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper() == "R":
        f = open(filename, "r") # opens the file to be read
        for lines in f: # print all the lines in the record
            print(lines)
        f.close() # close file
    displayBoard()
    while Turns != 9: # turns repeat 9 times as there are 9 board spaces
        Turns, playerOne = Turn(Turns, playerOne)

    
    playAgain(Turns, playerOne) # asks user to play again

def playAgain(Turns, playerOne):
    global board
    board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] # resets the board

    Again = input("Would you like to play again? Type Y or N ") # up to the user to start a new game
    
    if Again.upper() == "Y":
        playerOne = True # restarts the game from player one
        displayBoard()
        while Turns != 9:
            Turns, playerOne = Turn(Turns, playerOne)
    elif Again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        print("Invalid data entered, please try again")
main(Turns, playerOne)