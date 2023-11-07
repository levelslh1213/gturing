from ..Messages.Break.Break import Break
from ..Messages.StartExec.StartExec import StartExec

def Run (code): 
    try:
        StartExec()
        exec(code)
    except Exception as e:
        Break(str(e))