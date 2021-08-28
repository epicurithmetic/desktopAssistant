# This file defines the database structure for the daily planner.
import sqlite3

def createConnection(db_file):

    """
        This function creates a connection with a .db database file.
        If the file does not exist in the directory, then the .db file
        will be created when this function is called.

    """

    # Initialise the connection object.
    conn = sqlite3.connect(db_file)

    return conn

def createTable(conn, create_table_sql):

    """
        This function uses the SQL from the second input, to insert a table
        into the database specified by the connection object.

    """

    cur = conn.cursor()
    cur.execute(create_table_sql)


if __name__ == "__main__":

    database = "ddatabase.db"
    conn = createConnection(database)

    sql_create_planner_table = """ CREATE TABLE IF NOT EXISTS planner
                                (id integer PRIMARY KEY,
                                Title text NOT NULL,
                                Parent text NOT NULL,
                                Date text NOT NULL,
                                Complete text NOT NULL
                                );"""

    createTable(conn,sql_create_planner_table)
    conn.close()
