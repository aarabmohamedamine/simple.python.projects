import sqlite3
from models import user_name_exist
def admin_validation():
    admin_access = ['admin','admin@2026']
    name = input('Enter your name: ').strip()
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
        data.close()

    


def admin_mod():
    success = admin_validation()
    if not success:
        print('Access declined ❌')
    else:
        print('Access aprouved ✅')
        print('------Dashbord------')
        choice = admin_choice()
        if choice == 1:
            view_users()
        elif choice == 2:
            delete_user()
        



admin_mod()
