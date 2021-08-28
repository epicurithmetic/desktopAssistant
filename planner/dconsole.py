# This is the console for the Daily Planner.

# Import some functions from auxillary modules.
import os
from planner.dclasses import dClose
from planner.dclasses import dHomeScreen

def planner_main():
    # The user will be presented with the HomeScreen to start.
    planner_state = dHomeScreen()

    while planner_state.continue_program() == True:

        os.system('clear')

        planner_state.header()
        planner_state.explanation()

        if planner_state.option == "":                        # This if-else block can be used to return
            planner_state.option = planner_state.options()    # the user to the main menu of the current state.
        else:                                                 # Otherwise, the option will be performed.
            planner_state = dClose()

    return ""
