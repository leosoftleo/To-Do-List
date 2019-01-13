from flask import Flask, request
from flask_cors import CORS
from login import *
from listControl import *
import json



app = Flask(__name__)
CORS(app)


@app.route("/getUsername", methods=["POST"])
def get_username():
    if request.method == "POST":
        sessionID = request.values["sessionID"]
        result = getUsername(sessionID)
        return result
    return " "


@app.route("/login", methods=["POST"])
def loginmethod():
    if request.method == "POST":
        username = request.values["username"]
        password = request.values["password"]
        loginStatus = login(username, password)
        return json.dumps(loginStatus)
    return " "

@app.route("/register", methods=["POST"])
def registermethod():
    if request.method == "POST":
        username = request.values["username"]
        password = request.values["password"]
        status = register(username, password)
        return json.dumps(status)
    return " "

@app.route("/changePassword", methods=["POST"])
def changePasswordMethod():
    if request.method == "POST":
        sessionID = request.values["sessionID"]
        password = request.values["password"]
        changePassword(sessionID, password)
    return " "

@app.route("/getList", methods=["POST"])
def getList():
    if request.method == "POST":
        sessionID = request.values["sessionID"]
        result = showAllItem(sessionID)
        return json.dumps(result)
    return " "

@app.route("/insertItem", methods=["POST"])
def insertItem():
    if request.method == "POST":
        sessionID = request.values["sessionID"]
        name = request.values["name"]
        insertNewItem(sessionID, name)
    return " "

@app.route("/deleteItem", methods=["POST"])
def deleteItem():
    if request.method == "POST":
        sessionID = request.values["sessionID"]
        itemID = request.values["itemID"]
        deleteOldItem(sessionID, itemID)
        return ""
    return " "

if __name__ == '__main__':
    app.debug = False
    app.run()