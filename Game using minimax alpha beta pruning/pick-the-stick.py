import random
import time
from collections import deque

def evaluate(numofsticks, ismax):
    if ismax and numofsticks is 1:
        return -10
    elif not ismax and numofsticks is 1:
        return 10
    elif ismax and numofsticks < 1:
        return 1000
    elif not ismax and numofsticks < 1:
        return -1000

def minimax(tree, ismax, numofsticks, alpha, beta):
    # print(f'minmax called number of stciks {numofsticks}, max = {ismax}, tree = {tree}')
    if numofsticks <= 1:
        score = evaluate(numofsticks, ismax)
        tree.pop()
        return score

    if ismax:
        best = -1000
        for stick in [1, 2, 3]:
            tree.append(stick)
            numofsticks -= stick
            val = minimax(tree, not ismax, numofsticks, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            numofsticks += stick

            if beta <= alpha:
                break
        # print(f' best score = {best}, number of stick used in this step {sticks}')
        return best

    else:
        best = 1000
        for stick in [1, 2, 3]:
            tree.append(stick)
            numofsticks -= stick
            val = minimax(tree, not ismax, numofsticks, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            numofsticks += stick

            if beta <= alpha:
                break
        # print(f' best score = {best}, number of stick used in this step {sticks}')
        return best

def findbestmove(tree, numofsticks):
    bestVal = -1000
    bestMove = 0

    if numofsticks is 4:
        return 3
    if numofsticks is 3:
        return 2
    if numofsticks is 2:
        return 1

    for stick in [1, 2, 3]:
        # print(stick)
        numofsticks -= stick

        moveVal = minimax(tree, False, numofsticks, -1000, 1000)

        if moveVal > bestVal:
            bestMove = stick
            bestVal = moveVal

    return bestMove


def twoPlayerGame(numOfSticks):
    print("Get ready for the Toss...")
    turn = random.choice([0, 1])
    time.sleep(2)
    print(f"Player{turn%2 + 1}, won the toss and will go first")

    while numOfSticks > 0:
        print(f'\nPlayer{turn%2 + 1}\'s turn')
        pickSticks = int(input("Pick-the-Stick: "))

        if not 1 <= pickSticks <= 3:
            print("Invalid choice, Pick Again...")
            continue

        numOfSticks -= pickSticks
        print(f'Player{turn%2 + 1} takes {pickSticks} sticks, {numOfSticks} sticks remaining')
        if numOfSticks is 1:
            break
        turn += 1

    print("\n\n")
    print(f'Congratulations!!, Player{turn % 2 + 1}: You Won')
    turn -= 1
    print(f'Player{turn % 2 + 1} has to take the final stick and loses, Better luck next time!!\n\n')
    return

def compHumanGame(numOfSticks):
    print("Get ready for the Toss...")
    dic = {0: "Human", 1: "AI"}
    turn = random.choice([0, 1])
    time.sleep(2)
    print(f"{dic[turn]}, won the toss and will go first")

    tree = deque()
    while numOfSticks > 0:
        print(f'\n{dic[turn%2]}\'s turn')

        if turn%2:
            pickSticks = findbestmove(tree, numOfSticks)
            numOfSticks -= pickSticks
            time.sleep(1)

        else:
            pickSticks = int(input("Pick-the-Stick: "))

            if not 1 <= pickSticks <= 3:
                print("Invalid choice, Pick Again...")
                continue

            numOfSticks -= pickSticks

        print(f'{dic[turn%2]} takes {pickSticks} sticks, {numOfSticks} sticks remaining')
        if numOfSticks is 1:
            break
        turn += 1

    print("\n\n")
    print(f'Congratulations!!, {dic[turn%2]}: You Won')
    turn -= 1
    print(f'{dic[turn%2]} has to take the final stick and loses, Better luck next time!!\n\n')
    return


def compCompGame(numOfSticks):

    print("Get ready for the Toss...")
    turn = random.choice([0, 1])
    time.sleep(2)
    print(f"AI-{turn % 2 + 1}, won the toss and will go first")

    tree = deque()
    while numOfSticks > 0:
        print(f'\nAI{turn % 2 + 1}\'s turn')
        pickSticks = findbestmove(tree, numOfSticks)
        numOfSticks -= pickSticks
        time.sleep(2)
        print(f'AI-{turn % 2 + 1} takes {pickSticks} sticks, {numOfSticks} sticks remaining')
        if numOfSticks is 1:
            break
        turn += 1

    print("\n\n")
    print(f'Congratulations!!, AI{turn % 2 + 1}: You Won')
    turn -= 1
    print(f'AI-{turn % 2 + 1} has to take the final stick and loses, Better luck next time!!\n\n')
    return

def rules():
    print("The rules of the game are as follows:")
    print("-> It is a 2-player game.")
    print("-> Each player picks up sticks alternatively.")
    print("-> On their turn, Each player has to pick at least 1 stick and at most 3 sticks")
    print("-> The one who has to pick the final stick will be the loser.")
    print("-> First turn will be randomly decided with toss.")


if __name__ == '__main__':
    exit_game = False
    repeat = True
    numOfSticks = 0

    print("Welcome to PICK-THE-STICK :D")
    while not exit_game:

        if not repeat:
            quit()

        print("Menu:")
        print("(1) Human1 vs Human2\n(2) AI vs Human\n(3) AI-1 vs AI-2\n(4) Rules\n(5) Exit")
        choice = int(input("Enter your choice: "))

        if(choice is not 4 and choice is not 5):
            print("Number number of sticks?")
            print("-> 14\n-> 21\n-> 53")
            numOfSticks = int(input())

        if choice is 1:
            twoPlayerGame(numOfSticks)

        elif choice is 2:
            compHumanGame(numOfSticks)

        elif choice is 3:
            compCompGame(numOfSticks)

        elif choice is 4:
            rules()

        elif choice is 5:
            exit_game = True

        if choice is not 4 and choice is not 5:
            print("Play Again?\nYes/No")
            repeat = input()
            repeat.lower()
            if repeat == "yes":
                repeat = True
            elif repeat == "no":
                repeat = False

    quit()
