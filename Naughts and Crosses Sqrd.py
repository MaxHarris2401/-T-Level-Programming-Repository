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
displayBoard()