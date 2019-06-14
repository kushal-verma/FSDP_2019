"""
Database Handling ( sqlite, mysql online, mongodb and mongo atlas )
"""


"""
Database handling using sqlite 
"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'university.db' )


# creating cursor
c = conn.cursor()



# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE student(
          Student_Name TEXT, Student_Age INTEGER, Student_Roll_no INTEGER, Student_Branch TEXT
          )""")



c.execute("INSERT INTO student VALUES ('Sylvester', 19, 50, 'CSE')")
c.execute("INSERT INTO student VALUES ('Yogendra', 20, 70, 'ME')")
c.execute("INSERT INTO student VALUES ('Pradeep', 19, 30, 'IT')")
c.execute("INSERT INTO student VALUES ('Kunal', 18, 31, 'EC')")
c.execute("INSERT INTO student VALUES ('Devendra', 20, 36, 'IT')")
c.execute("INSERT INTO student VALUES ('Lakshya', 19, 59, 'CSE')")
c.execute("INSERT INTO student VALUES ('Aditya', 17, 23, 'EE')")
c.execute("INSERT INTO student VALUES ('Abhishek', 19, 10, 'ME')")
c.execute("INSERT INTO student VALUES ('Kushal', 18, 67, 'CE')")
c.execute("INSERT INTO student VALUES ('Aman', 20, 76, 'EC')")



c.execute("SELECT * FROM student")

print ( c.fetchone()) 

print ( c.fetchmany(2)) 

print ( c.fetchall() )

c.execute("SELECT * FROM student")


df = DataFrame(c.fetchall())  
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]
 
conn.commit()

conn.close()
