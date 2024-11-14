import random

board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] 
# empty naughts and crosses board
player_one = True 
# sets the condition for player one to play first
turns = 0

filename = 'XOWinRecord.txt'

f = open(filename, "a") 
# opens the file to check if it exists, it will create it
f.close()

def dict_file(filename): 
    # opens the file as a dictionary
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            dict[key] = value
        return dict

win_record = dict_file(filename)

def display_board():
    for row in board:
        print(" ".join(row)) 
        # gets rid of the square brackets and quotations in the array
def block_player(): 
    # function for AI to predict player moves in attempt to block
    for row in range(3): 
        if board[row].count("x") == 2 and board[row].count("-") == 1: 
            # checks if row has 2 consecutive xs
            return row, board[row].index("-") 
    
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]] 
        # checks columns
        if column.count("x") == 2 and column.count("-") == 1:
            return column.index("-"), col 
 
    diagonal_1 = [board[0][0], board[1][1], board[2][2]] 
    # diagonal victories
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]
    
    if diagonal_1.count("x") == 2 and diagonal_1.count("-") == 1: 
        # if 2 diagonals are occupied by x and one is empty it will play that empty space
        index = diagonal_1.index("-") 
        return index, index
    
    if diagonal_2.count("x") == 2 and diagonal_2.count("-") == 1:
        index = diagonal_2.index("-") 
        return index, 2 - index
    
    return None

def try_win(): # function for AI to try to win 3 in a row
    for row in range(3): 
        if board[row].count("o") == 2 and board[row].count("-") == 1: 
            # checks if row has 2 consecutive os
            return row, board[row].index("-") 
    
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]] 
        # checks columns
        if column.count("o") == 2 and column.count("-") == 1:
            return column.index("-"), col 
 
    diagonal_1 = [board[0][0], board[1][1], board[2][2]] 
    # diagonal victories
    diagonal_2 = [board[0][2], board[1][1], board[2][0]] 
    
    if diagonal_1.count("o") == 2 and diagonal_1.count("-") == 1: 
        # if 2 diagonals are occupied by o and one is empty it will play that empty space
        index = diagonal_1.index("-") 
        return index, index
    
    if diagonal_2.count("o") == 2 and diagonal_2.count("-") == 1:
        index = diagonal_2.index("-") 
        return index, 2 - index
    
    return None
    
def turn(turns, player_one, AI):
    
    if player_one == True:
        print("Player 1 (X)'s turn!\n")
    elif player_one == False:
        if AI == True:
            print("AI Player is thinking of Move...\n")
        else:
            print("Player 2 (O)'s turn!\n")
    if AI == True: # if player set mode is AI
        while True:
            if player_one == True:
                row_input = input("Enter a row ")
                column_input = input("Enter a column ")
                try: 
                    # checks that the data entered is an integer otherwise asks the user to re enter it
                    row_input = int(row_input)
                    column_input = int(column_input)
                    try: 
                        # checks that the row and column are in the range of the array or asks you to re enter
                        board[row_input][column_input]
                        break 
                    # break the infinite while loop allowing the program to continue as the data entered is valid
                    except:
                        print("Invalid row or column entered, try again")
                except:
                    print("One or more invalid values entered")
            else:
                move = try_win() # attempt to win first
                if move:
                    row_input, column_input = move
                else:
                    move = block_player() # try to block player
                    if move:
                        row_input, column_input = move
                    else: # random position
                        column_input = random.randint(0,2)
                        row_input = random.randint(0,2)
                if board[row_input][column_input] != "-":
                    print("Invalid")
                else:
                    break
    elif AI == False: # 2 player mode
        while True:
            row_input = input("Enter a row ")
            column_input = input("Enter a column ")
            try: 
                # checks that the data entered is an integer otherwise asks the user to re enter it
                row_input = int(row_input)
                column_input = int(column_input)
                try: 
                    # checks that the row and column are in the range of the array or asks you to re enter
                    board[row_input][column_input]
                    break 
                # break the infinite while loop allowing the program to continue as the data entered is valid
                except:
                    print("Invalid row or column entered, try again")
            except:
                print("One or more invalid values entered")

    if board[row_input][column_input] != "-": 
        # checks if the position inputted by the user already contains an x or o
        print("Position already taken")
    else:
        if player_one == True:
            board[row_input][column_input] = "x"
            player_one = False
        elif player_one == False:
            board[row_input][column_input] = "o"
            player_one = True

    turns +=1 # increments turn
    display_board()
    
    if is_win():
        if player_one:
            print("\nPlayer 2 (O) wins!")
            if len(win_record) == 0: 
                # checks dictionaries length is empty
                win_record.update({0: "Player 2 Win"}) 
                # writes to the record that this was a player 2 win to key 0
            else:
                win_record.update({len(win_record): "Player 2 Win"}) 
                # writes to the record that this was a player 2 win
            with open(filename, 'w') as f:  
                for key, value in win_record.items():  
                    f.write('%s:%s\n' % (key, value))
        # no file written to if the game is a draw
        else:
            print("\nPlayer 1 (X) wins!")
            if len(win_record) == 0: 
                # checks dictionaries length is empty
                win_record.update({0: "Player 1 Win"})
                # writes to the record that this was a player 1 win to the key 0
            else:
                win_record.update({len(win_record): "Player 1 Win"}) 
                # writes to the record that this was a player 1 win
            with open(filename, 'w') as f:  
                for key, value in win_record.items():  
                    f.write('%s:%s\n' % (key, value))
        f.close() # closes the file
        play_again(turns, player_one, AI)
    
    return turns, player_one

def is_win():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-": 
            # checks if any row is not equal to an empty space
            return True # somebody won
    
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != "-":
            return True # somebody won
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True # somebody won
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-": 
        return True # somebody won
    
    return False

def main(turns, player_one):
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
    display_board()
    while turns != 9: 
        # turns repeat 9 times as there are 9 board spaces
        turns, player_one = turn(turns, player_one, AI)

    
    play_again(turns, player_one, AI) 
    # asks user to play again

def play_again(turns, player_one, AI):
    global board
    board = [["-","-","-"],["-","-","-"],["-", "-", "-"]] 
    # resets the board
    turns = 0

    again = input("Would you like to play again? Type Y or N ") 
    # up to the user to start a new game
    
    if again.upper() == "Y":
        player_one = True 
        # restarts the game from player one
        display_board()
        while turns != 9:
            turns, player_one = turn(turns, player_one, AI)
    elif again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        
        print("Invalid data entered, please try again")
main(turns, player_one)