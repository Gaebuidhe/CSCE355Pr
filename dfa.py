#simulation start dfa class for part 1
import sys
import time

class Dfa:
    #initiates dfa with blank states and accepting states
    def __init__(self):
        statesNo = None
        global accepting
        accepting = []
        global states
        states = []

    #
    def set_dfa(self):
        print("Number of States:")
        statesNo = int(input())
        print("Accepting states:")
        newAccepting = raw_input()
        mapping = newAccepting.split()
        accepting = map(int, mapping)
        for i in range(0,statesNo):
            if i == 0:
                states.append(raw_input("Input first state: "))
            else:
                states.append(raw_input("Input next state: "))
