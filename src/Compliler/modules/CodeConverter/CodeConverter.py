def CodeConverter (expressionList, langStyle): 

    reservedWords = langStyle
    reservedWordsFixed = { }

    for key in reservedWords.keys():
        reservedWordsFixed[reservedWords[key]] = key

    reservedWords = reservedWordsFixed

    lowCode = []

    identity = 0
    for x in expressionList:
        for k in reservedWords:
            if x == reservedWords[k] and k not in ['start_scope', 'end_scope']:
                print(f'expression: {x}')
                print('Invalid expression!')
                exit()
        exp = x
        exp = exp.replace(reservedWords["return"], 'return')
        exp = exp.replace(reservedWords["equals"], '==')
        exp = exp.replace(reservedWords["allocation"], '=')
        exp = exp.replace(reservedWords["subtract"], '-')
        exp = exp.replace(reservedWords["addition"], '+')
        exp = exp.replace(reservedWords["multiply"], '*')
        exp = exp.replace(reservedWords["division"], '/')
        exp = exp.replace(reservedWords["print"] + '(', 'print(')
        exp = exp.replace(reservedWords["variable"] + ' ', '')
        exp = exp.replace('++', ' += 1')

        if reservedWords["loop"] + ' (' in exp:
            exp = exp.replace(reservedWords["loop"] + ' (', 'for ')
            exp = exp.replace(') ' + reservedWords["start_scope"], ':')
            identity += 1
            lowCode.append(exp + '\n')
            continue

        if reservedWords["function"] + ' ' in exp:
            exp = exp.replace(reservedWords["function"] + ' ', 'def ')
            exp = exp.replace(' '+ reservedWords["start_scope"], ':')
            identity += 1
            lowCode.append(exp + '\n')
            continue

        if reservedWords["if_condition"] + ' (' in exp:
            exp = exp.replace(reservedWords["if_condition"] + ' (', 'if ')
            exp = exp.replace(') ' + reservedWords["start_scope"], ':')
            identity += 1
            lowCode.append(exp + '\n')
            continue
        
        if reservedWords["end_scope"] + ' ' + reservedWords["else_condition"] + ' ' + reservedWords["start_scope"] in exp:
            exp = exp.replace(reservedWords["end_scope"] + ' ' + reservedWords["else_condition"] + ' ' + reservedWords["start_scope"], 'else:')
            lowCode.append(exp + '\n')
            continue

        if reservedWords["end_scope"] == exp:
            exp = exp.replace(reservedWords["end_scope"], '')
            identity -= 1
            continue
            

        lowCode.append(''.join(['\t' for _ in range(identity)]) + exp + '\n')

    # for index, code in enumerate(lowCode):
    #     rCode = code.replace('\n', '')
    #     print(f'{index}: {rCode}')

    return ''.join(lowCode)