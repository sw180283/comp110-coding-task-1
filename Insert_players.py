#!/usr/bin/python

#Turn on debug mode.
import cgitb
cgitb.enable()

#Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

#Connect to the database.
import cgi
form = cgi.FieldStorage()

if "user" not in form:
  print ("Something Went Wrong")
else
  print("<b>Hello " + str(form.getvalue("user")) + "<b>")
  my_first_int = 1
  my_first_str = str(form.getvalue("user"))
  
#Connect to the database.
import pymysql
conn = pymysql.connect(
  db = 'example',
  user = 'root'
  passwd = 'password' #changed this incase it matter
  host = 'localhost')
c = conn.cursor()

#Insert some example data - Having some problem with this as my database says there is an error.
c.execute("INSERT INTO players VALUES (" + my_first_int _ ", ' " + my_first_str + "', 'Users')")
conn.commit

#Print database
c.execute("SELECT * FROM players)
print([r[0], r[1]) for r in c.fetchall()])