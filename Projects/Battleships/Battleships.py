import random as rng

board = [] # initialise board array
empty_board = [] # initialise empty board that will only change when a hit sinks a ship or misses
level = 1
hits = 0
turns = 0

def main():
    print("----------Battleships-----------\n1. New Game\n2. Help Screen\n3. Quit")
    while True:
        key_press_menu = input(">>> ")
        if key_press_menu == "1":
            setup_board()
            display_board()
            player_turn()
            break
        elif key_press_menu == "2":
            print("To play, select a type of generation to use as the enemy board, between 1-3 or P for procedural generation\nThen, you must guess the position of the enemy ships using the grid (between 0-9 on rows or columns) and try to sink the entirety of the ship's length\nOnce you have taken out all of the 5 enemy ships, you win\nOtherwise, you have 15 turns to win the game and if that number is exceeded the game will be over")
            key_press_help = input("Would you like to continue?\n>>> ")
            main()
        elif key_press_menu == "3":
            while True:
                exit_check = input("Are you sure you want to quit? Type Y or N\n>>> ")
                if exit_check.upper() == "Y":
                    print("Thanks for playing!")
                    exit()
                    break
                    
                elif exit_check.upper() == "N":
                    main()
                    break
                else:
                    print("Invalid option entered, please try again")
            
def setup_board():
    global board
    global empty_board
    global level
    for i in range(10):
        board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        empty_board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]) 
        # empty board to be displayed so the user has to play the game properly
    while True:
        level = input("Enter a level (1-3) or type P for procedural generation: ")
        if level == "1" or level == "2" or level == "3":
            print("Level",level)
            break
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
                place_ship(rng.randint(3,5), letter)
            break
        else:
            print("Invalid option entered, please try again")

    if level == "1":
        for i in range(5):
            board[3][3+i] = "A"
       
        for i in range(4):
            board[2+i][1] = "B"
            
        for i in range(3):
            board[7+i][5] = "S"
        
        for i in range(3):
            board[6][7+i] = "C"
            
    elif level == "2":
        for i in range(5):
            board[5+i][0] = "A"
           
        for i in range(4):
            board[7][2+i] = "B"
         
        for i in range(3):
            board[6][3+i] = "S"
           
        for i in range(3):
            board[1+i][9] = "C"
          
    elif level == "3":
        for i in range(5):
            board[2+i][8] = "A"
          
        for i in range(4):
            board[4+i][3] = "B"
        
        for i in range(3):
            board[4][5+i] = "S"
    
        for i in range(3):
            board[3+i][4] = "C"
        

def display_board():
    print("  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(board): 
        # gets the number of each array and assigns it to the variable number
        print(number, " | ".join(row))
        print("   -+---+---+---+---+---+---+---+---+-")
        
def player_turn():
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
            register = "\033[32mHit\033[0m"
            board[int_col][int_row] = "\033[32m*\033[0m" # red text
            # changed so you can't hit the same ship twice
            empty_board[int_col][int_row] = "\033[32m*\033[0m" 
            # changed so you can see you've hit that ship
            hits+=1
            turns+=1
        elif board[int_col][int_row] == "-":
            register = "\033[31mMiss\033[0m"
            board[int_col][int_row] = "\033[31m.\033[0m" # green text
            # changed so you can't miss the same ship twice
            empty_board[int_col][int_row] = "\033[31m.\033[0m" 
            # changed so you can see you've missed that ship
            turns+=1

        display_board()
        print(register)

        if game_over():
            print("Game over as number of turns has exceeded 15")
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
    while True: # checks the length of ship isn't bigger than the index
        col_pos = rng.randint(0,9) # random column position
        row_pos = rng.randint(0,9) # random row position
        axis_pos = rng.randint(0,1) # 0 is horizontal 1 is vertical
        
        if axis_pos == 0:
            if col_pos + ship_length > 10:
                continue
        else:
            if row_pos + ship_length > 10:
                 continue
            
        can_place = True
        for i in range(ship_length):
            if axis_pos == 0:  # horizontal
                if board[row_pos][col_pos + i] != "-":
                    can_place = False
                    break
            else:  # vertical
                if board[row_pos + i][col_pos] != "-":
                    can_place = False
                    break
        
        if can_place:
            for i in range(ship_length):
                if axis_pos == 0:  # horizontal
                    board[row_pos][col_pos + i] = ship_letter
                else:  # vertical
                    board[row_pos + i][col_pos] = ship_letter
            break  # exit the loop after placing the ship

main()
