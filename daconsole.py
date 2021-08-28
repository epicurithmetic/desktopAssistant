#               Source file for the desktop assistant main console.

# Some os calls need to be made in order clear console.
import os
import platform

# Code for the homescreen.
from daclasses import daHomeScreen
from daclasses import daClose

# Import the _main() functions for each part of the assistant.
from map.mconsole import map_main
from budget.bconsole import budget_main
from library.lconsole import library_main
from updates.uconsole import updates_main
from recipes.rconsole import recipes_main
from planner.dconsole import planner_main
from inspire.iconsole import inspire_main
from projects.pconsole import projects_main

# One function to clear the console, irregardless of platform (Linux/Windows)
def clearConsole():

    opsys = platform.system()

    if opsys == "Linux":
        return os.system("clear")
    else:
        return os.system("cls")



if __name__ == "__main__":

    # Load the user into the desktop assistant homescreen.
    user_state = daHomeScreen()

    while user_state.continue_program() == True:

        # The entire console runs within this loop. It will stop when the
        # user has chosen the class close() and hence user.continue == False.

        clearConsole()

        # Print the landing screen information for a given class.

        if user_state.option == "":                     # This if-else block can be used to return
            user_state.option = user_state.options()    # the user to the main menu of the current state.
        else:                                           # Otherwise, the option will be performed.
            pass


        # At this point the user has chosen an option. We need to act on the option
        # But this action depends on the state of the user i.e. where they are in the console.
        if user_state.state == "daHome":

            # In this case, the user has chosen an option on daHomeScreen()
            if user_state.option == "D":

                user_state.option = planner_main()

            elif user_state.option == "L":

                user_state.option = library_main()      # Return of each _main() call will
                                                        # either [Q] the assistant or send
            elif user_state.option == "P":              # the user back to the assistant
                                                        # home screen.
                user_state.option = projects_main()

            elif user_state.option == "U":

                user_state.option = updates_main()

            elif user_state.option == "M":

                user_state.option = map_main()

            elif user_state.option == "R":

                user_state.option = recipes_main()

            elif user_state.option == "B":

                user_state.option = budget_main()

            elif user_state.option == "I":

                user_state.option = inspire_main()

            else:
                user_state = daClose()

        else:
            input("Any key to exit.")
            user_state = daClose()

    # Outside primary loop. Program is closing.
    clearConsole()
    print("Laterz")
