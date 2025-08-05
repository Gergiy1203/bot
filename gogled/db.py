import main
import sqlite3 as sq

conction = sqlite3.connect('databse.sqlite')



cursor = connect.cursor()
cursor.execute("SELECT <column_name> FROM <table_name>")
results = cursor.fetchall()
cursor.execute("INSERT INTO <table_name> (id, name, surname, birthdate) VALUES (2, 'Petr', 'Ivanov', '2003-12-13') ")
connect.commit()

