#simulation start dfa class for part 1
import sys
import time

class Dfa:
    global statesNo
    global accepting
    global states
    global alphabet
    global curState
    global psFL
    global nonAccepting

    # initiates dfa with blank states and accepting states
    def __init__(self):
        self.statesNo = None
        self.accepting = []
        self.states = []
        self.curState = 0

    #set states Number
    def set_statesNo(self, newNo):
        self.statesNo = newNo


    # accepting states setter
    def set_accepting(self, list):
        mapping = list.split()
        self.accepting = map(int, mapping)

    # states setter
    def set_states(self, listStr):
        for i in range(0,int(self.statesNo)):
            mid = listStr[i].split()
            self.states.append(map(int, mid))

    # alphabet setter takes in a string
    def set_alphabet(self, alpStr):
        self.alphabet = alpStr

    # checks if input is a possible array of
    def check_input(self, chkString):
        foo = chkString.split()
        if all(x.isdigit() for x in foo) == True:
            return True
        else:
            return False

    # take string and test it against current DFA
    def dfaStringtest(self, inputStr):
        for i in range (0,len(inputStr)):
            temp = inputStr[i]
            if temp in self.alphabet:
                print(self.alphabet.index(temp))
            else:
                print("Fail")

    # takes the alphabet and checks for doubles
    def check_alphabet(self, testAlpha):
        for i in range(0, len(testAlpha)):
            if testAlpha.count(testAlpha[i]) > 1:
                return False
        return True

    # takes the test string and passes it through the checks
    def check_string(self, inStr):
        self.curState = 0
        for i in range(0,len(inStr)):
            if inStr[i] in self.alphabet:
                tempState = self.states[int(self.curState)][int(self.alphabet.index(inStr[i]))]
                self.curState = tempState
                if self.curState >= self.statesNo or self.curState < 0:
                    return "reject"
            else:
                return "reject"
        if self.curState in self.accepting:
            return "accept"
        else:
            return "reject"

    def minimizeDFA(self):
        self.
