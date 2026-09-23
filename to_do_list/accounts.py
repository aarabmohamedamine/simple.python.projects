import sqlite3
from datetime import datetime

def data_user_table():
    data = sqlite3.connect('to_do_list/data/users.db')
    cursor = data.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    password TEXT,
    time TEXT
    )""")
    data.commit()
    data.close()

def name_existing(name):
    data = sqlite3.connect('to_do_list/data/users.db')
    cursor = data.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?",(name,))
    names = cursor.fetchall()
    if not names:
        return False
    else :
        return True

   

def sign_in():
    data_user_table()
    print('Welcom to our app 😊')
    print('-----Sign in ------')
    while True:
        name = input('Enter your name: ').strip()
        if name_existing(name):
            print('User name already exist ❌')
            print('Try another one.')
        else:
            break


    while True:
        password = input('Set your password: ')
        if len(password)<6:
            print('Password must contient 6 characters at least ⚠️ .')
        else:
            password1 = input('confirme your password: ')
            if password == password1:
                break
            else:
                print('Try again❗')



    data = sqlite3.connect('to_do_list/data/users.db')
    cursor = data.cursor()
    cursor.execute("INSERT INTO users(name,password,time) VALUES(?,?,?)",(name,password,datetime.now().strftime("%H:%M")))
    data.commit()
    print("account created ✅")
    print(f'Welcom {name}')
    data.close()
    return name


def log_in():
    data_user_table()
    print('------Log in------')
    name = input('Enter your user name: ')
    data = sqlite3.connect('to_do_list/data/users.db')
    cursor = data.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?",(name,))
    names = cursor.fetchall()
    if not names:
        print("""User name doesn't exist ❗""")
        data.close()
        return None
        
    else:
        attempts = 0
        while attempts < 3:
            password = input('enter the password: ')
            attempts +=1
            for row in names:
                    if password == row[1]:
                        print(f'Welcom {name} 🫡')
                        data.close()
                        return name
                    else:
                        print('password incorrect ❌ ')
                        print('Try again')
                        data.close()

                    

            print('Account temporarily locked 🚫')
            
    
  
        

       






