import sqlite3

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('Sign_in/users.db')
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        user_id TEXT,
        passeword TEXT,
        Log_in TEXT)""")
        self.connection.commit()

    def save_user(self,user):
        return


        