#TASK 1 To Do List

#importing packages
import tkinter
import tkinter.messagebox
import pickle

window=tkinter.Tk()
window.title("Own to do list")

def task_adding():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!",messasge="To add a task,please enter some task !!")
        
def task_removing():
    try:
        index_todo=list_frame.curselection()[0]
        list_frame.delete(index_todo)
        
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="To delete a task,you must select a task !!")

def task_load():
    try:
        todo_task=pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter,END)
        for todo in tasks:
            list_frame.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="Cannot find task.dat")
        
def task_save():
    todo_list=list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("tasks.dat","wb"))
    
    
list_frame=tkinter.Frame(window)
list_frame.pack()

todo_box=tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)

scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)

task_add=tkinter.Entry(window,width=60)
task_add.pack()

add_task_button=tkinter.Button(window,text="CLICK TO ADD TASK",font=("arial",10,"bold"),background="red",width=35,command=task_adding)
add_task_button.pack()

remove_task_button=tkinter.Button(window,text="CLICK TO DELETE TASK",font=("arial",18,"bold"),background="green",width=28,command=task_removing)
remove_task_button.pack()

load_task_button=tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",15,"bold"),background="yellow",width=26,command=task_load)
load_task_button.pack()

save_task_button=tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",25,"bold"),background="blue",width=30,command=task_save)
save_task_button.pack()

window.mainloop()