from models import user
from admin import admin_mod

def display_menu():
    print('-'*50)
    print('1.Create acount.')
    print('2.Log in ')
    print('3.change password .')
    print('4.Admin mode .')
    print('5.exit')

def valid_choice():
    display_menu()
    choices = [i for i in range(1,6)]
    while True:
        try :
            choice = int(input(":"))
            if choice in choices:
                return choice
            else :
                print('Invalid choice ⚠️')
        except ValueError:
            print('Must me a number')



def main():

    User = user()
    while True : 
        choice = valid_choice()
        if choice == 1:
            User.create_account()
        elif choice == 2:
            User.log_in()
        elif choice == 3:
            User.change_password()
        elif choice == 4:
            admin_mod()
        elif choice == 5:
            print('Good bye 🫡')
            break
        


main()