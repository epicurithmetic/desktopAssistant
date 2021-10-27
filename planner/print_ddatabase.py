# This file contains the code required to print the daily planner in a nice manner.
# In particular we want each subtask layer to have identation and either [ ] or [X]
# to distinguish complete from incomplete tasks.

from planner.read_ddatabase import dTaskSubtaskStructure


def printDailyTasks():

    """
        This function prints the tasks and subtasks.

    """

    taskSubTasks = dTaskSubtaskStructure()
    print(taskSubTasks)

    x = "|||"
    y = "-"
    z = " "
    w = "\n"

    for task in taskSubTasks:

        # Update: One day do check for completion here
        # to determine whether [ ] or [X] is printed.

        print(w + " "*5 + "[ ]:" + task[0] + w)

        for subtask in task[1]:

            print(" "*10 + "[ ]:" + subtask)

printDailyTasks()
