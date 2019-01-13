# To-Do-List
Developed by Leo Tsang :smiley:

## Introduction
  This is my first web project. It called To-Do-List. It is a simple "to do list" website to demonstrate my learning outcome.
  
  Techniques:<br />
  Client side: JQuery, Bootstrap <br />
  Server side: Python Flask <br />
  Database: MySQL

## Deployment

  For the APIs server, the following packages need to be installed.
  
  * Flask
  * Flask-Cors
  * mysql-connector
  
 Firstly, create requirment.txt
 ```
 Flask
 Flask-Cors
 mysql-connector
 ```
 Secondly, install packages according to requirment.txt
 ```
 pip install -r requirment.txt
 ```
 
 Lastly, you can use the following command to check whether the packages is installed properly or not (Optional)
 ```
 pip list
 ```
 
 For the database, use the following SQL statement to create the table
 ```SQL
 # The table containing username and password
 CREATE TABLE login (
  username varchar(12) COLLATE utf8_bin NOT NULL,
  password varchar(16) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

# The table containing login session id
CREATE TABLE session (
  sessionID varchar(60) COLLATE utf8_bin NOT NULL,
  username varchar(12) COLLATE utf8_bin NOT NULL,
  loginTime datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

# The table containing the item of the to do list
CREATE TABLE item (
  itemID int(15) NOT NULL,
  username varchar(12) COLLATE utf8_bin NOT NULL,
  name varchar(30) COLLATE utf8_bin NOT NULL,
  time datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

# Add primary key and foregin key to each table
ALTER TABLE login
  ADD PRIMARY KEY (username);
  
 ALTER TABLE session
  ADD PRIMARY KEY (sessionID),
  ADD CONSTRAINT session_fk1 FOREIGN KEY (username) REFERENCES login (username);
  
 ALTER TABLE item
  ADD PRIMARY KEY (itemID, username),
  ADD CONSTRAINT item_fk1 FOREIGN KEY (username) REFERENCES login (username);
 ```
 
 # Demonstration
 
 ### Before login
 
  Index page 
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/indexPage.PNG)
  
  Login
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/loginModal.PNG)
  
  Register
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/registerModal.PNG)
 
 ### After login
 
  Home page
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/homePage.PNG)
  
  List page
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/listPage.PNG)
  
  Add item
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/addItem_1.PNG)
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/addItem_2.PNG)
  
  Delete item
  
  ![image](https://github.com/leosoftleo/To-Do-List/blob/master/image/deleteItem.png)
