import random
class Values:
    LetterVal1 = ["a","e","i","o","u","l","n","r","s","t"]
    LetterVal2 = ["d","g"]
    LetterVal3 = ["b","c","m","p"]
    LetterVal4 = ["f","h","v","w","y"]
    LetterVal5 = ["k"]
    LetterVal8 = ["j","x"]
    LetterVal10 = ["q","z"]
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def FindLetterValue():
    letter = input("Please enter a letter: ")
    match letter:
        case letter if letter in Values.LetterVal1:
            print("This value is worth one point")
            ValueLetter=1
        case letter if letter in Values.LetterVal2:
            print("This value is worth two point")
            ValueLetter=2
        case letter if letter in Values.LetterVal3:
            print("This value is worth three point")
            ValueLetter=3
        case letter if letter in Values.LetterVal4:
            print("This value is worth four point")
            ValueLetter=4
        case letter if letter in Values.LetterVal5:
            print("This value is worth five point")
            ValueLetter=5
        case letter if letter in Values.LetterVal8:
            print("This value is worth eight point")
            ValueLetter=8
        case letter if letter in Values.LetterVal10:
            print("This value is worth ten point")
            ValueLetter=10
        case _:
            print("Letter does not qualify")
def FindWordValue(Word):
    Word = list(Word)
    ValueLetter = 0
    for letter in Word:
        match letter:
            case letter if letter in Values.LetterVal1:
                ValueLetter=ValueLetter+1
            case letter if letter in Values.LetterVal2:
                ValueLetter=ValueLetter+2
            case letter if letter in Values.LetterVal3:
                ValueLetter=ValueLetter+3
            case letter if letter in Values.LetterVal4:
                ValueLetter=ValueLetter+4
            case letter if letter in Values.LetterVal5:
                ValueLetter=ValueLetter+5
            case letter if letter in Values.LetterVal8:
                ValueLetter=ValueLetter+8
            case letter if letter in Values.LetterVal10:
                ValueLetter=ValueLetter+10
            case _:
                print("Word does not qualify")
    return ValueLetter
def GetRandomLetters():
    RandomLetters = random.sample(Alphabet, 7)
    print("Your letters are",str(RandomLetters)+"\nEnter the best word you can make up from these letters")
    return RandomLetters
def PlayGame():
    P1Turns = 0
    P1Score = 0
    P2Turns = 0
    P2Score = 0
    P1Name = input("Player 1 what is your name?\n")
    P2Name = input("Player 2 What is your name?\n")
    Player = 1
    RandomLetters = GetRandomLetters()
    while P1Turns != 3 and P2Turns != 3:
        Word = input()
        for letter in Word:
            if letter in RandomLetters:
                Score = FindWordValue(Word)
            else:
                print("This word has letters not from the list")
        if Player == 1:
            P1Score = P1Score + Score
            print("This word is worth",str(Score),"points")
        else:
            P2Score = P2Score + Score
            print("This word is worth",str(Score),"points")
        if Player == 1:
            P1Turns = P1Turns+1
            print("Player 2, Your turn")
            Player = 2
        else:
            P2Turns = P2Turns+1
            
            print("Player 1, your turn")
            Player = 1
    print("End of turns")
    if P1Score > P2Score:
        print("Player 1 has", str(P1Score),"Points")
        print("Player 2 has", str(P2Score),"Points")
        print("Player 1 win")
    elif P2Score > P1Score:
        print("Player 1 has", str(P1Score),"Points")
        print("Player 2 has", str(P2Score),"Points")
        print("Player 2 win")
    else:
        print("Player 1 has", str(P1Score),"Points")
        print("Player 2 has", str(P2Score),"Points")
        print("Draw")        
def main():
    print("SCRABBLE \nEnter 1 to get the value of a scrabble letter\nEnter 2 to get value of a scrabble word\nEnter 3 to play a game\nEnter 4 to quit")
    while True:
        Option = input(">>> ")
        if Option == "1":
            FindLetterValue()
        elif Option == "2":
            Word = input()
            ValueLetter = FindWordValue(Word)
            print("This word is worth",str(ValueLetter),"points")
        elif Option == "3":
            PlayGame()
        elif Option == "4":
            print("Bye")
            break
        else:
            print("Invalid option, try again")
main()
