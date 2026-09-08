import sqlite3
from datetime import datetime 
def create_table():
    data = sqlite3.connect("to_do_list/tasks.db")
    cursor = data.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_list(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        status TEXT,
        date TEXT     ) """)
    data.close()

def add_task():
    create_table()
    task_name = input("Enter the task name : ")
    status = 'Pending'
    date = datetime.now().strftime("%H:%M")
    data = sqlite3.connect("to_do_list/tasks.db")
    cursor = data.cursor()
    cursor.execute("INSERT INTO task_list(task,status,date) VALUES(?,?,?)",(task_name,status,date))
    data.commit()
    print("Task added successfully !")
    data.close()



def view_tasks():
    create_table()
    data = sqlite3.connect("to_do_list/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list ")
    db = cursor.fetchall()
    if not db:
        print("List is empty !")
    else:
        for row in db:
            print(row)
    
       

def delete_task():
    create_table()
    view_tasks()
    name = input("Enter the name of the task : ")
    data = sqlite3.connect("to_do_list/task.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE LOWER(task) = LOWER(?)",(name,))
    db = cursor.fetchall()
    if not db :
        print("Task does not exist !")
    else:
        cursor.execute("DELETE FROM task_list WHERE LOWER(task) = LOWER(?)",(name,))
        data.commit()
        print("Task deleted")
        data.close()




def mark_done():
    create_table()
    data = sqlite3.connect("to_do_list/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list")
    db = cursor.fetchall()
    if not db :
        print("Liste is empty ! .")
        data.close()
    else : 
        view_tasks()
        name = input("Enter the name of the task : ")
        data = sqlite3.connect("to_do_list/tasks.db")
        cursor = data.cursor()
        cursor.execute("SELECT * FROM task_list WHERE LOWER(task) = LOWER(?)",(name,))
        db = cursor.fetchall()
        if not db :
            print("Task does not exist !")
        else:
            cursor.execute("UPDATE task_list SET status = 'done' WHERE LOWER(task) = LOWER(?)",(name,))
            data.commit()
            print("Task mark as done!")
            data.close()
  
def clear_tasks():
        create_table()
        data = sqlite3.connect("to_do_list/tasks.db")
        cursor = data.cursor()
        cursor.execute("DROP TABLE task_list")
        data.commit()
        print("All clear !! ")
        data.close()









