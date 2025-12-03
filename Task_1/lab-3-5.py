__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"


class person:
    def __init__(self):
        self.__name = ''
        self.__gender = ''
        self.__haircolor = ''
        self.__eyecolor = ''

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setgender(self, gender):
        self.__gender = gender

    def getgender(self):
        return self.__gender

    def sethaircolor(self, haircolor):
        self.__haircolor = haircolor

    def gethaircolor(self):
        return self.__haircolor

    def seteyecolor(self, eyecolor):
        self.__eyecolor = eyecolor

    def geteyecolor(self):
        return self.__eyecolor

    name = property(getname, setname)
    gender = property(getgender, setgender)
    haircolor = property(gethaircolor, sethaircolor)
    eyecolor = property(geteyecolor, seteyecolor)


celebrity = []
celebrity.append(person())
celebrity[0].name = 'Daniel Radcliffe'
celebrity[0].gender = 'man'
celebrity[0].haircolor = 'brun'
celebrity[0].eyecolor = 'brun'

celebrity.append(person())
celebrity[1].name = 'Rupert Grint'
celebrity[1].gender = 'man'
celebrity[1].haircolor = 'röd'
celebrity[1].eyecolor = 'blå'

celebrity.append(person())
celebrity[2].name = 'Emma Watson'
celebrity[2].gender = 'kvinna'
celebrity[2].haircolor = 'brun'
celebrity[2].eyecolor = 'brun'

celebrity.append(person())
celebrity[3].name = 'Selena Gomez'
celebrity[3].gender = 'kvinna'
celebrity[3].haircolor = 'brun'
celebrity[3].eyecolor = 'brun'

celebrity.append(person())
celebrity[4].name = 'Sean Bean'
celebrity[4].gender = 'man'
celebrity[4].haircolor = 'brun'
celebrity[4].eyecolor = 'grön'

celebrity.append(person())
celebrity[5].name = 'Anna Kendrick'
celebrity[5].gender = 'kvinna'
celebrity[5].haircolor = 'brun'
celebrity[5].eyecolor = 'blå'

celebrity.append(person())
celebrity[6].name = 'Claire Forlani'
celebrity[6].gender = 'kvinna'
celebrity[6].haircolor = 'brun'
celebrity[6].eyecolor = 'blå'

celebrity.append(person())
celebrity[7].name = 'Anthony Hopkins'
celebrity[7].gender = 'man'
celebrity[7].haircolor = 'grå'
celebrity[7].eyecolor = 'blå'

celebrity.append(person())
celebrity[8].name = 'Amy Poehler'
celebrity[8].gender = 'kvinna'
celebrity[8].haircolor = 'blond'
celebrity[8].eyecolor = 'blå'


def inputString(message):
    while True:
        try:
            userInput = str(input(message))
            if userInput.isdigit():
                raise ValueError()
        except ValueError:
            print('Inmatning är ej korrekt, välj antingen kvinna  eller man')
            continue
        else:
            return userInput
        break


user = person()
user.name = 'defUser'
user.gender = inputString('Ange kön: ')
user.haircolor = inputString('Ange hårfärg: ')
user.eyecolor = inputString('Ange ögonfärg ')
print('-----')

matchedCelebs = ''

for actor in celebrity:
    i = 0
    index = 0
    userIndex = 0
    for trait, value in actor.__dict__.items():
        for userTrait, userValue in user.__dict__.items():
            if userValue == value and index == userIndex:
                i += 1
            userIndex += 1
        userIndex = 0
        index += 1
    if i == 3:
        matchedCelebs += actor.name + ' '
    else:
        i = 0

if matchedCelebs != '':
    print('Egenskaper matchar med: ' + matchedCelebs)
else:
    print('Inga matchningar hittades!')

input()
