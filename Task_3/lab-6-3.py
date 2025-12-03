__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import os


def Clear(): os.system('cls')


def ContainNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def Palindrome(inputString):
    return inputString == inputString[::-1]


def EvaluateInput(message):
    while True:
        try:
            userInput = input(message).lower().replace(
                " ", "").replace("-", "").replace("_", "")
            reversedUserInput = Palindrome(userInput)

            if ContainNumbers(userInput) == False:
                if userInput == 'exit':
                    os._exit(1)

                elif userInput.strip() == '':
                    raise ValueError

                elif reversedUserInput:
                    print('" '+userInput+' "' ' är ett palindrom', end='')
                    input()
                    Clear()
                else:
                    print('" '+userInput+' "' ' är inte palindrom')
            else:
                raise ValueError

        except ValueError:
            Clear()
            print('Incorrect input, try again!')
            continue
    return


Clear()
EvaluateInput('Ange sträng: ' '')
