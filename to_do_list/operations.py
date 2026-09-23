import sqlite3
from datetime import datetime 
        


def create_table():
    data = sqlite3.connect("to_do_list/data/tasks.db")
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
    task_name = input("Enter the task name : ").title().strip()
    data = sqlite3.connect("to_do_list/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE user_name = ? AND task = ?",(name,task_name))
    db = cursor.fetchall()
    if not db : 
            status = 'Pending'
            date = datetime.now().strftime("%H:%M")
            cursor.execute("INSERT INTO task_list(user_name,task,status,date) VALUES(?,?,?,?)",(name,task_name,status,date))
            data.commit()
            print("Task added successfully ✅")
            data.close()
            return        
    else:
            print("Task already exist ❗❗")
            data.close()
            return



def view_tasks(name):
    create_table()
    data = sqlite3.connect("to_do_list/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE user_name = ? ",(name,))
    db = cursor.fetchall()
    if not db:
        print("List is empty ❗")
    else:
        i = 1
        for row in db:
            print(f'task {i:<1} : {row[2]:<8}, status :{row[3]:<7} , last update at {row[4]}🔻')
            i += 1
    
       

def delete_task(name):
    create_table()
    view_tasks(name)
    task_name = input("Enter the name of the task : ")
    data = sqlite3.connect("to_do_list/data/tasks.db")
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
    data = sqlite3.connect("to_do_list/data/tasks.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM task_list WHERE user_name = ?",(name,))
    db = cursor.fetchall()
    if not db :
        print("Liste is empty 🚫 .")
        data.close()
    else : 
        view_tasks(name)
        task_name = input("Enter the name of the task : ").strip().title()
        data = sqlite3.connect("to_do_list/data/tasks.db")
        cursor = data.cursor()
        cursor.execute("SELECT * FROM task_list WHERE task = ? AND user_name = ?",(task_name,name))
        db = cursor.fetchall()
        if not db :
            print("Task does not exist ❌")
        else:
            cursor.execute("UPDATE task_list SET status = 'Done',date = ? WHERE task = ? AND user_name = ?",(datetime.now().strftime("%H:%M"),task_name,name))
            
            data.commit()
            print("Task mark as done ✅")
            data.close()
  







