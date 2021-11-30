import sqlite3
import pandas as pd

# load gta.db file (make sure you run main.py first to create it)
connection = sqlite3.connect("gta.db")
# create a cursor object to execute SQL
cursor = connection.cursor()

# SELECT all the values from the gta table inside gta.db
cursor.execute("select * from gta")
for row in cursor:
    print(row)

connection.close()
