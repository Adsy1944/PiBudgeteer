import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="adsy1944",
        password="13George",
        database="budgiteer"
        )

    return mydb
