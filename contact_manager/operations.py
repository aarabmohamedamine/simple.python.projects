import sqlite3
import datetime as d
def display_menu():

    print('1.Add contact ')
    print('2.View all contacts')
    print('3.Search for a contact')
    print('4.Delete a contact')
    print('5.Update contact')
    print('6.Exit')
def valid_choice():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice : "))
            return choice
        except ValueError :
            print('Try again !!')
def create_table():
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS contact_list(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        phone TEXT,
        email TEXT     ) """)
    data.close()
   


def add_contact():
    create_table()
    user_name = input("Enter the name : ")
    phone = input("enter the phone number : ")
    email = input("Enter the email : ")
    contact = (user_name,phone,email)
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("INSERT INTO contact_list(user_name,phone,email) VALUES(?,?,?)",contact)
    data.commit()
    print("Contact added successfully !! ")
    data.close()
    
def view_contact():
    create_table()
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM contact_list")
    db = cursor.fetchall()
    for row in db:
        print(row)
    data.commit()
    data.close()
    
    
def search():
    
    name = input('Enter the Name : ')
    create_table()
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM contact_list WHERE user_name = ?",(name,))
    db = cursor.fetchall()
    for row in db :
        print(row)
    data.commit()
    data.close()
    print("contact deleted !")



def delete_contact():
    create_table()
    name = input("Enter the name you want to delete it : ")
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("DELETE FROM contact_list WHERE user_name = ? ",(name,))
    data.commit()
    data.close()

def update_contact():
    create_table()
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    name = input('enter the name you want to change it :')
    cursor.execute("SELECT * FROM contact_list WHERE user_name = ?",(name,))
    db = cursor.fetchall()
    if not db:
            print('Contact does not exist !')
            return 
    else:
            print("Choose the operation :")
            print("1-Change Phone number .")
            print("2-Change Email .")
            while True:
                try:
                   choice = int(input("Enter your choice : "))
                   break    
                except ValueError :
                    print('Try again !!')

            if choice == 1:
               new_phone = input("Enter the new phone number :")
               update =(new_phone,name) 
               cursor.execute("UPDATE contact_list SET phone = ? WHERE user_name = ? ",update)
               data.commit()
               print("Contact updated")
               data.close()
               return
            
            elif choice == 2:
               new_email = input("Enter the new email :")
               update = (new_email,name)
               cursor.execute("UPDATE contact_list SET email = ? WHERE user_name = ? ",update)
               data.commit()
               print("Email updated")
               data.close()
               return
            else : 
                print('invalid choice')
                return


        










