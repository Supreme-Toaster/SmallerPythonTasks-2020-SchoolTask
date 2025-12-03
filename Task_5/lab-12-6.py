__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"


import json
import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def Clear(): os.system('cls')


def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def MainPrint(data):
    Clear()
    print('.: ALWAYSNOTE :.')
    print('-- gold edition --')
    print('*'*18)
    for note in data['notes']:
        print('{:^18s}'.format(note['title']))
        print('{:^18s}'.format(note['content'])+'\n')
    print('-'*18)
    print('view | view note')
    print('add  | add note')
    print('rm   | remove note')
    print('exit | exit program')
    print('-'*18)


def LoadData(data):
    try:
        with open(os.path.join(__location__, 'data.txt')) as json_file:
            data = json.load(json_file)

    except FileNotFoundError:
        data = {}
        data['notes'] = []
        with open(os.path.join(__location__, 'data.txt'), 'w') as outfile:
            json.dump(data, outfile)

    return data


def SaveData(data):
    with open(os.path.join(__location__, 'data.txt'), 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)


data = ''
data = LoadData(data)
while True:
    MainPrint(data)
    userInput = input('menu > ').lower()

    if userInput == 'view':
        Clear()
        for note in data['notes']:
            print(note['title'])
            print(note['content']+'\n')
        input('Proceed?')

    elif userInput == 'add':
        data['notes'].append(
            {'title': input('Title > '), 'content': input('Text > ')})
        SaveData(data)
    elif userInput == 'rm':
        Clear()
        i = 0
        for note in data['notes']:
            print(str(i) + ' '+note['title']+' '+note['content'])
            i += 1
        while True:
            try:
                userInput = input('remove > ')
                ClearLine()
                if userInput.isdigit():
                    del data['notes'][int(userInput)]
                    SaveData(data)
                    break
            except ValueError:
                print('Enter a valid input!')
            except IndexError:
                print('Out of range, try again!')
                if len(data):
                    break
    elif userInput == 'exit':
        SaveData(data)
        os._exit(1)
