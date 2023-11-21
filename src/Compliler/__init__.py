from TuringMachine import TuringMachine
from TuringMachine import TokenWorker
from .modules.CodeReader.CodeReader import CodeReader as CRead
from .modules.CodeConverter.CodeConverter import CodeConverter as CConverter
from .modules.Tokens.GetToken import GetToken as GToken
from .modules.Runners.Run import Run as Exec
from .modules import Messages as Log
from .modules.Automatons.expression import ExpressionsAutomaton
from .modules.Automatons.functions import FunctionsAutomaton
from .modules.Automatons.reserverdFunctions import ReservedFunctionsAutomaton

def ValidadeExpression(TExpression, SExpression):
    print(TExpression)
    # print(SExpression)
    isValid = True
    for token in TExpression:
        if token == '<None>':
            Log.Error('Expression not recognized: ' + SExpression)
            isValid = False
            break
    
    tMachine = TuringMachine()
    tMachine.automatons['Function'] = FunctionsAutomaton()
    tMachine.automatons['Expression'] = ExpressionsAutomaton()
    tMachine.automatons['ReservedFunctions'] = ReservedFunctionsAutomaton()

    validations = []
    for key in tMachine.automatons.keys():
        validations.append({
            "result": teste_automaton(tMachine, key, TExpression),
            "message": tMachine.automatons[key].failMessage,
            "automaton": key
        })
    
    if True not in [x['result'] for x in validations]:
        isValid = False
        Log.Error('Expression not recognized: ' + SExpression)
        for x in validations:
            if x['result'] == False:
                Log.Error('Exception:  ' + x['message'])
    print('teste de validação: ' + str(validations))

    return isValid

def teste_automaton(tm: TuringMachine, automatonName, tokenList):
    tm.coil = []
    tm.coil = tokenList
    tm.pointer = 1
    tm.run(automatonName)
    return tm.automatons[automatonName].isFinalState
    