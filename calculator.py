#
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termocolor work on Windows to
init()

print( Back.BLACK )

what = input ('что делать? (+,-,*,/): ')

print( Back.YELLOW )

a = float( input ( 'ввведи первое число: ' ))
b = float( input('введи второе число: ' ))

if what == '+':
    c = a + b
    print ('результат: ' + str(c))

elif what == '-':
    c = a - b
    print ('результат: ' + str(c))
elif what == '*':
    c = a * b
    print ('овтет: ' + str(c))
elif what == '/':
    c = a / b
    print ('овтет: ' + str(c))
else: 
    print ('чета ты попутал')

input()