import sqlite3
from datetime import datetime 
        


def create_table():
    data = sqlite3.connect("TDLV2/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_list(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        task TEXT,
        status TEXT,
        date TEXT     ) """)
    data.close()

def add_task(name):
    create_table()
    task_name = input("Enter the task name : ")
    status = 'Pending'
    date = datetime.now().strftime("%H:%M")
    data = sqlite3.connect("TDLV2/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("INSERT INTO task_list(user_name,task,status,date) VALUES(?,?,?,?)",(name,task_name,status,date))
    data.commit()
    print("Task added successfully ✅")
    data.close()



def view_tasks(name):
    create_table()
    data = sqlite3.connect("TDLV2/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE user_name = ? ",(name,))
    db = cursor.fetchall()
    if not db:
        print("List is empty !")
    else:
        for row in db:
            print(row)
    
       

def delete_task(name):
    create_table()
    view_tasks(name)
    task_name = input("Enter the name of the task : ")
    data = sqlite3.connect("to_do_list/task.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE LOWER(task) = LOWER(?) AND user_name = ? ",(task_name,name))
    db = cursor.fetchall()
    if not db :
        print("Task does not exist ❗")
    else:
        cursor.execute("DELETE FROM task_list WHERE LOWER(task) = LOWER(?) AND user_name = ? ",(task_name,name))
        data.commit()
        print("Task deleted ✅")
        data.close()




def mark_done(name):
    create_table()
    data = sqlite3.connect("TDLV2/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE user_name = ?",(name,))
    db = cursor.fetchall()
    if not db :
        print("Liste is empty 🚫 .")
        data.close()
    else : 
        view_tasks(name)
        task_name = input("Enter the name of the task : ")
        data = sqlite3.connect("TDLV2/data/tasks.db")
        cursor = data.cursor()
        cursor.execute("SELECT * FROM task_list WHERE LOWER(task) = LOWER(?) AND user_name = ?",(task_name,name))
        db = cursor.fetchall()
        if not db :
            print("Task does not exist ❌")
        else:
            cursor.execute("UPDATE task_list SET status = 'done',date = ? WHERE LOWER(task) = LOWER(?) AND user_name = ?",(datetime.now().strftime("%H:%M"),task_name,name))
            
            data.commit()
            print("Task mark as done ✅")
            data.close()
  







