import lexer
import tokenLEX
from colorama import Fore

dev = True

tokens = []

while True:
    print(Fore.WHITE, end='')
    inputs = input()
    tokens = lexer.from_input(inputs, dev)
    print(Fore.WHITE, end='')
    tokens = tokenLEX.globalLex(tokens, dev)
    #print(tokens) # only used if I need to see the tokens without activating devMode
    if tokens == ['<dev>', '<PREN_LEFT>', '<PREN_RIGHT>']:
        if dev:
            dev = False
        else:
            dev = True
        print(dev)
