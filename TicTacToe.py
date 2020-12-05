from random import choice
import sys


br = [
    [1, 4, 7],
    [2, "X", 8],
    [3, 6, 9]
]
freefields = []

print("Welcome to Tic Tac Toe!")
print("You will play against the computer.")
print("To make a move please choose a square by inputing its number")


def displayboard(br):

    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|  ", br[0][0], "   |  ", br[1][0], "   |   ", br[2][0], "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|  ", br[0][1], "   |  ", br[1][1], "   |   ", br[2][1], "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|  ", br[0][2], "   |  ", br[1][2], "   |   ", br[2][2], "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")
    print(makefreefieldslist())

def computermove():
        cmove = choice(freefields)
        for column in range(len(br)):
            for i in range(3):
                if br[column][i] == cmove:
                    br[column][i] = "X"


        makefreefieldslist()
        VictoryFor(br)
        displayboard(br)
        checkdraw()
        entermove()






def entermove():
    move = int(input("Enter your move: "))
    # insert EXCEPT VALUE ERROR WNEM O NUMBERS OR NOT IN RANGE
    for column in range(len(br)):
        for i in range(3):
            if br[column][i] == move:
                br[column][i] = "O"

    makefreefieldslist()
    VictoryFor(br)
    computermove()
    checkdraw()




def makefreefieldslist():
    global freefields
    freefields = []
    for column in range(len(br)):
        for i in range(3):
            if br[column][i] != "X":
                if br[column][i] != "O":
                        freefields.append(br[column][i])


    return sorted(freefields)

def VictoryFor(br):
    displayboard(br)
    checklose()
    checkwin()


def checkwin():
    check = False
    if br[0][0] == "O":
        if br[0][1] == "O":
            if br[0][2] == "O":
                check = True

    if br[0][0] == "O":
        if br[1][0] == "O":
            if br[2][0] == "O":
                check = True

    if br[2][0] == "O":
        if br[2][1] == "O":
            if br[2][2] == "O":
                check = True

    if br[0][2] == "O":
        if br[1][2] == "O":
            if br[2][2] == "O":
                check = True

    if check == True:
        print("You Win!")
        displayboard(br)
        sys.exit()

def checklose():
    check2 = False
    if br[0][0] == "X":
        if br[0][1] == "X":
            if br[0][2] == "X":
                check2 = True

    if br[1][0] == "X":
        if br[1][1] == "X":
            if br[1][2] == "X":
                check2 = True

    if br[0][0] == "X":
        if br[1][0] == "X":
            if br[2][0] == "X":
                check2 = True

    if br[2][0] == "X":
        if br[2][1] == "X":
            if br[2][2] == "X":
                check2 = True

    if br[0][2] == "X":
        if br[1][2] == "X":
            if br[2][2] == "X":
                check2 = True

    if br[0][2] == "X":
        if br[1][2] == "X":
            if br[2][2] == "X":
                check2 = True

    if br[0][2] == "X":
        if br[1][1] == "X":
            if br[2][0] == "X":
                check2 = True

    if check2 == True:
        print("You Lose!")
        sys.exit()

def checkdraw():
    if len(freefields) == []:
        print("The game is draw!")
        sys.exit()



displayboard(br)
entermove()








