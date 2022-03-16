import lexer
import tokenLEX
from colorama import Fore

dev = False

tokens = []

while True:
    print(Fore.WHITE, end='')
    inputs = input()
    tokens = lexer.from_input(inputs, dev)
    print(Fore.WHITE, end='')
    tokens = tokenLEX.globalLex(tokens, dev)
    #print(tokens) # only used if I need to see the tokens without activating devMode
    if dev:
        print('SUP TOKENS: ' + str(tokens))
    if tokens == ['<CALL>', '<dev>']:
        if dev:
            dev = False
        else:
            dev = True
        print(dev)
