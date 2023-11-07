from .modules.CodeReader.CodeReader import CodeReader as CRead
from .modules.CodeConverter.CodeConverter import CodeConverter as CConverter
from .modules.Tokens.GetToken import GetToken as GToken
from .modules.Runners.Run import Run as Exec
from .modules import Messages as Log

def ValidadeExpression(TExpression, SExpression):
    print(TExpression)
    return True