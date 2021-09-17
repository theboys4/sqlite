import sqlite3
connection=sqlite3.connect('movie.db')
cursor=connection.cursor()
command="""CREATE TABLE IF NOT EXISTS
movie(name TEXT, actor TEXT , actress TEXT, director TEXT, year of release INTEGER)"""
cursor.execute(command)
c1="""INSERT INTO movie VALUES ('abcd','kavi','thrisha','harish',2001)"""
c2="""INSERT INTO movie VALUES ('efgh','jai','nayanthara','hari',2010)"""
c3="""INSERT INTO movie VALUES ('ijk','thillai','katrina','harish',2001)"""
c4="""INSERT INTO movie VALUES ('xyz','aravinth','deepika padukone','shankar',2011)"""
cursor.execute(c1)
cursor.execute(c2)
cursor.execute(c3)
cursor.execute(c4)
cursor.execute("SELECT *FROM movie")
r=cursor.fetchall()
print(r)
cursor.execute("select name from movie where actor='aravinth'")
results=cursor.fetchall()
print(results)
