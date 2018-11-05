#simulation start dfa class for part 1
import sys
import time

class Dfa:
    # initiates dfa with blank states and accepting states
    def __init__(self):
        statesNo = None
        global accepting
        accepting = []
        global states
        states = []
        global alphabet

    # setter function to get info from the user for the dfa
    def set_dfa(self):
        # First get the number of states in the DFA
        statesNo = raw_input("Number of States: ")

        # Checks if input is integer if not re-asks for integer
        while statesNo.isdigit()==False:
            print("Please input integer...")
            statesNo = raw_input()

        # Next asks for accepting states
        newAccepting = raw_input("Accepting states: ")

        # Checks if accepting states are all
        print (self.check_input(newAccepting))
        while self.check_input(newAccepting) == False:
            print("Improper Accepting states, ensure states are integers.")
            newAccepting = raw_input("Accepting states: ")

        # With integer string we split and create accepting
        mapping = newAccepting.split()
        accepting = map(int, mapping)


        for i in range(0,int(statesNo)):
            if i == 0:
                states.append(raw_input("Input first state: "))
            else:
                states.append(raw_input("Input next state: "))

    # checks if input is a possible array of
    def check_input(self, chkString):
        foo = chkString.split()
        if all(x.isdigit() for x in foo) == True:
            return True
        else:
            return False
