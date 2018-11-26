# main
#!/usr/bin/env python
import sys
import time
from dfa import Dfa

r1 = Dfa()

# Opens the DFA text file and fills out the dfa statistics:
# State Number, Accepting States, Alphabet, and State Changes
flDfa = open("simDFA.txt")

r1.set_statesNo(int(flDfa.readline()))

r1.set_accepting(flDfa.readline())

r1.set_alphabet(flDfa.readline())

tempStates = []
for i in range(0,r1.statesNo):
    tempStates.append(flDfa.readline())

r1.set_states(tempStates)
flDfa.close()

# Displays the Dfa
print("Number of States: " + str(r1.statesNo))
print("Accepting States: " + str(r1.accepting))
print("Alphabet: " + r1.alphabet.rstrip())
print("States: " + str(r1.states[0]))
for i in range(1,r1.statesNo):
    print(r1.states[i])

# goes through the test trings and runs them against the dfa
dfainput = open("simDFA_stringTest.txt")

testString = dfainput.readline()
while testString:
    print(testString.rstrip())
    print(r1.check_string(testString.rstrip())+"\n")
    testString = dfainput.readline()
dfainput.close
#3dfainput = raw_input("Test String: ")
#print(r1.check_string(dfainput))
