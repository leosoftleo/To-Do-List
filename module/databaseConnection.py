import mysql.connector

#Connect to database
def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="", # Username of database
        passwd="", # Password of database
        database="todolist_deploy"
    )
    return mydb
