import sqlite3
import mysql.connector as sql

class DBConnector:
    def __init__(self, dbname, user, password, host='localhost'):
        self.database = dbname
        self.user = user
        self.password = password
        self.host = host

    def get_connection(self):
        connection = sql.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host
            )
        print("Connected to the database successfully!")
        cursor = self.connection.cursor()
        return connection

