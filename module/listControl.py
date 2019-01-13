from databaseConnection import connection
import datetime

def showAllItem(sessionID):
    #Connect to database
    db = connection()

    #Run SQL statement to get all the items according to the session ID
    cursor = db.cursor()
    sql = "SELECT item.name, item.itemID FROM item, session WHERE session.username = item.username AND session.sessionID = %s ORDER BY itemID"
    val = (sessionID,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    
    #Generate JSON
    JSONresult = {"result": [], "itemID": []}
    if len(result) != 0:
        for i in range(0, len(result)):
            JSONresult["result"].append(result[i][0].decode("utf-8"))
            JSONresult["itemID"].append(result[i][1])

    return JSONresult

def insertNewItem(sessionID, name): 
    #Connect to database
    db = connection()

    #Get the username and latest item ID
    username = ""
    itemID = 0

    cursor = db.cursor()
    sql = "SELECT item.itemID FROM item, session WHERE session.username = item.username AND session.sessionID = %s ORDER BY item.time DESC"
    val = (sessionID,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    if len(result) > 0:
        itemID = result[0][0] + 1
    else:
        itemID = 1

    cursor = db.cursor()
    sql = "SELECT login.username FROM login, session WHERE session.username = login.username AND session.sessionID = %s"
    val = (sessionID,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    username = result[0][0].decode("utf-8")
    
    #Run SQL statement to add new item according to the session ID
    cursor = db.cursor()
    sql = "INSERT INTO item VALUES(%s, %s, %s, %s)"
    val = (itemID, username, name, datetime.datetime.now())
    cursor.execute(sql,val)
    db.commit()

def deleteOldItem(sessionID, itemID):
    #Connect to database
    db = connection()

    #Get the username and latest item ID
    username = ""
    cursor = db.cursor()
    sql = "SELECT item.username FROM item, session WHERE session.username = item.username AND session.sessionID = %s"
    val = (sessionID,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    username = result[0][0].decode("utf-8")

    #Run SQL statement to delete item according to the session ID
    cursor = db.cursor()
    sql = "DELETE FROM item WHERE itemID = %s AND username = %s"
    val = (itemID, username, )
    cursor.execute(sql,val)
    db.commit()

