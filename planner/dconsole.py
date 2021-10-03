# This is the console for the Daily Planner.

# Import some functions from auxillary modules.
import os
import re
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
                                                              # Otherwise, the option will be performed.

        # We need to parse the different options here.
        #
        #       Options for the user:
        #           [ ]: Add task with "atx.y.z" Adds a task sub to x and y.
        #           [ ]: Remove task with "rtx.y.z" Removes a task sub to x and y.
        #           [ ]: Complete task with "ctx.y.z" Marks task complete.
        #           [ ]: Reset task list with "reset"

        # This solution with RegEx is not fool-proof. Nor elegant.
        elif not re.search(r"^at", planner_state.option) == None:

            # If command starts with "at" then assume of correct ad task form.
            taskHierachy = planner_state.option.split("at")[1]
            taskHierachy = taskHierachy.split(".")
            taskHierachy = [int(x) for x in taskHierachy]       # This list should have integers indicating
                                                                # the position of new task.
            print(taskHierachy)
            input("I am ready to add a task to the planner.")
            planner_state.option = ""

        elif not re.search(r"^rt", planner_state.option) == None:

            # If command starts with "rt" then assume of correct ad task form.
            taskHierachy = planner_state.option.split("rt")[1]
            taskHierachy = taskHierachy.split(".")
            taskHierachy = [int(x) for x in taskHierachy]       # This list should have integers indicating
                                                                # the position of the task to be removed.
            print(taskHierachy)
            input("I am ready to remove a task from the planner.")
            planner_state.option = ""

        elif not re.search(r"^ct", planner_state.option) == None:

            # If command starts with "ct" then assume of correct ad task form.
            taskHierachy = planner_state.option.split("ct")[1]
            taskHierachy = taskHierachy.split(".")
            taskHierachy = [int(x) for x in taskHierachy]       # This list should have integers indicating
                                                                # the position of completed task.
            print(taskHierachy)
            input("I am ready to complete a task in the planner.")
            planner_state.option = ""

        elif planner_state.option == "reset":

            input("I am ready to rest the planner for the day.")
            planner_state.option =   ""

        elif planner_state.option == "Q":

            planner_state = dClose()

        else:
            input("This command does not make sense. Hit any key to return to the previous window.")
            planner_state.option =   ""

    return ""
