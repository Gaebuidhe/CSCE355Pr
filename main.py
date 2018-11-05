# main
#!/usr/bin/env python
import sys
import time
from dfa import Dfa

# variable used for maintaining while loop
status = True

#Basic interface with the program exit turns status to false and kills program
print("\nThis project demonstrates the various applications of DFA.\n")
while status == True:

    #initial and continuous input request for main menu
    input = raw_input("Please choose one of the following options to test or 'exit' to exit.\n\n" +
    " 1-Simulation\n 2-Minimizing\n 3-Text Search\n 4-Closure C&I\n 5-Closure IHI\n 6-Properties\n 7-Exit\n\n"+
    "Selection: ")

    #below are if else commands from the menu and an else statement to catch un usable inputs
    #reading the data from input one of the following will be used
    #the if else statements have a variety of acceptable inputs depending on the user interpretation of the menu
    if input.lower == "simulation" or input[0][0] == '1':
        r1 = Dfa()
        r1.set_dfa()
        

    elif input.lower == "minimizing" or input.lower == "minimize" or input[0][0] =='2':
        print ("I'm sorry this feature has not yet been implemented.")

    elif input.lower == "text search" or input.lower == "text" or input.lower == "search" or input[0][0] == '3':
        print ("I'm sorry this feature has not yet been implemented.")

    elif input.lower == "closure c&i" or input.lower == "c&i" or input[0][0] == '4':
        print ("I'm sorry this feature has not yet been implemented.")

    elif input.lower == "closure ihi" or input.lower == "ihi" or input[0][0] == '5':
        print ("I'm sorry this feature has not yet been implemented.")

    elif input.lower == "properties" or input.lower == "property" or input[0][0] =='6':
        print ("I'm sorry this feature has not yet been implemented.")

    elif input.lower() == "exit" or input[0][0] == '7':
        print("\nHave a wonderful day! Good-bye.")
        status = False

    else:
        print("I'm sorry, I did not understand your request. Please type either the number or\n"+
        "the text or the full selection of the item you would like to test.\n")

    time.sleep(.75)
