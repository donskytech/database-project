"""
Created by donsky for www.donskytech.com
"""
import os
import sqlite3

# Create DB in current file
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'StudentDB.db')
CREATE_SQL_FILE = os.path.join(os.path.dirname(__file__), 'StudentDB.sql')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def create_table():
    db_conn = db_connect()

    with db_conn:
        try:
            db_conn = db_connect()
            cursor = db_conn.cursor()
            print("Successfully Connected to SQLite")

            with open(CREATE_SQL_FILE, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            cursor.executescript(sql_script)
            print("SQLite script executed successfully")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

    print("Successfully created table!")


def create_student_task(conn, student):
    """
    Create a new student task
    :param conn:
    :param student:
    :return:
    """

    sql = ''' INSERT INTO Students(student_id, name, rf_id_code)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


def create_students():
    # create a database connection
    db_conn = db_connect()

    with db_conn:
        # students
        student1 = (2000, 'Adam Smith', "00-11-22")
        student2 = (2001, 'Steve Davidson', "00-33-44")
        student3 = (2002, 'Michael Trent', "00-55-66")

        # create student
        create_student_task(db_conn, student1)
        create_student_task(db_conn, student2)
        create_student_task(db_conn, student3)


def main():
    create_table()
    create_students()


if __name__ == '__main__':
    main()