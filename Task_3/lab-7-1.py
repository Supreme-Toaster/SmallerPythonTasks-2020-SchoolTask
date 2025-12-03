__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import os


class billboard_post:
    def __init__(self):

        self.POST_1 = 'Detta är första posten.'
        self.POST_2 = 'Detta är andra posten.'
        self.POST_3 = 'Detta är tredje posten.'

    def setPOST_1(self, POST_1):
        self.__POST_1 = POST_1

    def getPOST_1(self):
        return self.__POST_1

    def setPOST_2(self, POST_2):
        self.__POST_2 = POST_2

    def getPOST_2(self):
        return self.__POST_2

    def setPOST_3(self, POST_3):
        self.__POST_3 = POST_3

    def getPOST_3(self):
        return self.__POST_3

    POST_1 = property(getPOST_1, setPOST_1)
    POST_2 = property(getPOST_2, setPOST_2)
    POST_3 = property(getPOST_3, setPOST_3)


def Clear(): os.system('cls')


def EditPost(post):
    Clear()
    print('*'*20)
    print(str(post))
    print('-'*20)
    post = input('> ''')
    return post


def PrintPost(post):
    print('*'*20)
    print('P1: ', str(post.POST_1))
    print('P2: ', str(post.POST_2))
    print('P3: ', str(post.POST_3))
    print('-'*20)


post = billboard_post()

userInput = ''

while userInput != 'e':
    Clear()
    print('.: basicBILLBOARD :.')
    PrintPost(post)
    print('c | Ändra post')
    print('e | Stäng program')
    userInput = input('meny >''').lower()
    if userInput == 'c':
        Clear()

        PrintPost(post)
        print('Vilken post vill du ändra?'+'\n' + 'P1,P2 eller P3')
        userInput = input('meny >''').lower()

        if userInput == 'p1':
            post.POST_1 = EditPost(post.POST_1)
        elif userInput == 'p2':
            post.POST_2 = EditPost(post.POST_2)
        elif userInput == 'p3':
            post.POST_3 = EditPost(post.POST_3)
os._exit(1)
