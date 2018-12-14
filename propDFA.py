# Joseph Frazier
# CSCE 355
# December 6, 2018
# main
#!/usr/bin/env python
import sys
from dfa import Dfa
from dfs import Dfs

r1 = Dfa()
properties = ""
empNonemp = False

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

# sets up reachable states from 0
depth = Dfs(r1.states,r1.accepting)
reachable = depth.DFS(0)

# determines if accepting states are reachable
for i in range(0,len(list(r1.accepting))):
    tempaccepting = list(r1.accepting)
    if tempaccepting[i] in reachable:
        properties = properties + "nonempty"
        empNonemp = True # if true dfa is nonempty
        break
    if i == (len(r1.accepting) - 1):
        properties = properties + "empty"

# determines if there is a cycle that reaches a finalstate
# if there is a cycle and start reaches final state declares infinite
if empNonemp and depth.isCyclic():
    properties = properties + " infinite"
else:
    properties = properties + " finite"

print(properties)
