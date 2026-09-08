from operation import add_task,view_tasks,mark_done,delete_task,clear_tasks




def display_menu():
    print("------Menu------")
    print("1.add task ")
    print("2.View task")
    print("3. Mark Task as Done")
    print("4.delete task")
    print("5.clear all")
    print("6.exit")
    return 



def main():

    while True :
        display_menu()
        try :
            choice = int(input("enter your choice : ")) 
        except ValueError :
            print("try again !! ")
            continue
        if choice == 1:
            add_task()
        elif choice == 2:
                view_tasks()
        elif choice == 3:
                mark_done()  
        elif choice == 4:
                delete_task()
        elif choice == 5:
                clear_tasks()
        elif choice == 6 :
            break
        else :
            print("invalid choice")
 
main()