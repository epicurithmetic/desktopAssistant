# This is the console for the Daily Planner.

# Import some functions from auxillary modules.
import os
import platform
from planner.dclasses import dClose
from planner.dclasses import dHomeScreen

# One function to clear the console, irregardless of platform (Linux/Windows)
def clearConsole():

    opsys = platform.system()

    if opsys == "Linux":
        return os.system("clear")
    else:
        return os.system("cls")

def planner_main():
    # The user will be presented with the HomeScreen to start.
    planner_state = dHomeScreen()

    while planner_state.continue_program() == True:

        clearConsole()

        planner_state.header()
        planner_state.explanation()

        if planner_state.option == "":                        # This if-else block can be used to return
            planner_state.option = planner_state.options()    # the user to the main menu of the current state.
        else:                                                 # Otherwise, the option will be performed.
            planner_state = dClose()

    return ""
