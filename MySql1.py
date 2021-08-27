#check mysql is existing or not in specified user
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root", # by default my sql user name is root and password is blank
  passwd=""
)
print(mydb)