
def CodeReader (filePath):
    codeLines = None
    with open(f'{filePath}', 'r') as codeFile: 
        codeLines = codeFile.readlines()

    if codeLines == None: 
        print('No code found!')
        exit()

    codeLines = [x.replace('\n', '').strip().split(';') if x.replace('\n', '') else [] for x in codeLines]

    codeExpressions = [exp.strip() for line in codeLines for exp in line]
    for _ in range(codeExpressions.count('')):
        codeExpressions.remove('')

    return codeExpressions