import random

board = [] # initialise board array
empty_board = [] # initialise empty board that will only change when a hit sinks a ship or misses
p1_board = []
level = 1
hits = 0
turns = 0

player_one = True
ai_player = False

def main():
    print("----------Battleships-----------\nPress any key to play")
    key_press_menu = input(">>> ")
    setup_board()
    display_board()
    player_turn(player_one)

def setup_board():
    global board
    global empty_board
    global p1_board
    global level
    global ai_player
    for i in range(10):
        board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        empty_board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]) 
        p1_board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        # empty board to be displayed so the user has to play the game properly
    while True:
        level = input("Enter a level (1-3) or type P for procedural generation: ")
        if level == 1 or level == 2 or level == 3:
            try:
                level = int(level) # checks if level can be turned to an int
                if level < 1 or level > 3:
                    print("Invalid value entered, try again")
                else:
                    break
            except:
                print("Invalid data type entered, please try again")
        elif level.upper() == "P":
            print("Procedural Generation")
            for i in range(4): # different letter each time the for loop cycles
                letter_val = (i % 4) + 1  
                if letter_val == 1:
                    letter = "A"
                elif letter_val == 2:
                    letter = "B"
                elif letter_val == 3:
                    letter = "C"
                elif letter_val == 4:
                    letter = "S"
                place_ship(random.randint(3,5), letter)
            break
        else:
            print("Invalid option entered, please try again")
    while True:
        ai_option = input("Do you want to play with another player or AI? Enter P for player and AI for AI: ")
        if ai_option.upper() == "P":
            ai_option == False
            break
        elif ai_option.upper() == "AI":
            ai_option == True
            break
        else:
            print("Invalid option, please try again")

    if level == 1:
        count = 0
        for i in range(5):
            board[3][3+count] = "A"
            count = count+1
        count = 0
        for i in range(4):
            board[2+count][1] = "B"
            count = count+1
        count = 0
        for i in range(3):
            board[7+count][5] = "S"
            count = count+1
        count = 0
        for i in range(3):
            board[6][7+count] = "C"
            count = count+1
    
    elif level == 2:
        count = 0
        for i in range(5):
            board[5+count][0] = "A"
            count = count+1
        count = 0
        for i in range(4):
            board[7][2+count] = "B"
            count = count+1
        count = 0
        for i in range(3):
            board[6][3+count] = "S"
            count = count+1
        count = 0
        for i in range(3):
            board[1+count][9] = "C"
            count = count+1
    
    elif level == 3:
        count = 0
        for i in range(5):
            board[2+count][8] = "A"
            count = count+1
        count = 0
        for i in range(4):
            board[4+count][3] = "B"
            count = count+1
        count = 0
        for i in range(3):
            board[4][5+count] = "S"
            count = count+1
        count = 0
        for i in range(3):
            board[3+count][4] = "C"
            count = count+1
    
    input_ship()

def display_board():
    print("  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(board): 
        # gets the number of each array and assigns it to the variable number
        print(number, " | ".join(row))
        print("   -+---+---+---+---+---+---+---+---+-")
    print("Player's board\n")
    for number, row in enumerate(p1_board): 
        # gets the number of each array and assigns it to the variable number
        print(number, " | ".join(row))
        print("   -+---+---+---+---+---+---+---+---+-")
        
def player_turn(player_one):
    global hits
    global turns
    while game_over != True:
        while True: # infinite while loop that breaks when correct data type entered
            str_col = input("Please enter a column (0-9): ")
            try:
                int_col = int(str_col)
                if int_col < 0 or int_col > 10:
                    print("Invalid value entered, please try again")
                else:
                    break
            except:
                print("Invalid data type entered, please try again")
        while True: # infinite while loop that breaks when correct data type entered
            str_row = int(input("Please enter a row (0-9): "))
            try:
                int_row = int(str_row)
                if int_row < 0 or int_row > 10:
                    print("Invalid value entered, please try again")
                else:
                    break
            except:
                print("Invalid data type entered, please try again")
        if board[int_col][int_row] == "A" or board[int_col][int_row] == "B" or \
        board[int_col][int_row] == "C" or board[int_col][int_row] == "S":
            print("Hit")
            board[int_col][int_row] = "*" # changed so you can't hit the same ship twice
            empty_board[int_col][int_row] = "*" # changed so you can see you've hit that ship
            hits+=1
            turns+=1
        else:
            print("Miss")
            board[int_col][int_row] = "." # changed so you can't miss the same ship twice
            empty_board[int_col][int_row] = "." # changed so you can see you've missed that ship
            turns+=1
        display_board()

        if game_over():
            print("Game over as number of turns has exceeded")
            exit()

        if has_won():
            print("Game over as player won")
            exit()

def has_won():
    global hits
    if hits == 15:
        return True
    else:
        return False

def game_over():
    global turns
    if turns == 20:
        return True
    else:
        return False

def place_ship(ship_length, ship_letter):
    col_pos = random.randint(0,9) # random column position
    row_pos = random.randint(0,9) # random row position
    axis_pos = random.randint(0,1) # 0 is horizontal 1 is vertical
    while True: # check empty spaces
        if board[col_pos][row_pos] != "-":
            col_pos = random.randint(0,9)
            row_pos = random.randint(0,9)
        else:
            break
    if axis_pos == 0: # horizontal
        while True:
            if col_pos + ship_length > 10:
                col_pos = random.randint(0,9)
                row_pos = random.randint(0,9)
            else:
                break
        for i in range(ship_length):
            if board[col_pos][row_pos] != "-":
                board[col_pos+i][row_pos] = ship_letter
    elif axis_pos == 1: # vertical
        while True:
            if row_pos + ship_length > 10:
                col_pos = random.randint(0,9)
                row_pos = random.randint(0,9)
            else:
                break
        for i in range(ship_length):
            board[col_pos][row_pos+i] = ship_letter

def input_ship():
    display_board()
    print("Please enter ship co-ordinates for your board")
    while True:
        col_pos = input("Enter a column position (0-9): ")
        row_pos = input("Enter a row position (0-9): ")
        axis_pos = input("Enter an axis position (0 for horizontal, 1 for vertical): ")
        ship_length = input("Enter the length of your ship (Between numbers 3 and 5): ")
        try:
            col_pos = int(col_pos)
            row_pos = int(row_pos)
            axis_pos = int(axis_pos)
            ship_length = int(ship_length)
            if ship_length < 3 or ship_length > 5:
                break
        except:
            print("One or more invalid data type entered, please try again")
    while True: # check empty spaces
        if board[col_pos][row_pos] != "-":
            print("Position already taken, please try again")
            col_pos = input("Enter a column position (0-9): ")
            row_pos = input("Enter a row position (0-9): ")
        else:
            break
    if axis_pos == 0: # horizontal
        while True:
            if col_pos + ship_length > 10:
                print("Ship's length exceeds the size of the board, please try again")
                col_pos = input("Enter a column position (0-9): ")
                row_pos = input("Enter a row position (0-9): ")
            else:
                break
        for i in range(ship_length):
            if board[col_pos][row_pos] != "-":
                board[col_pos+i][row_pos] = ship_letter
    elif axis_pos == 1: # vertical
        while True:
            if row_pos + ship_length > 10:
                print("Ship's length exceeds the size of the board, please try again")
                col_pos = input("Enter a column position (0-9): ")
                row_pos = input("Enter a row position (0-9): ")
            else:
                break
        for i in range(ship_length):
            board[col_pos][row_pos+i] = ship_letter
 

main()
