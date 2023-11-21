from TuringMachine.turing_machine import TuringMachine
from TuringMachine.automatons.generic_automaton import GenericAutomaton

class ReservedFunctionsAutomaton(GenericAutomaton):
    
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

        if value == '<loop>':
            tm.WriteAndMove(value, +1)
            return self.__Q1(tm)
        elif value == '<if_condition>':
            tm.WriteAndMove(value, +1)
            return self.__Q1(tm)
        elif value == '<print>':
            tm.WriteAndMove(value, +1)
            return self.__Q5(tm)
        else:
            self.__failMessage('Not a valid function element!')
            return self.__QDead()
        
        # return self.__Q3(tm)
        
    @GenericAutomaton.statefunction
    def __Q1 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable_name>' or value == '<number>' or value == '<array_declaration>':
            tm.WriteAndMove(value, +1)
            return self.__Q2(tm)
        else :
            self.__failMessage('Not a valid manipulable element! Element: ' + str(value))
            return self.__QDead()
        
    @GenericAutomaton.statefunction
    def __Q2 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<inside_values>':
            tm.WriteAndMove(value, +1)
            return self.__Q3(tm)
        elif value == '<equals>':
            tm.WriteAndMove(value, +1)
            return self.__Q6(tm)
        else: 
            self.__failMessage('Not a valid operation at:' + str(value))
            return self.__QDead()

    @GenericAutomaton.finalstatefunction
    def __Q3 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable_name>' or value == '<array_declaration>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        else: 
            self.__failMessage('Not a valid manipulable element! Element: ' + str(value))
            return self.__QDead()
        
    @GenericAutomaton.finalstatefunction
    def __Q4 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<start_scope>':
            tm.WriteAndMove(value, +1)
            return self.__Q5(tm)
        elif value == '<subtract>' or value == '<addition>' or value == '<division>' or value == '<multiply>' or value == '<inside_values>':
            tm.WriteAndMove(value, +1)
            return self.__Q6(tm)
        else: 
            self.__failMessage('Not a valid manipulable element! Element: ' + str(value))
            return self.__QDead()
        
    @GenericAutomaton.finalstatefunction
    def __Q5 (self, tm:TuringMachine):
        value = tm.Read()

        return 'success'

    @GenericAutomaton.statefunction
    def __Q6 (self, tm:TuringMachine):
        value = tm.Read()

        if value == '<variable_name>' or value == '<number>' or value == '<array_declaration>':
            tm.WriteAndMove(value, +1)
            return self.__Q4(tm)
        else: 
            self.__failMessage('Not a valid manipulable element!' + str(value))
            return self.__QDead()