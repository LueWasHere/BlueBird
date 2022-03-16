from colorama import Fore

def globalLex(tokens, dev):
    tokList = ['<EQUALS>', '<DIV>', '<PLUS>', '<MINUS>','<MULTIPLY>','<VAR_INCLUDE>','<PERCENT>','<POWER_BY>','<AND>','<OR>','<BACKSLASH>','<POUND>','<MACRO>','<CALL>','<PREN_LEFT>','<PREN_RIGHT>','<CPREN_LEFT>','<CPREN_RIGHT>','<SQPREN_LEFT>','<SQPREN_RIGHT>','<COLON>','<END_LINE>','<LESS_THAN>','<GREATER_THAN>','<QUERY>','<COMMA>','<PERIOD>', '<STR_MARK>', '<STR_MARK>', '<SPACER>']

    str = False
    spickUp = 0
    chr = False
    cpickup = 0
    float = False
    fpickup = 0
    line = 0
    i = 0
    buildStr=''
    ntokens = []
    ops = ['=', '/', '+', '-', '*', '$', '%', '^', '&', '|', '\\', '#', '!', '@', '(', ')', '{', '}', '[', ']', ':', ';', '<', '>', '?', ',', '.', '"', "'"]
    
    while i != len(tokens):
        if tokens[i] == '<BACKSLASH>':
            try:
                print()
            except:
                print(Fore.RED)
        if dev:
            print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'On token {tokens[i]} at index {i}' + Fore.WHITE)
        if i == len(tokens) or i > len(tokens):
            if dev:   
                print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Broke at {i}' + Fore.WHITE)
            break
        if tokens[i] == '<STR_MARK>':
            if dev:
                print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Entered str as {str}' + Fore.WHITE)
            if str:
                ntokens.append(['<STR>', buildStr+'"'])
                str = False
                if dev:
                    print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + 'Finished str' + Fore.WHITE)
            elif not str:
                str = True
                if dev:
                    print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + 'Making str' + Fore.WHITE)
        if tokens[i] not in tokList:
            if str:
                if dev:
                    print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Adding token to str pram="is not in the tokList"::::::Str=\'{buildStr}\' + \'{tokens[i]}\'' + Fore.WHITE)
                a=tokens[i].replace('<', '')
                a=a.replace('>', '')
                buildStr += a
        if tokens[i] == '<SPACER>' and str:
            if dev:
                print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Adding token to str pram="is spacer"::::::Str=\'{buildStr}\' + \' \'' + Fore.WHITE)
            buildStr += ' '
        if tokens[i] == '<NLN>' and str:
            if dev:
                print(Fore.RED + 'ERROR' + Fore.WHITE + ': type str cannot contain ' + Fore.BLUE + 'nln')
            exit(1)
        if tokens[i] in tokList and str and not tokens[i] == '<SPACER>':
            if dev:
                print(Fore.GREEN + '[DEV] ' + Fore.LIGHTYELLOW_EX + f'Adding token to str pram="in toklist and str=true"::::::Str=\'{buildStr}\' + \'{ops[int(tokList.index(tokens[i]))]}\'' + Fore.WHITE)
            buildStr += ops[int(tokList.index(tokens[i]))]
        i += 1
    if ntokens == []:
        return tokens
    return ntokens
