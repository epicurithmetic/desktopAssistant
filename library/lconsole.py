# This is the console for the library.

# Import some functions from auxillary modules.
import os
import platform
from library.lclasses import lClose
from library.lclasses import lHomeScreen
from library.commandLineBooks import bookShelf

# One function to clear the console, irregardless of platform (Linux/Windows)
def clearConsole():

    opsys = platform.system()

    if opsys == "Linux":
        return os.system("clear")
    else:
        return os.system("cls")

def library_main():

    # The user will be presented with the HomeScreen to start.
    library_state = lHomeScreen()

    while library_state.continue_program() == True:

        clearConsole()

        library_state.header()
        library_state.explanation()

        if library_state.option == "":                        # This if-else block can be used to return
            library_state.option = library_state.options()    # the user to the main menu of the current state.
        else:                                                 # Otherwise, the option will be performed.
            library_state = lClose()

    return ""
