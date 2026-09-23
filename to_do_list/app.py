import accounts
import operations




def main():
    current_user = None

    while current_user is None:
        while True:
            print("\n1. Sign In (Create Account)")
            print("2. Log In")
            print("3. Exit")

            try :
                choices = [i for i in range(1,4)]
                choice = int(input('Enter choice: '))
                if choice in choices:
                    break 
                else :
                    print('Invalid choice ❌')
            except ValueError:
                print('must be number ❌')



        if choice == 1:
            accounts.sign_in()
        elif choice == 2:
            current_user = accounts.log_in()
        elif choice == 3:
            print("Goodbye!")
            return

    while True:
        while True:    

            try :
                print(f"\n--- To-Do List ({current_user}) ---")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Mark Done")
                print("4. Delete Task")
                print("5. Log Out")

                choices = [i for i in range(1,6)]
                task_choice = int(input('Enter choice: '))
                if task_choice in choices:
                    break 
                else :
                    print('Invalid choice ❌')
            except ValueError:
                print('must be number ❌')


        if task_choice == 1:
            operations.add_task(current_user)
        elif task_choice == 2:
            operations.view_tasks(current_user)
        elif task_choice == 3:
            operations.mark_done(current_user)
        elif task_choice == 4:
            operations.delete_task(current_user)
        elif task_choice == 5:
            print("Logged out successfully.")
            break

if __name__ == "__main__":
    main()