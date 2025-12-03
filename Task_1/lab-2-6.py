__author__ = "Peter Gulin"
__version__ = "1.0.1"
__email__ = "pgn19001@student.mdh.se", "peter.gulin@hotmail.com"
__status__ = "Student"

import locale
import math


def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if userInput < 0:
                raise ValueError()
        except ValueError:
            print('Inmatning är ej korrekt, försök igen...')
            continue
        else:
            return userInput
        break


print(".: KORVKOLLEN 1.0.1 :.")
print('----------------')
print('Hur många elever vill ha ...')

twoSausages = inputNumber('2 vanliga korvar > ')
threeSausages = inputNumber('3 vanliga korvar > ')
twoVeggieSausages = inputNumber('2 veganska korvar > ')
threeVeggieSausages = inputNumber('3 veganska korvar > ')

sausagePackage = int(math.ceil((2*twoSausages+3*threeSausages)/8))
veggieSausagePackage = int(
    math.ceil((2*twoVeggieSausages+3*threeVeggieSausages)/4))
soda = int(twoSausages+threeSausages+twoVeggieSausages+threeVeggieSausages)

print('----------------')
print('-  INKÖPLISTA  -')
print('----------------')

print('| Vanlig korv: ' + str(sausagePackage))
print('| Vegansk korv: ' + str(veggieSausagePackage))
print('| Dryck: ' + str(soda))

print('----------------')

costValue = math.ceil(float((sausagePackage*20.95) +
                            (veggieSausagePackage * 34.95) + (soda*13.95)))

locale.setlocale(locale.LC_MONETARY, 'sv_SE')

print('| ' + locale.currency(costValue, True))
print('----------------')
print('Enter för att avsluta! ', end='')
input()
