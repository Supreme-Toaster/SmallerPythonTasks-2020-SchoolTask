import csv
import os
import sys


def Clear(): os.system('cls')


def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def Files(__location__):
    Clear()
    files = os.listdir(__location__)
    files_csv = [i for i in files if i.endswith('.csv')]

    for item in files_csv:
        print(item.replace('.csv', ''), end='\n')
    input()
    MainOutput()


def LoadTodo(defUserList, __location__):
    while True:
        try:
            userInput = input('Filename > ')
            ClearLine()
            with open(os.path.join(__location__, userInput+'.csv'), newline='')as f:
            #with open(userInput+'.csv', newline='')as f:
                reader = csv.reader(f)
                defUserList = list(reader)
            return defUserList
        except IOError:
            print("Specified file couldn't be found")


def MainOutput():
    Clear()
    print(29*'*')
    print('{:^29s}'.format('Todoify'))
    print(29*'-')
    print('files    | List todo-files')
    print('show     | Show todos')
    print('add      | Add todo')
    print('check    | Check todo')
    print('delete   | Delete todo')
    print(29*'-')
    print('save     | Save todos to file')
    print('load     | Load todos to file')
    print('exit     | Save and exit')
    print(29*'-')


def PrintTodo(defUserList):
    Clear()
    for line in defUserList:
        print(str(defUserList.index(line))+' ' + str(line).replace(
            '[', '').replace(']', '').replace("'", '').replace('"', '').replace(',', ''))


def SaveTodo(defUserList, __location__):
    try:
        userInput = input('Specify filename > ')
        ClearLine()
       # f = open(userInput+'.csv', 'x')

        with open(userInput+'.csv', 'x') as f:
            for item in defUserList:
                f.write("%s\n" % item)
    except FileExistsError:
        #with open(os.path.join(__location__, userInput+'.csv'), 'w') as f:
        with open(userInput+'.csv', 'w') as f:
            for item in defUserList:
                f.write("%s\n" % item)


def UserSelection(message):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    defUserList = []

    while True:

        userInput = input(message).lower()
        MainOutput()
        if userInput == 'save':
            SaveTodo(defUserList, __location__)

        elif userInput == 'load':
            defUserList = LoadTodo(defUserList, __location__)

        elif userInput == 'files':
            Files(__location__)

        elif userInput == 'add':
            defUserList.append(input('add > '))
            ClearLine()
        elif userInput == 'show':
            PrintTodo(defUserList)
            input()
            MainOutput()
        elif userInput == 'check':
            try:
                PrintTodo(defUserList)
                defUserList[int(input('Index > '))] += ' X'
                MainOutput()
            except IndexError:
                MainOutput()
                print('Out of range or empty')
            except ValueError:
                MainOutput()
                print('Invalid input')

        elif userInput == 'delete':
            try:
                PrintTodo(defUserList)
                del defUserList[int(input('Index > '))]
                MainOutput()
            except IndexError:
                MainOutput()
                print('Out of range or empty')

            except ValueError:
                MainOutput()
                print('Invalid input')
        elif userInput == 'exit':
            SaveTodo(defUserList, __location__)
            os._exit(1)


MainOutput()
UserSelection(('Selection > '))
