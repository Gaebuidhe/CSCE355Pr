# main
#!/usr/bin/env python
import sys
import time


# Opens the DFA text file and fills out the dfa statistics:
# State Number, Accepting States, Alphabet, and State Changes
flDfa = open(sys.argv[1])

statesNo = flDfa.readline()[18:-1]
accept = flDfa.readline()[18:-1]
alphab = flDfa.readline()[10:-1]

tempStates = []
for i in range(0,int(statesNo)):
    tempStates.append(flDfa.readline()[0:-1])

flDfa.close()

print(statesNo)
print(accept)
print(alphab)
print(tempStates[0])
