from ast import Str
from colorama import Fore

# dev messages
thismess = ['"Full token list: "', '"Generating unknown... "', '"Unknown finished! "']
# ops
ops = ['=', '/', '+', '-', '*', '$', '%', '^', '&', '|', '\\', '#', '!', '@', '(', ')', '{', '}', '[', ']', ':', ';', '<', '>', '?', ',', '.', '"', "'"]
opsTk = ['<EQUALS>', '<DIV>', '<PLUS>', '<MINUS>','<MULTIPLY>','<VAR_INCLUDE>','<PERCENT>','<POWER_BY>','<AND>','<OR>','<BACKSLASH>','<POUND>','<MACRO>','<CALL>','<PREN_LEFT>','<PREN_RIGHT>','<CPREN_LEFT>','<CPREN_RIGHT>','<SQPREN_LEFT>','<SQPREN_RIGHT>','<COLON>','<END_LINE>','<LESS_THAN>','<GREATER_THAN>','<QUERY>','<COMMA>','<PERIOD>', '<STR_MARK>', '<CHR_MARK']
# token array
tokens = []
# token counting
countT = 0
# unknown ops
unknown = ''

alpha = []

after = ''

intCheck = []

for i in range(0, 9):
    intCheck.append(str(i))

def unknownMakeFunc(devMode, chars):
    global after
    global thismess
    global tokens
    global ops
    global opsTk
    global countT
    global unknown
    global after
    
    for i in range(0, len(ops)):
        if chars in intCheck:
            countT = ''
            break
        if chars == ' ':
            countT = '<SPACER>'
            break
        if chars == ops[i]:
            countT = i
            break
        if i == len(tokens)-1 and len(unknown) == 0:
            countT = '<FAIL>'
        elif len(unknown) > 0:
            countT = '<>'
    if devMode and type(countT) == int:
        print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + opsTk[countT] + Fore.WHITE)
    # print dev but only if countT is a str not int
    if devMode and countT == '<FAIL>':
        print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + countT + Fore.WHITE)
    if type(countT) == int:
        after = opsTk[countT]
    elif not countT == '<>':
        after = countT

    countT = f'<{unknown}>'
    if devMode:
        print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Unknown op created! {unknown}')

for i in range(52):
    if i >= 26:
        i += 6
    alpha.append(chr(i+65))
    #print(chr(i+65))

def from_input(inputS, devMode):
    global thismess
    global tokens
    global ops
    global opsTk
    global countT
    global unknown
    global after
    
    # token array
    tokens = []
    # token counting
    countT = 0
    # unknown ops
    unknown = ''
    
    after = ''

    unicount = 0
    
    # find single char tokens
    for chars in inputS:
        if chars in intCheck:
            print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'INT creation: {chars}')
            tokens.append(['<INT>', chars])
        unicount += 1
        if chars in alpha:
            unknown += chars
            if devMode:
                print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Unknown op creation... {chars}:{unknown}')
        if chars in ops and len(unknown) > 0:
            unknownMakeFunc(devMode, chars)
            #print('1')
        elif chars in ops and unicount == len(inputS) and len(unknown) > 0:
            unknownMakeFunc(devMode, chars)
            #print('2')
        elif chars == ' ' and len(unknown) > 0:
            unknownMakeFunc(devMode, chars)
            #print('3')
        elif unicount == len(inputS) and len(unknown) > 0:
            unknownMakeFunc(devMode, chars)
            #print('4')
        
        if countT != f'<{unknown}>':
            for i in range(0, len(ops)):
                if chars in intCheck:
                    countT = ''
                    break
                if chars == ' ':
                    countT = '<SPACER>'
                    break
                if chars == ops[i]:
                    countT = i
                    break
                if i == len(tokens)-1 and len(unknown) == 0:
                    countT = '<FAIL>'
                elif len(unknown) > 0:
                    countT = '<>'
        # print dev related things
        if devMode and type(countT) == int:
            print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + opsTk[countT] + Fore.WHITE)
        # print dev but only if countT is a str not int
        if devMode and countT == '<FAIL>':
            print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + countT + Fore.WHITE)
        if devMode and countT == '<>':
            print(Fore.GREEN + '[DEV] ' + Fore.CYAN + f'[MSG]: {thismess[1]} ' + Fore.WHITE)
        if devMode and countT == f'<{unknown}>':
            #print('I just appended:', unknown)
            print(Fore.GREEN + '[DEV] ' + Fore.CYAN + f'[MSG]: {thismess[2]} ' + Fore.WHITE)
            tokens.append(f'<{unknown}>')
            if after != '':
                tokens.append(f'{after}')
            countT = ''
            unknown = ''
        elif not devMode and countT == f'<{unknown}>':
            tokens.append(f'<{unknown}>')
            tokens.append(f'{after}')
            countT = ''
            unknown = ''
        if type(countT) == int and len(str(countT))>0:
            tokens.append(opsTk[countT])
        elif not countT == '<>' and len(countT)>0:
            #print('adding', unknown)
            tokens.append(countT)  
    if devMode: 
        print(Fore.GREEN + '[DEV] ' + Fore.CYAN + f'[MSG]: {thismess[0]} ' + Fore.LIGHTYELLOW_EX, end='')
        for i in range(0,len(tokens)): 
            if not i == len(tokens)-1:
                print(tokens[i], end=', ')
            else:
                print(tokens[i])
        print(Fore.WHITE, end='')
    return tokens
def from_file(inputF, devMode):
    print()
def add_lib(lib_path, devMode):
    print()
