import sqlite3
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


class ContactManager:
    def __init__(self):
        self.connection = sqlite3.connect("contact_manager/contact.db")
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS contact_list(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        phone TEXT,
        email TEXT     ) """)
    def add_contact(self):
        cursor = self.connection.cursor()
        user_name = input("Enter the name : ")
        phone = input("enter the phone number : ")
        email = input("Enter the email : ")
        contact = (user_name,phone,email)
        cursor.execute("INSERT INTO contact_list(user_name,phone,email) VALUES(?,?,?)",contact)
        self.connection.commit()

    def view_contact(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM contact_list ")
        db = cursor.fetchall()
        if not db :
            print("Contact list is empty .")
        else:
            for row in db:
                print(row)

    def search(self):
        cursor = self.connection.cursor()
        searched_name = input("Enter the name : ")
        cursor.execute("SELECT * FROM contact_list WHERE LOWER(user_name) = LOWER(?)",(searched_name,))
        db = cursor.fetchall()
        if not db:
            print("Contact does not exist")
        else:
            for row in db :
                print(row)
    def delete_contact(self):
        deleted_name = input("Enter the name you want to delete it : ")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM contact_list WHERE LOWER(user_name) = LOWER(?)",(deleted_name,))
        db = cursor.fetchall()
        if not db :
            print("Contact does not exist !")
        else :
            cursor.execute("DELETE FROM contact_list WHERE LOWER(user_name) = LOWER(?)",(deleted_name,) )
            self.connection.commit()
            print('Contact Deleted')

    def update_contact(self):
        cursor = self.connection.cursor()
        name = input('enter the name you want to change it :')
        cursor.execute("SELECT * FROM contact_list WHERE LOWER(user_name) = LOWER(?)",(name,))
        db = cursor.fetchall()
        if not db:
                print('Contact does not exist !')  
        else:
                print("Choose the operation :")
                print("1-Change Phone number .")
                print("2-Change Email .")
                choice = int(input("Enter your choice "))
                if choice == 1:
                    new_phone = input("Enter the new phone number :")
                    update =(new_phone,name) 
                    cursor.execute("UPDATE contact_list SET phone = ? WHERE LOWER(user_name) = LOWER(?) ",update)
                    self.connection.commit()
                    print("Contact updated")
                elif choice == 2:
                    new_email = input("Enter the new email :")
                    update = (new_email,name)
                    cursor.execute("UPDATE contact_list SET email = ? WHERE LOWER(user_name) = LOWER(?) ",update)
                    self.connection.commit()
                    print("Email updated")
                else : 
                    print('invalid choice')
                    


    










        






         