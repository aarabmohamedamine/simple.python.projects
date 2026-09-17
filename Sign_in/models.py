from random import choice,sample
import random
import string as str
import sqlite3
from datetime import datetime
#password and account number generator  

def lenght_validation():
    while True:
        try:
            lenght = int(input('enter the lenght of the generated password: '))
            if lenght > 0:
                return lenght
        except ValueError:
            print('Must be a number .')


def password_generator():
    char = str.ascii_letters + str.digits
    lenght = random.randint(5,10)
    return "".join(sample(char,lenght))

def id_generator():
    return ''.join(sample(str.digits,6))

def password_verification():
    print('Set a password')
    while True:
        password = input(':')
        if len(password) < 6:
            print('password must contien at least 6 characters!')
        else:
            return password

def user_name_exist(name):
    data = sqlite3.connect('Sign_in/data/users.db')
    cursor = data.cursor()
    cursor.execute('SELECT * FROM users WHERE LOWER(name) = LOWER(?)',(name,))
    db = cursor.fetchall()
    if not db:
        return False 
    else :
        return True 
    

    
class user:
    def __init__(self):
        pass

    def create_table(self):
        self.connection = sqlite3.connect('Sign_in/data/users.db')
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        user_id TEXT,
        password TEXT,
        last_update TEXT)""")
        self.connection.commit()

    def create_account(self):
        name = input('Enter your name :').strip().title()
        self.create_table()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE LOWER(name) = LOWER(?)",(name,))
        db = cursor.fetchall()
        if not db:
            user_id = id_generator()
            user_password = password_generator()
            data = (
                name,
                user_id,
                user_password,
                datetime.now().strftime("%H:%M")

            )
            cursor.execute("INSERT INTO users(name,user_id,password,last_update) VALUES(?,?,?,?)",data)
            self.connection.commit()
            print('Account created ✅')
            print('🔻🔻🔻🔻🔻🔻')
            print(f'Your User ID : {user_id}')
            print(f'your password : {user_password}')
            print('Warning ⚠️: Do not share with anyone ')
            return
        else:
            print('name already exists ❌')

    def change_password(self):
        search_name = input('enter the name account: ').strip().title()
        self.create_table()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE LOWER(name) = LOWER(?)",(search_name,))
        rows = cursor.fetchall()
        if not rows:
            print("""user name doesn't exist ❗❗""")
            self.connection.close()
        else: 
            print('Enter the current passeword')
            user_password = input(':')
            for row in rows:
                if user_password == row[3]:
                    new_password = password_verification()
                    cursor.execute("UPDATE users SET password = ?,last_update = ? WHERE LOWER(name) = LOWER(?)",(new_password,datetime.now().strftime("%H:%M"),search_name))
                    self.connection.commit()
                    print('Password Updated ✅')
                    self.connection.close()
                    break

                     
                else :
                
                    print('password incorrect ❗')
                    self.connection.close()


    def log_in(self):
        user_name = input('Enter the user name: ').title().strip()
        self.create_table()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE LOWER(name) = LOWER(?)" ,(user_name,))
        rows = cursor.fetchall()
        if not rows:
            print("""user name doesn't exist ❗❗""")
            self.connection.close()
        else:
            password = input('enter the password: ')
            for row in rows:
                if password == row[3]:
                    print(f'Welcom {user_name} 🫡')
                    self.connection.close()
                    break
                else:
                    print('password incorrect ❌ ')
                    self.connection.close()



            

        






    




