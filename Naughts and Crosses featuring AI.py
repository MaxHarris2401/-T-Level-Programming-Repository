import random

board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] # empty naughts and crosses board
playerOne = True # sets the condition for player one to play first
Turns = 0

filename = 'XOWinRecord.txt'

f = open(filename, "a") # opens the file to check if it exists, it will create it
f.close()

def dictFile(filename): # opens the file as a dictionary
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            dict[key] = value
        return dict

filename = 'XOWinRecord.txt'
WinRecord = dictFile(filename)

def displayBoard():
    for row in board:
        print(" ".join(row)) # gets rid of the square brackets and quotations in the array
def blockPlayer(): # function for AI to predict player moves in attempt to block
    for row in range(3): 
        if board[row].count("x") == 2 and board[row].count("-") == 1: # checks if row has 2 consecutive xs
            return row, board[row].index("-") 
    
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if column.count("x") == 2 and column.count("-") == 1:
            return column.index("-"), col 
 
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    
    if diagonal1.count("x") == 2 and diagonal1.count("-") == 1:
        index = diagonal1.index("-") 
        return index, index
    
    if diagonal2.count("x") == 2 and diagonal2.count("-") == 1:
        index = diagonal2.index("-") 
        return index, 2 - index
    
    return None

def tryWin(): # function for AI to predict player moves in attempt to block
    for row in range(3): 
        if board[row].count("o") == 2 and board[row].count("-") == 1: # checks if row has 2 consecutive xs
            return row, board[row].index("-") 
    
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if column.count("o") == 2 and column.count("-") == 1:
            return column.index("-"), col 
 
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    
    if diagonal1.count("o") == 2 and diagonal1.count("-") == 1:
        index = diagonal1.index("-") 
        return index, index
    
    if diagonal2.count("o") == 2 and diagonal2.count("-") == 1:
        index = diagonal2.index("-") 
        return index, 2 - index
    
    return None
    
def Turn(Turns, playerOne, AI):
    
    if playerOne == True:
        print("Player 1 (X)'s turn!\n")
    elif playerOne == False:
        if AI == True:
            print("AI Player is thinking of Move...\n")
        else:
            print("Player 2 (O)'s turn!\n")
    else:
        print("Draw")
    if AI == True: # if player set mode is AI
        while True:
            if playerOne == True:
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
            else:
                move = tryWin() # attempt to win first
                if move:
                    rowInput, columnInput = move
                else:
                    move = blockPlayer() # try to block player
                    if move:
                        rowInput, columnInput = move
                    else: # random position
                        columnInput = random.randint(0,2)
                        rowInput = random.randint(0,2)
                if board[rowInput][columnInput] != "-":
                    print("Invalid")
                else:
                    break
    elif AI == False: # 2 player mode
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
    
    if isWin():
        if playerOne:
            print("\nPlayer 2 (O) wins!")
            if len(WinRecord) == 0: # checks dictionaries length is empty
                WinRecord.update({0: "Player 2 Win"}) # writes to the record that this was a player 2 win to key 0
            else:
                WinRecord.update({len(WinRecord): "Player 2 Win"}) # writes to the record that this was a player 2 win
            with open("XOWinRecord.txt", 'w') as f:  
                for key, value in WinRecord.items():  
                    f.write('%s:%s\n' % (key, value))
        # no file written to if the game is a draw
        else:
            print("\nPlayer 1 (X) wins!")
            if len(WinRecord) == 0: # checks dictionaries length is empty
                WinRecord.update({0: "Player 1 Win"}) # writes to the record that this was a player 1 win to the key 0
            else:
                WinRecord.update({len(WinRecord): "Player 1 Win"}) # writes to the record that this was a player 1 win
            with open("XOWinRecord.txt", 'w') as f:  
                for key, value in WinRecord.items():  
                    f.write('%s:%s\n' % (key, value))
        f.close() # closes the file
        playAgain(Turns, playerOne)
    else:
        print("It was a Draw!")
        if len(WinRecord) == 0: # checks dictionaries length is empty
            WinRecord.update({0: "Draw"}) # writes to the record that this was a player 1 win to the key 0
        else:
            WinRecord.update({len(WinRecord): "Draw"}) # writes to the record that this was a player 1 win
        with open("XOWinRecord.txt", 'w') as f:  
            for key, value in WinRecord.items():  
                f.write('%s:%s\n' % (key, value))
        f.close() # closes the file
        playAgain(Turns, playerOne)
    
    return Turns, playerOne

def isWin():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-": # checks if any row is not equal to an empty space
            return True # somebody won
    
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != "-":
            return True # somebody won
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True # somebody won
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-": 
        return True # somebody won
    
    return False

def main(Turns, playerOne):
    print("-------Noughts and Crosses-------\n") #title screen
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper() == "R":
        f = open("XOWinRecord.txt", "r") # opens the file to be read
        for lines in f: # print all the lines in the record
            print(lines)
        f.close() # close file
    while True:
        players = input("Would you like to play with 2 people or with AI? Type 2 for 2 player and AI for the AI\n>>> ")
        if players.upper() == "AI":
            AI = True
            break
        elif players == "2":
            AI = False
            break
        else:
            print("Invalid Option entered, please try again\n")
    displayBoard()
    while Turns != 9: # turns repeat 9 times as there are 9 board spaces
        Turns, playerOne = Turn(Turns, playerOne, AI)

    
    playAgain(Turns, playerOne) # asks user to play again

def playAgain(Turns, playerOne):
    global board
    board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] # resets the board

    Again = input("Would you like to play again? Type Y or N ") # up to the user to start a new game
    
    if Again.upper() == "Y":
        playerOne = True # restarts the game from player one
        displayBoard()
        while Turns != 9:
            Turns, playerOne = Turn(Turns, playerOne, AI)
    elif Again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        
        print("Invalid data entered, please try again")
main(Turns, playerOne)