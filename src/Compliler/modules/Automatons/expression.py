from TuringMachine.turing_machine import TuringMachine
from TuringMachine.automatons.generic_automaton import GenericAutomaton

class ExpressionsAutomaton(GenericAutomaton):
    
    def __init__(self):
        self.__failMessage = ''
        super().__init__()

    @property 
    def failMessage(self):
        return self.__failMessage
    
    @failMessage.setter
    def failMessage(self, value):
        self.__failMessage = value

    @GenericAutomaton.deathstatefunction
    def __QDead (self):
        return 'fail'

    @GenericAutomaton.initialstatefunction
    def __Q0 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable>':
            tm.WriteAndMove(value, +1)
            return self.__Q1(tm)
        elif value == '<variable_name>':
            tm.WriteAndMove(value, +1)
            return self.__Q2(tm)
        else:
            return self.__QDead()
        
    @GenericAutomaton.statefunction
    def __Q1 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable_name>':
            tm.WriteAndMove(value, +1)
            return self.__Q2(tm)
        else :
            return self.__QDead()
        
    @GenericAutomaton.statefunction
    def __Q2 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<allocation>':
            tm.WriteAndMove(value, +1)
            return self.__Q3(tm)
        elif value == '<variable_increment>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        else: 
            return self.__QDead()

    @GenericAutomaton.statefunction
    def __Q3 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable_name>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        elif value == '<number>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        elif value == '<array_declaration>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        else: 
            return self.__QDead()
        
    @GenericAutomaton.finalstatefunction
    def __Q4 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<subtract>' or value == '<addition>' or value == '<division>' or value == '<multiply>' or value == '<inside_values>':
            tm.WriteAndMove(value, +1)
            return self.__Q3(tm)
        else:
            return 'success'