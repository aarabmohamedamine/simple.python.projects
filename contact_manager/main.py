from operations import add_contact,view_contact,search,valid_choice,delete_contact,update_contact

def main():
    
    while True :
        choice = valid_choice()
        if choice == 1 :
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
               search()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            update_contact()
            
        elif choice == 6:
            break
        else : 
            print("invalid choice")


main()

