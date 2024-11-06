board = [] # initialise board array
level = 1
hits = 0
turns = 0

def main():
    print("----------Battleships-----------\nPress any key to play")
    key_press_menu = input(">>> ")
    setup_board()
    display_board()
    player_turn()

def setup_board():
    global board
    global level
    for i in range(10):
        board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
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


def display_board():
    print("  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(board):
        print("   -+---+---+---+---+---+---+---+---+-")
        print(number, " | ".join(row))
        
def player_turn():
    global hits
    global turns
    while True:
        str_col = input("Please enter a column (0-9): ")
        try:
            int_col = int(str_col)
            if int_col < 0 or int_col > 10:
                print("Invalid value entered, please try again")
            else:
                break
        except:
            print("Invalid data type entered, please try again")
    while True:
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
        board[int_col][int_row] = "*"
        hits+=1
        turns+=1
    else:
        print("Miss")
        board[int_col][int_row] = "."
        turns+=1

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
main()
if game_over():
    print("Game over as number of turns has exceeded")