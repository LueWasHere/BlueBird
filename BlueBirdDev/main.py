import lexer
from colorama import Fore

dev = False

tokens = []

while True:
    print(Fore.WHITE, end='')
    inputs = input()
    tokens = lexer.from_input(inputs, dev)
    print(Fore.WHITE, end='')
    #print(tokens) # only used if I need to see the tokens without activating devMode
    if tokens == ['<dev>', '<PREN_LEFT>', '<PREN_RIGHT>']:
        if dev:
            dev = False
        else:
            dev = True
        print(dev)
