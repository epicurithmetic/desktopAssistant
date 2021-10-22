# Functions for reading the ddatebase.db

# When reading the database for the daily planner I need to be
# able to search for the following:

#   [ ]: All primary tasks.
#   [ ]: All subtasks, given a primary.
#   [ ]: Determine whether or not a task is complete.
#   [ ]:
#   [ ]:
#   [ ]:
#   [ ]:

import sqlite3


def dPrimaryTasks():

    """
        This returns a list containing lists of length two:
            the first element is the title while the second is the
            task number of the title.

    """

    conn_ddatabase = sqlite3.connect("ddatabase.db")

    sql_primaryTasks = "SELECT title FROM planner WHERE subtask = 'n';"

    # Execute the sql for primary tasks.
    cur = conn_ddatabase.cursor()
    cur.execute(sql_primaryTasks)
    data = cur.fetchall()
    number_of_primary = len(data)


    # Data contains the title, but we can clean the format with the following.
    primaryTaskTitles = []
    for i in range(number_of_primary):
        primaryTaskTitles.append(data[i][0])

    # Now we can pair the primaryTasks with their taskNumber.
    primaryTasksNumber = []

    for task in primaryTaskTitles:
        sql_taskNumber = ("SELECT taskNumber FROM planner WHERE title = '%s';" % task)
        cur = conn_ddatabase.cursor()
        cur.execute(sql_taskNumber)
        data = cur.fetchall()

        primaryTasksNumber.append([task,data[0][0]])

    return primaryTasksNumber

def dTaskSubtaskStructure():


    conn_ddatabase = sqlite3.connect("ddatabase.db")

    primaryWithNumbers = dPrimaryTasks()


    dTaskSubtaskList = []

    for task in primaryWithNumbers:
        sql_subTask = ("SELECT title FROM planner WHERE taskNumber = %d AND subTask = 'Y';" % task[1])
        cur = conn_ddatabase.cursor()
        cur.execute(sql_subTask)
        data = cur.fetchall()

        subTasks = []
        for subTask in data:
            subTasks.append(subTask[0])


        dTaskSubtaskList.append([task[0],subTasks])

    return dTaskSubtaskList
