import csv
import os
import sys

# Simple defined function to clear terminal
def Clear(): os.system('cls')

# Function to go back one line in terminal and clear it
def ClearLine():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line

# Checks if there are any .csv files in the folder that the PY file is contained
#   then prints them to the terminal.
def Files(__location__):
    Clear()
    files = os.listdir(__location__)
    files_csv = [i for i in files if i.endswith('.csv')]

    for item in files_csv:
        print(item.replace('.csv', ''), end='\n')
    input()
    MainOutput()

# User specifies  what file to load, it's contents get put in a list (defUserList)
def LoadTodo(defUserList, __location__):
    while True:
        try:
            userInput = input('Filename > ')
            ClearLine()
            with open(os.path.join(__location__, userInput+'.csv'), newline='')as f:
                reader = csv.reader(f)
                defUserList = list(reader)
            return defUserList
        except IOError:
            print("Specified file couldn't be found")

# Main print function, we call this to keep the terminal clean
def MainOutput():
    Clear()
    print(29*'*')
    print('{:^29s}'.format('Todoify')) #with format we can tell the terminal to center content according to 29 characters
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

# Prints the contents of defUserList, clean the output from brackets and other special chars in the conversion
def PrintTodo(defUserList):
    Clear()
    for line in defUserList:
        print(str(defUserList.index(line))+' ' + str(line).replace(
            '[', '').replace(']', '').replace("'", '').replace('"', '').replace(',', ''))

# Saves the current list to a new or existing file
#   writes each items as a new line.
def SaveTodo(defUserList, __location__):
    try:
        userInput = input('Specify filename > ')
        ClearLine()
        f = open(userInput+'.csv', 'x')#  'x' hints at creating a file

        with open(userInput+'.csv', 'w') as f: #writes too that file
            for item in defUserList:
                f.write("%s\n" % item)
    except FileExistsError:
        with open(os.path.join(__location__, userInput+'.csv'), 'w') as f: # 'w' writes to an existing file with exact specified location
            for item in defUserList:
                f.write("%s\n" % item)

# The heart of the program, handles the user selections and holds list/file location
# __Location__ is mainly for getting the location of the executed PY-code
def UserSelection(message):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))) #Dir-location of PY-code
    defUserList = [] #Empty list to be allocated with user inputs

    while True:

        userInput = input(message).lower() #only place we use Lower, rest are considered safe for erratic inputs.
        MainOutput()
        if userInput == 'save':
            SaveTodo(defUserList, __location__)

        elif userInput == 'load':
            defUserList = LoadTodo(defUserList, __location__)

        elif userInput == 'files':
            Files(__location__)

        elif userInput == 'add':
            defUserList.append(input('add > ')) #add user input to the bottom of list
            ClearLine()
        elif userInput == 'show':
            PrintTodo(defUserList)
            input()
            MainOutput()
        elif userInput == 'check':
            try:
                PrintTodo(defUserList)
                defUserList[int(input('Index > '))] += ' X' #User marks what line to be considered "done" with an X
                MainOutput()
            except IndexError:
                MainOutput()
                print('Out of range or empty') #If the input is outside the range of list
            except ValueError:
                MainOutput()
                print('Invalid input') #if the input is empty

        elif userInput == 'delete':
            try:
                PrintTodo(defUserList)
                del defUserList[int(input('Index > '))]#removes item/line at inputed index
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
