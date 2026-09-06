import sqlite3

import datetime as d
def display_menu():

    print('1.Add contact ')
    print('2.View all contacts')
    print('3.Search for a contact')
    print('4.Delete a contact')
    print('5.Exit')
def valid_choice():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice : "))
            return choice
        except ValueError :
            print('Try again !!')
    while True :
        try :            
            contact_index = int(input("enter the contact index : "))
            if contact_index > 0 and contact_index <= len(contact_list):
                return contact_index-1
                
            else :  
                print('number invalid')
        except ValueError:
            print("error.")
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
    data.close
    print("contact deleted !")



def delete_contact():
    create_table()
    name = input("Enter the name you want to delete it : ")
    data = sqlite3.connect("contact_manager/contact.db")
    cursor = data.cursor()
    cursor.execute("DELETE FROM contact_list WHERE user_name = ? ",(name,))
    data.commit()
    data.close()
