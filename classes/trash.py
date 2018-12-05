# main
#!/usr/bin/env python
import sys
import time
from dfa import Dfa

r1 = Dfa()

# initial input for number of states
statesNo = raw_input("Number of States: ")
while statesNo.isdigit() == False:
    print("Please input integer...")
    statesNo = raw_input()

r1.set_statesNo(statesNo)

# initial input accepting states
newAccepting = raw_input("Accepting states: ")
while r1.check_input(newAccepting) == False:
    print("Improper Accepting states, ensure states are integers.")
    newAccepting = raw_input("Accepting states: ")

r1.set_accepting(newAccepting)

# initial input alphabet
alphabet = raw_input("Alphabet: ")
# checks for doubles in the alphabet to eliminate errors
while r1.check_alphabet(alphabet) == False:
    alphabet = raw_input("Previous had double, Alphabet: ")

r1.set_alphabet(alphabet)

# initial input state changes
newStates = []
for i in range(0,int(statesNo)):
    if i == 0:
        tempState = raw_input("Input first state: ")
        while (r1.check_input(tempState) == False) or (len(tempState.split()) != len(alphabet)):
            tempState = raw_input("Improper Input, Input first state: ")
        newStates.append(tempState)
    else:
        tempState = raw_input("Input next state: ")
        while (r1.check_input(tempState) == False) or (len(tempState.split()) != len(alphabet)):
            tempState = raw_input("Improper Input, Input next state: ")
        newStates.append(tempState)

r1.set_states(newStates)
dfainput = raw_input("Test String: ")
print(r1.check_string(dfainput))
#r1.dfaStringtest(dfainput)



    # goes through equivalence steps to minimize DFA
    def minimizeDFA(self):
        self.nonAccepting = []
        self.pk = []
        for i in range(0,self.statesNo):
            if i not in self.accepting:
                self.nonAccepting.append(i)

        self.pk.append([self.accepting,self.nonAccepting])
        self.pk.append([self.accepting,self.nonAccepting])

    def calcPk(self):
        x = 0
        while 1:
            for i in range(0,len(pk[x])):
                if len(pk[x][i]) > 1:
