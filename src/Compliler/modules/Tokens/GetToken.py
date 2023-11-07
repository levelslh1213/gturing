
import re

def GetToken (expression, langStyle):
    words = expression.split(' ')

    tokenList = []

    reservedWords = langStyle

    lastKey = None
    for index, word in enumerate(words):
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
                continue
            except:
                _ = False

        variableNamePattern = re.compile(r'\b[a-zA-Z]+\b')
        if bool(re.match(variableNamePattern, word)) and word not in reservedWords.keys():
            tokenList.append(f'<variable_name>' if lastKey != 'function' else '<function_name>')
            lastKey = 'variable_name' if lastKey != 'function' else 'function_name'
            continue

        numberPattern = re.compile(r'^[0-9]+(?:\.[0-9]+)?$')
        if bool(re.match(numberPattern, word)):
            tokenList.append(f'<number>')
            lastKey = 'number'
            continue

        if lastKey == 'function_name':
            varDeclarationPattern = re.compile(r'\(\w+\)')
            if bool(re.match(varDeclarationPattern, word)) and word not in reservedWords.keys():
                tokenList.append(f'<properties_declaration>')
                lastKey = key
                continue

        arrayDeclarationPattern = re.compile(r'\[\w+(,\w+)*\]')
        if bool(re.match(arrayDeclarationPattern, word)) and word not in reservedWords.keys():
            tokenList.append(f'<array_declaration>')
            lastKey = key
            continue

        tokenList.append(f'<{str(key)}>')
        lastKey = key

    return tokenList