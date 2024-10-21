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
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-",], ["-", "-", "-"], ["-", "-", "-"]]   
    ]
]
player_one = True
turns = 0
filename = 'XOSquaredWinRecord.txt'

f = open(filename, "a") # opens the file to check if it exists, it will create it
f.close()

def dict_file(filename): # opens the file as a dictionary
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            dict[key] = value
        return dict

win_record = dict_file(filename)

def display_board(board):
    for layer in range(3):
        for row in range(3):
            print("   ".join(" ".join(board[layer][grid][row]) for grid in range(3)))
        print()  # separate layers with a blank line

def turn(turns, player_one):
    if player_one:
        print("Player 1 (X)'s turn!\n")
    else:
        print("Player 2 (O)'s turn!\n")
    
    while True:
            layer_input = input("Enter a layer ")
            grid_input = input("Enter a grid ")
            row_input = input("Enter a row ")
            column_input = input("Enter a column ")
            try: # checks that the data entered is an integer otherwise asks the user to re enter it
                layer_input = int(layer_input)
                grid_input = int(grid_input)
                row_input = int(row_input)
                column_input = int(column_input)
                try: # checks that the row and column are in the range of the array or asks you to re enter
                    board[layer_input][grid_input][row_input][column_input]
                    break # break the infinite while loop allowing the program to continue as the data entered is valid
                except:
                    print("Invalid row or column entered, try again")
            except:
                print("One or more invalid values entered")
                
    if board[layer_input][grid_input][row_input][column_input] != "-": # checks if the position inputted by the user already contains an x or o
        print("Position already taken")
    else:
        if player_one == True:
            board[layer_input][grid_input][row_input][column_input] = "x"
            player_one = False
        elif player_one == False:
            board[layer_input][grid_input][row_input][column_input] = "o"
            player_one = True

    turns +=1 # increments turn
    display_board(board)
    
    layer, grid = is_win_small()

    if is_win_small():
        if player_one:
            board[layer][grid] == ["-", " ", "-"], [" ", "-", " "], ["-", " ", "-"]
        else:
            print("chees")
    
    
    
    return turns, player_one

def is_win_small():
    for layer in range(3):
        for grid in range(3):
            for row in board[layer][grid]:
                if row[0] == row[1] == row[2] and row[0] != "-": 
                    # checks if any row is not equal to an empty space
                    return True # somebody won
    
                for column in range(3):
                    if board[layer][grid][0][column] == board[layer][grid][1][column] == board[layer][grid][2][column] and board[layer][grid][0][column] != "-":
                        return True # somebody won

                if board[layer][grid][0][0] == board[layer][grid][1][1] == board[layer][grid][2][2] and board[layer][grid][0][0] != "-":
                    return True # somebody won
                
                if board[layer][grid][0][2] == board[layer][grid][1][1] == board[layer][grid][2][0] and board[layer][grid][0][2] != "-": 
                    return True # somebody won
                
                return False, layer, grid, row, column

def main(turns, player_one):
    print("-------Noughts and Crosses Squared-------\n")
    play = input("Press any key to play or type R to view the win record\n>>> ")
    if play.upper() == "R":
        with open(filename, "r") as f:
            for line in f:
                print(line)
    display_board(board)
    while True:
        turns, player_one = turn(turns, player_one)

    play_again(turns, player_one)

def play_again(turns, player_one):
    global board
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
    [
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],  
        [["-", "-", "-",], ["-", "-", "-"], ["-", "-", "-"]]   
    ]
    ]
    turns = 0
    again = input("Would you like to play again? Type Y or N ")
    if again.upper() == "Y":
        player_one = True
        display_board(board)
    elif again.upper() == "N":
        print("Thank you for playing!!")
        exit()
    else:
        print("Invalid data entered, please try again")

main(turns, player_one)
