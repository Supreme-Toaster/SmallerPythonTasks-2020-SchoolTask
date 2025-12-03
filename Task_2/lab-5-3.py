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
    stringVal = ('.: MATHLETE v2.0 :.'+'\n' +
                 '-------------------')
    print(stringVal)


def InputValue(message):
    while True:
        try:
            userInput = input(message)

            if userInput.isalpha():
                if userInput.lower() == 'exit':
                    return str(userInput)
                else:
                    raise ValueError()
            else:
                if float(userInput)!=0.0:
                    return float(userInput)
                else: raise ValueError()
        except ValueError:
            ClearLine()
            print('Incorrect number, try again!')
            continue


def Outcome(userNumInputs, userSum):
    if userNumInputs != 0:
        userAverage = userSum/userNumInputs
        output = ('-------------------'+'\n' +
                  'Kardinalitet: ' + str(userNumInputs) + '\n' +
                  'Summa: ' + str(userSum)+'\n' +
                  'Medelvärde: ' + str(userAverage))
        print(output)
        print('\n')
        print('Do you want to make a new calculation? Yes/No')
        if input('>' '').lower() == ('yes'):
            Clear()
            DisplayOutput()
            userNumInputs = 0
            userSum = 0
            return userNumInputs, userSum
        else:
            os._exit(1)
    else:
        print('No inputed data from user!')
        input('Enter to exit...')
        os._exit(1)

Clear()
DisplayOutput()
userNumInputs = 0
userSum = 0

while True:
    userValue = InputValue('> ' '')
    if userValue != 'exit':
        userSum += userValue
        userNumInputs += 1
    else:
        (userNumInputs, userSum) = Outcome(userNumInputs, userSum)
