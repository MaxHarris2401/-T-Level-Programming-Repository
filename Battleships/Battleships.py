board = [] # initialise board array
level = 1
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

def display_board():
    print("  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(board):
        print("   -+---+---+---+---+---+---+---+---+-")
        print(number, " | ".join(row))
        
def player_turn():
    
main()