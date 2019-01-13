from databaseConnection import connection
import hashlib
import datetime


def getUsername(sessionID):
    #Connect to database
    db = connection()

    #Get the username
    cursor = db.cursor()
    sql = "SELECT login.username FROM login, session WHERE session.username = login.username AND session.sessionID = %s"
    val = (sessionID,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    return result[0][0].decode("utf-8")


def login(username, password):
    #Connect to database
    db = connection()

    #Check the username and password
    cursor = db.cursor()
    sql = "SELECT username FROM login WHERE username=\"" + username + "\" AND password=\"" + password + "\""
    cursor.execute(sql)
    result = cursor.fetchall()

    #Create JSON source
    status = {"sessionID": "0"}
    
    #If login successfully
    if len(result) != 0:

        #Create session information
        md5Content = username + str(datetime.datetime.now())
        m = hashlib.md5(md5Content.encode("utf-8")).hexdigest()
        status["sessionID"] = m
        validdate = datetime.datetime.now() + datetime.timedelta(hours=1)

        #Update session into database
        sql = "INSERT INTO session VALUES(%s, %s, %s)"
        val = (m, username, validdate)
        cursor.execute(sql,val)
        db.commit()

    return status

def register(username, password):
    #Connect to database
    db = connection()

    
    '''
    Status code references
    0 : Success
    1 : Repeated username
    2 : Password does not meet requirement
    '''

    #Initialize status code 
    status = {"status": 0}

    #Check the password
    if (len(password) < 6):
        status["status"] = 2
        return status

    #Check whether the username is repeated or not
    cursor = db.cursor()
    sql = "SELECT * FROM login WHERE username = %s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    if len(result) != 0:
        status["status"] = 1
        return status

    #Insert new username and password to login table
    cursor = db.cursor()
    sql = "INSERT INTO login VALUES(%s, %s)"
    val = (username, password, )
    cursor.execute(sql, val)
    db.commit()

    return status

def changePassword(sessionID, newPassword):
    #Connect to database
    db = connection()

    #Find the username according to the session ID
    username = getUsername(sessionID)
    
    #Change the password
    cursor = db.cursor()
    sql = "UPDATE login SET password = %s WHERE username = %s"
    val = (newPassword, username, )
    cursor.execute(sql, val)
    db.commit()
