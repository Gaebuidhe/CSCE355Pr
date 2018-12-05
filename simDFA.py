# Joseph Frazier
# CSCE 355
# December 6, 2018
# main
#!/usr/bin/env python
import sys
from dfa import Dfa

r1 = Dfa()

# Opens the DFA text file and fills out the dfa statistics:
# State Number, Accepting States, Alphabet, and State Changes
flDfa = open(sys.argv[1])

r1.set_statesNo(int(flDfa.readline()[18:-1]))

r1.set_accepting(flDfa.readline()[18:-1])

r1.set_alphabet(flDfa.readline()[10:-1])

tempStates = []
for i in range(0,r1.statesNo):
    tempStates.append(flDfa.readline()[0:-1])

r1.set_states(tempStates)
flDfa.close()


# goes through the test trings and runs them against the dfa
dfainput = open(sys.argv[2])

testString = dfainput.readline()
while testString:
    print(r1.check_string(testString[0:-1])) #passes the current string to func.
    testString = dfainput.readline()
dfainput.close
