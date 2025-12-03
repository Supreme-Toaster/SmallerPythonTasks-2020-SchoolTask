__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import os
import random
import sys


def Clear(): os.system('cls')


def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def DisplayOutput():
    stringVal = ('.: THE HIGHER LOWER GAME :.'+'\n' +
                 '---------------------------' + '\n' +
                 'Welcome to The Higher Lower' + '\n' +
                 'Game. I will randomize a   ' + '\n' +
                 'number between 0 and 99.   ' + '\n' +
                 'Can you guess it?' + '\n' +
                 '---------------------------')
    print(stringVal)


def InputValue(message):
    while True:
        try:
            userInput = input(message)
            return int(round(float(userInput)))
        except ValueError:
            print('Incorrect input, try again!')
            continue


def RandomGame(userValue, randomValue):
    if userValue > randomValue:
        ClearLine()
        print('It is LOWER than: ' + str(userValue))
        return False
    elif userValue < randomValue:
        ClearLine()
        print('It is HIGHER than: ' + str(userValue))
        return False
    elif userValue == randomValue:
        ClearLine()
        return True


def RandomGenerator():
    randomValue = random.randint(1, 99)
    return randomValue


def Outcome(userInput, userTriesValue):
    gameOutcome = ('---------------------------' + '\n' +
                   str(userInput) + ' is Correct!' + '\n' +
                   'It took you ' + str(userTriesValue) + ' guesses.' + '\n' +
                   'Good Job!' + '\n'+'\n' +
                   'Play again?  :  Yes/No')
    print(gameOutcome)


Clear()
DisplayOutput()
currentRandomValue = RandomGenerator()
userTries = 0


while True:

    userInput = InputValue('Your guess >' '')
    if userTries > 0:
        ClearLine()
    userTries += 1

    if RandomGame(userInput, currentRandomValue) == True:
        Clear()
        Outcome(userInput, userTries)
        if input('>' '').lower() == ('yes'):
            Clear()
            userTries = 0
            currentRandomValue = RandomGenerator()
            DisplayOutput()
        else:
            Clear()
            print('Thanks for playing!')
            input('Enter to exit' '')
            os._exit(1)
