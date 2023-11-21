
import re

def GetToken (expression, langStyle):
    words = expression.split(' ')

    tokenList = []

    reservedWords = langStyle

    lastKey = None
    jumpValue = False
    for index, word in enumerate(words):
        # print(str(word))
        if lastKey == 'print' and jumpValue == True:
            if ')' in word:
                jumpValue = False
            continue
        if word[0] == '(':
            word = word[1: ]
        if word[-1:] == ')':
            word = word[:-1]
        key = None

        try:
            key = reservedWords[word]
            tokenList.append(f'<{str(key)}>')
            lastKey = key
            continue
        except:
            wordFunc = word.split('(')[0]
            try:
                key = reservedWords[wordFunc]
                tokenList.append(f'<{str(key)}>')
                lastKey = key
                if key == 'print':
                    jumpValue = True
                continue
            except:
                _ = False

        variableNamePattern = re.compile(r'\b[a-zA-Z]+\b') # variáveis podem ter letras e não podem ter números
        if bool(re.match(variableNamePattern, word)) and word not in reservedWords.keys():
            if word[-2: ] == '++':
                tokenList.append(f'<variable_name>')
                tokenList.append(f'<variable_increment>')
                lastKey = 'variable_increment'
                continue
            elif word[-2: ] == '--':
                tokenList.append(f'<variable_name>')
                tokenList.append(f'<variable_decrease>')
                lastKey = 'variable_decrease'
                continue
            else:
                tokenList.append(f'<variable_name>' if lastKey != 'function' else '<function_name>')
                lastKey = 'variable_name' if lastKey != 'function' else 'function_name'
                continue

        numberPattern = re.compile(r'^[0-9]+(?:\.[0-9]+)?$') # variáveis que possuem numeros e/ou tenham pontos
        if bool(re.match(numberPattern, word)):
            tokenList.append(f'<number>')
            lastKey = 'number'
            continue

        if lastKey == 'function_name':
            varDeclarationPattern = re.compile(r'\(\w+\)') # se a última key identificada é uma function name, verifica se tem parenteses - parâmetro
            if bool(re.match(varDeclarationPattern, word)) and word not in reservedWords.keys():
                tokenList.append(f'<properties_declaration>')
                lastKey = key
                continue

        arrayDeclarationPattern = re.compile(r'\[\w+(,\w+)*\]') # se tiver abertura de colchetes antes e tiver algo depois é array
        if bool(re.match(arrayDeclarationPattern, word)) and word not in reservedWords.keys():
            tokenList.append(f'<array_declaration>')
            lastKey = key
            continue

        tokenList.append(f'<{str(key)}>')
        lastKey = key

    return tokenList