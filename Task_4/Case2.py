import os
import sys

os.system('cls')
##################


todo_list = [] 
todo_list.sort()

try:
    f = open('TodoList.txt', 'r')
    for line in f:
        todo_list.append(line.strip())
        f.close()    
except:
    pass 

def menu():
    while True:
        os.system('cls')
        print('***************************')
        print('         Todoify     ')
        print('---------------------------')
        print('list   |List todos')
        print('add    |Add todo')
        print('check  |Check todo')
        print('delete |Delete todo')
        print('---------------------------')
        print('save   |Save todos to file')
        print('load   |Load todos to file')
        print('---------------------------')

        selection = input('Selcetion > ').lower()

        if selection == 'list':
            viewList()
        elif selection == 'add':
            addTodo()
        elif selection == 'check':
            checkTodo()
        elif selection == 'delete':
            removeTodo()
        elif selection == 'save':
            pass
        elif selection == 'load':
           pass
        else:
            print('---------------------------\n')
            print('Error: Unknown command',"'",str(selection),"'")
            print()
            input('Press enter to continue...')
            menu()
            


def viewList():
    print('---------------------------')
    for i in todo_list:
        print('[ ]',i)
    print('---------------------------')
    input('Press enter to continue...')
    menu()

def addTodo():
    print('---------------------------')
    todo = input('Todo description > ')
    todo_list.append(todo)
    print('---------------------------\n')
    print('SUCCESS:', todo, 'added\n')
    saveList()
    input('Press enter to continue...')
    menu()


def checkTodo():
    print('---------------------------')
    for i in todo_list:
        print('[ ]',i)
    print()
    item = input('Choose todo to see status > ')
    if item in todo_list:
        print('SUCESS: Unchecked -> Checked ')
    else:
        print('')    
        input('Press enter to continue...')
        menu()

def removeTodo():
    print('---------------------------')
    for i in todo_list:
        print('[ ]',i)
    print('---------------------------')    
    todo = input('Choose todo from list to remove > ')    
    todo_list.remove(todo)
    print('---------------------------\n')
    print('SUCCESS:', todo, 'removed\n')
    saveList()
    input('Press enter to continue...')
    menu()

def saveList():
    f = open('TodoList.txt', 'w')    
    for item in todo_list:
        f.write(item+'\n')
    f.close()



menu()  



    




















