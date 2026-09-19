import sqlite3
from models import user_name_exist,id_generator
from datetime import datetime

def create_data():
        connection = sqlite3.connect('Sign_in/data/users.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        user_id TEXT,
        password TEXT,
        last_update TEXT)""")
        connection.commit()
        connection.close()




def admin_validation():
    admin_access = ['admin','admin@2026']
    name = input('Enter admin user: ').strip()
    password = input("Enter the password: ")
    if name == admin_access[0]:
        if password == admin_access[1]:
            return True
        else:
            return False
    else:
        return False

    
def admin_choice():
    admin_menu()
    choices = [i for i in range(1,6)]
    while True:
        try :
            choice = int(input(":"))
            if choice in choices:
                return choice
        except ValueError:
            print('Must me a number')


def admin_menu():
    print('1.View users ')
    print('2.Delete user  ')
    print('3.update user .')
    print('4.add user .')
    print('5.exit')


def view_users():
    data = sqlite3.connect('Sign_in/data/users.db')
    cursor = data.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if not rows:
        print('Users list empty❗')
    else:
        for row in rows:
            print(row)

    data.close()


def delete_user():
    name = input('Enter the name:').strip().title()
    success = user_name_exist(name)
    if not success:
        print('User not founded ❌')
    else:
        data = sqlite3.connect('Sign_in/data/users.db')
        cursor = data.cursor()
        cursor.execute("DELETE FROM users WHERE name = ?",(name,))
        data.commit()
        print('User deleted ✅')
        data.close()


def update_user():
    name = input('Enter the name: ').strip().title()
    success = user_name_exist(name)
    if not success :
        print('User not founded ❌ ')
    else:
        data = sqlite3.connect('Sign_in/data/users.db')
        cursor = data.cursor()
        while True:
            print('1.change user name')
            print('2.change password')
            try :
                choice = int(input(':'))
                break
            except ValueError:
                print('must be a number')     

        if choice == 1:
            new_name = input('Enter the new name: ').title().strip()
            cursor.execute("UPDATE users SET name = ? WHERE name = ?",(new_name,name))
            data.commit()
            print("User name updated ✅")
            data.close()
        elif choice == 2:
            new_password = input('Enter the new password: ')
            cursor.execute("UPDATE users SET password = ? WHERE name = ?",(new_password,name))
            data.commit()
            print("Password updated ✅")
            data.close()
        else:
            print("Invalid choice ⚠️")
            data.close()


def add_user():
    user_name = input('Add user name: ').strip().title()
    user_password = input('Add user password: ')
    user_id = id_generator()
    time = datetime.now().strftime("%H:%M")
    data = sqlite3.connect('Sign_in/data/users.db')
    cursor = data.cursor()
    cursor.execute("INSERT INTO users (name,user_id,password,last_update) VALUES(?,?,?,?)",(user_name,user_id,user_password,time))
    data.commit()
    print('User added ✅')
    data.close()



def admin_mod():
    create_data()
    success = admin_validation()
    if not success:
        print('Access declined ❌')
    else:
        print('Access aprouved ✅')
        while True:
            print('------Dashbord------')
            choice = admin_choice()
            if choice == 1:
                view_users()
            elif choice == 2:
                delete_user()
            elif choice == 3:
                update_user()
            elif choice == 4:
                add_user()
            elif choice == 5:
                print('Good bye Admin 🫡')
                break
            

        




