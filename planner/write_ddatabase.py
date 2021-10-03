# This file defines methods for writing data to the planner database.
import sqlite3
from datetime import date
from create_ddatabase import createConnection

def insertTask(conn):

    """
        This method lets the user input a task into the daily planner
        database. Prompting them for: title, parent task, and completion.

        Note: the date section will be inserted automatically.

    """

    # CHANGES REQUIRED: Database structure has been changed. More infomration need to write to .db

    task_name = ""
    task_parent = ""
    task_complete = ""

    user_dhappy = False
    while not user_dhappy:

        task_name = input("Task name: ")
        task_parent = input("Parent task [Top/number]: ")
        # Future Rob - you need to add the subtask placement features here.
        task_complete = input("Is the task complete? [Y/n]: ")

        task_check = input("Is this information correct? [Y/n]: ")

        if task_check == "Y":
            user_dhappy = True
        else:
            pass

    insert_sql = """ INSERT INTO Planner (Title, Parent, Date, Complete)
                     VALUES(?,?,?,?)"""

    # Date NOT NULL. Use time module to get the data.
    task_date = date.today()
    print(task_date)

    task_data = (task_name, task_parent, task_date, task_complete)

    with conn:
        cur = conn.cursor()
        cur.execute(insert_sql,task_data)

    print("Task has been entered.")

conn_planner = createConnection("ddatabase.db")
insertTask(conn_planner)
