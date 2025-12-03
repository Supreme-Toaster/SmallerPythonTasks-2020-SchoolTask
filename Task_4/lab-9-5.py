__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import os


def Clear(): os.system('cls')


def ContentOutput(cars):
    print(' - '+'\n - '.join(map(str,  cars)))


def MenuOutput(cars):
    Clear()
    print('  .: STACKMATER v1.33.7 :.  ')
    print('-'*28)
    ContentOutput(cars)
    print('-'*28)
    print('{:^28s}'.format('| MENU |'))
    print('-'*28)
    print('push | Push element to stack')
    print('pull | Pull element to stack')
    print('exit | Exit program')
    print('-'*28)


def EvalInput(message):
    while True:
        try:
            userInput = (input(message))
            if userInput.isdigit():
                raise ValueError()
        except ValueError:
            print('Inmatning är ej korrekt, försök igen...')
            continue
        else:
            return userInput


cars = ['Mercedes', 'Volvo', 'Toyota']
MenuOutput(cars)

while True:
    userInput = EvalInput('MENU > ').lower()
    if userInput == 'push':
        cars.append(EvalInput('> '))
        MenuOutput(cars)
    elif userInput == 'pull':
        if cars:
            cars.pop()
        MenuOutput(cars)
    elif userInput == 'exit':
        os._exit(1)
