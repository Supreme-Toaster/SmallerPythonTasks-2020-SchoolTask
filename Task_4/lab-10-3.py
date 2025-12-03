__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import csv
import os
import sys


def Clear(): os.system('cls')


def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def MainOutput():
    Clear()
    print('.: PEOPLES DATABASE :.')
    print(22*'-')
    print('get_id | Get person by ID ')
    print('get_year | Get persons by Year ')
    print('scan_f | List people by FORENAME')
    print('scan_s | List people by SURNAME')
    print('exit | Exit program')
    print(22*'-')


def EvalInput(message, searchType):
    while True:
        try:
            userInput = input(message)
            if userInput == 'get_id':

                ClearLine()
                while True:
                    userInput = input('| ID = ')
                    if userInput.isdigit() and int(userInput) >= 0:
                        return userInput, 0
                    else:
                        MainOutput()
                        print('Inmatning är ej korrekt, försök igen...')

            elif userInput == 'get_year':

                ClearLine()
                while True:
                    userInput = input('| YEAR = ')
                    if userInput.isdigit() and int(userInput) >= 1900:
                        return userInput, 4
                    else:
                        MainOutput()
                        print('Inmatning är ej korrekt, försök igen...')

            elif userInput == 'scan_f':
                ClearLine()
                while True:
                    userInput = input('| Name = ')
                    if userInput.isalpha():
                        return userInput, 1
                    else:
                        MainOutput()
                        print('Inmatning är ej korrekt, försök igen...')

            elif userInput == 'scan_s':
                ClearLine()
                while True:
                    userInput = input('| Name = ')
                    if userInput.isalpha():
                        return userInput, 2
                    else:
                        MainOutput()
                        print('Inmatning är ej korrekt, försök igen...')
            elif userInput == 'exit':
                os._exit(1)
            else:
                raise ValueError()
        except ValueError:
            MainOutput()
            print('Inmatning är ej korrekt, försök igen...')
            continue
        else:
            return userInput, ''


def Search(userInput, list):
    for line in list:
        if str(userInput[0].lower()) == str(line[userInput[1]].lower()):
            print(str(line).replace('[', '').replace(
                ']', '').replace(',', '').replace("'", ' '))
            if userInput[1] == 0:
                return #With ID search we only need one result, end the search early.


MainOutput()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
searchType = ''

with open(os.path.join(__location__, 'database.csv'), newline='')as f:
    reader = csv.reader(f)
    data = list(reader)

while True:
    Search(EvalInput('| > ', searchType), data)
