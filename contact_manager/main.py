from operations import valid_choice , ContactManager

def main():
    manager = ContactManager()
    while True :
        choice = valid_choice()
        if choice == 1 :
            manager.add_contact()
        elif choice == 2:
            manager.view_contact()
        elif choice == 3:
               manager.search()
        elif choice == 4:
            manager.delete_contact()
        elif choice == 5:
            manager.update_contact()
            
        elif choice == 6:
            break
        else : 
            print("invalid choice")


main()

