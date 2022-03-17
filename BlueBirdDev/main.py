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
    #print(tokens)
    if dev:
        print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + 'Begining super token cunstruction with prim token list')
    print(Fore.WHITE, end='')
    tokens = tokenLEX.globalLex(tokens, dev)
    print(Fore.WHITE, end='')
    #print(tokens) # only used if I need to see the tokens without activating devMode
    if dev:
        print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + 'SUP TOKENS: ' + str(tokens))
    print(Fore.WHITE, end='')
    if tokens == ['<CALL>', '<dev>']:
        if dev:
            dev = False
        else:
            dev = True
        print(dev)
