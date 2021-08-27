#2. Create Database Dynamically
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE DATABASE movies") #bydefault the database will tbkes automatically lowercase letter
  print("Db Successfully Created")
except:
  print("Db alreay Created")