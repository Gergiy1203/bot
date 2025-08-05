import main
import sqlite3 as sq

conction = sqlite3.connect('databse.sqlite')



cursor = connect.cursor()
cursor.execute("SELECT <column_name> FROM <table_name>")
results = cursor.fetchall()
