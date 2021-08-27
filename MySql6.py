#find record
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="movies"
)

mycursor = mydb.cursor()
moviename=input("Enter your movie name")
sql = "SELECT * FROM listofmovies WHERE movie_name ='"+ moviename + "'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)