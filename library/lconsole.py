# This is the console for the library.

# Import some functions from auxillary modules.
import os
from library.commandLineBooks import bookShelf
from library.lclasses import lHomeScreen
from library.lclasses import lClose

def library_main():

    # The user will be presented with the HomeScreen to start.
    library_state = lHomeScreen()

    while library_state.continue_program() == True:

        os.system('clear')

        library_state.header()
        library_state.explanation()

        if library_state.option == "":                        # This if-else block can be used to return
            library_state.option = library_state.options()    # the user to the main menu of the current state.
        else:                                                 # Otherwise, the option will be performed.
            library_state = lClose()

    return ""
