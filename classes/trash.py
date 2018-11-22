# setter function to get info from the user for the dfa
def set_dfa1(self):
    # First get the number of states in the DFA
    statesNo = raw_input("Number of States: ")

    # Checks if input is integer if not re-asks for integer
    while statesNo.isdigit()==False:
        print("Please input integer...")
        statesNo = raw_input()

    # Next asks for accepting states
    newAccepting = raw_input("Accepting states: ")

    # Checks if accepting states are all
    while self.check_input(newAccepting) == False:
        print("Improper Accepting states, ensure states are integers.")
        newAccepting = raw_input("Accepting states: ")

    # With integer string we split and create accepting
    mapping = newAccepting.split()
    accepting = map(int, mapping)

    # Get alphabet for the Dfa
    alphabet = raw_input("Alphabet: ")

    newStates = []
    for i in range(0,int(statesNo)):
        if i == 0:
            newStates.append(raw_input("Input first state: "))
        else:
            newStates.append(raw_input("Input next state: "))

    # maps integers to states array which lays out paths during a particular state
    for i in range(0,int(statesNo)):
        mid = newStates[i].split()
        states.append(map(int, mid))
