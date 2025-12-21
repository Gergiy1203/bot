import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT




connection = psycopg2.connect(user="postgres",
    password="1111",
    host="127.0.0.1",
    port="5432")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
sel_create_database = 'create database postgres_db'
cursor.execute(sql_create_database)
