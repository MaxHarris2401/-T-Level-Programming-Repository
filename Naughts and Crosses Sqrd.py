board = [
    [[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]],
    
    [[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]],
    
    [[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
     [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]]
]

playerOne = True
Turns = 0
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
            # join the rows from all three grids in the current layer
            print("   ".join(" ".join(board[layer][grid][row]) for grid in range(3)))
        print("\n")  # separate layers with a blank line



def Turn(Turns, playerOne):
    
    if playerOne == True:
        print("Player 1 (X)'s turn!\n")
    elif playerOne == False:
        print("Player 2 (O)'s turn!\n")
    else:
        print("Draw")
    while True:
        gridInput = int(input("Enter a grid "))
        rowInput = int(input("Enter a row "))
        columnInput = int(input("Enter a column "))
        if 0 <= gridInput < 3 and 0 <= rowInput < 3 and 0 <= columnInput < 3:
            if board[gridInput][rowInput][columnInput] != "x" or board[gridInput][rowInput][columnInput] != "o":
                if playerOne == True:
                    board[gridInput][rowInput][columnInput] = "x"
                    playerOne = False
                elif playerOne == False:
                    board[gridInput][rowInput][columnInput] = "o"
                    playerOne = True
                Turns += 1
                break
            else:
                print("Position already taken, try again.")
        else:
            print("Invalid grid, row, or column entered, try again.")
                
    displayBoard(board)
    return Turns, playerOne

def main(Turns, playerOne):
    print("-------Noughts and Crosses-------\n")
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper() == "R":
        with open(filename, "r") as f:
            for line in f:
                print(line)
    displayBoard(board)
    while Turns < 9:
        Turns, playerOne = Turn(Turns, playerOne)

    playAgain(Turns, playerOne)

def playAgain(Turns, playerOne):
    global board

    Again = input("Would you like to play again? Type Y or N ")
    if Again.upper() == "Y":
        playerOne = True
        displayBoard()
        while Turns < 9:
            Turns, playerOne = Turn(Turns, playerOne)
    elif Again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        print("Invalid data entered, please try again")

main(Turns, playerOne)
