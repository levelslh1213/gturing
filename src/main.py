from src import Compliler
import json

langName = 'reserved_words'
langStyle = {}
with open('src/Compliler/lang/' + langName + '.json', 'r') as jsonFile: 
        langStyle = json.load(jsonFile)

Compliler.Log.Info('Reading file...')
expressions = Compliler.CRead('exemples/ex3.txt')
Compliler.Log.Info('File readed!')

Compliler.Log.Info('Validating expressions...')
for expression in expressions:
    if not Compliler.ValidadeExpression(Compliler.GToken(expression, langStyle), expression):
        Compliler.Log.Break('Expression not valid!')
        exit()

Compliler.Log.Info('Expressions validated!')
code = Compliler.CConverter(expressions, langStyle)

# for index, codeLine in enumerate(code.split('\n')):
#      print(f'{str(index)}: {codeLine}')

Compliler.Exec(code)
