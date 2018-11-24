# main
#!/usr/bin/env python
import sys
import time
from dfa import Dfa

r1 = Dfa()

flDfa = open("simDFA.txt")

r1.set_statesNo(int(flDfa.readline()))

r1.set_accepting(flDfa.readline())

r1.set_alphabet(flDfa.readline())

tempStates = []
for i in range(0,r1.statesNo):
    tempStates.append(flDfa.readline())

r1.set_states(tempStates)
flDfa.close()

print("Number of States: " + str(r1.statesNo))
print("Accepting States: " + str(r1.accepting))
print("Alphabet: " + r1.alphabet.rstrip())
print("States: " + str(r1.states[0]))
for i in range(1,r1.statesNo):
    print(r1.states[i])
#3dfainput = raw_input("Test String: ")
#print(r1.check_string(dfainput))
