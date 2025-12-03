__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import os
import sys

# Clearing previous line, keeping things tidy.


def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def Refresh():
    os.system('cls')
    print('****************************')
    print('     Mathlete Calculator    ')
    print('----------------------------')
    print('add'' ''|' ' ''Add two numbers')
    print('sub'' ''|'' ' 'Subtract two numbers')
    print('mul'' ''|'' ' 'Multipy two numbers')
    print('div'' ''|'' ' 'Divide two numbers')
    print('----------------------------')

# Check user's input and prevents any misstyping.
# Keeps track of what state it's in, selection or calculation.


def inputValue(message, runningState):
    while True:
        try:
            userInput = input(message).lower()
            if runningState == False:
                if userInput == 'add' or userInput == 'sub' or userInput == 'mul' or userInput == 'div':
                    return userInput
                else:
                    raise ValueError()

            elif runningState == True:
                if type(float(userInput)) == float or type(int(userInput)) == int:
                    return userInput
                else:
                    raise ValueError()
        except ValueError:
            ClearLine()
            print('Incorrect input, try again!')
            continue
        else:
            return userInput


Refresh()  # Clears previous console outputs and displays standard format

# User's first input, with default state
selection = inputValue('Selection >'' ', False)
print('\n')
# User inputs the valuables for A/B
# After calculation, the console is reset and the user can pick new calculations
while True:
    print('Calculating "c" for expression')
    print('\n')
    if selection == 'add':
        print('     a + b = c')
        print('\n')
        a = float(inputValue('a = ', True))
        b = float(inputValue('b = ', True))
        c = a+b
        print('RESULT: ' + str(a) + ' + ' + str(b) + ' = ' + str(c))
        print('\n')
        input('Press Enter to continue...')
        Refresh()
        selection = inputValue('Selection >'' ', False)

    elif selection == 'sub':
        print('     a - b = c')
        print('\n')
        a = float(inputValue('a = ', True))
        b = float(inputValue('b = ', True))
        c = a-b
        print('RESULT: ' + str(a) + ' - ' + str(b) + ' = ' + str(c))
        print('\n')
        input('Press Enter to continue...')
        Refresh()
        selection = inputValue('Selection >'' ', False)

    elif selection == 'mul':
        print('     a * b = c')
        print('\n')
        a = float(inputValue('a = ', True))
        b = float(inputValue('b = ', True))
        c = a*b
        print('RESULT: ' + str(a) + ' * ' + str(b) + ' = ' + str(c))
        print('\n')
        input('Press Enter to continue...')
        Refresh()
        selection = inputValue('Selection >'' ', False)

    elif selection == 'div':
        print('     a / b = c')
        print('\n')
        a = float(inputValue('a = ', True))
        b = float(inputValue('b = ', True))
        if b != 0:
            c = a/b  # Simple if statement to handle ZeroDivisionException
        else:
            c = str('infinite')
        print('RESULT: ' + str(a) + ' / ' + str(b) + ' = ' + str(c))
        print('\n')
        input('Press Enter to continue...')
        Refresh()
        selection = inputValue('Selection >'' ', False)
