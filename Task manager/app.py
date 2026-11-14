import streamlit as st
import time
class Task:
    def __init__(self,name):
        self.name = name
        self.completed = False
    def complete(self):
        self.completed = True
    def uncomplete(self):
        self.completed = False

if "tasks" not in st.session_state: #Saves tasks bc stupid streamlit reruns the file every time you interact w something.
    st.session_state["tasks"] = [] 
if "ctasks" not in st.session_state:
    st.session_state["ctasks"] = []

if "tasks_completed" not in st.session_state:
    st.session_state["tasks_completed"] = 0

tasklist = st.session_state["tasks"]

ctask = st.session_state["ctasks"]

# tasks_completed = st.session_state["tasks_completed"]

st.title("Task Manager")
st.write("lowk feel like im larping streamlit")

add = st.button("➕ Add task")
remove = st.button("➖ Remove task")
removeall = st.button("⚠️ Remove all tasks")
task = st.text_input("Enter a task").strip().capitalize()

def task_sys(task,tasklist): #how to add/remove tasks without dupes/blanks.
    if removeall == True: #removing all tasks
        if tasklist == []:
            st.write("No tasks to delete!")
        else:
            tasklist.clear()
            st.write("Deleted all tasks!")
            return
    if task == "":
        pass
    else:
        if add == True:
            duplicate = False

            for existing_task in tasklist:
                if existing_task.name == task:
                    duplicate = True

            if duplicate == True:
                st.write("Task already exists!")
            else:
                new_task = Task(task)
                tasklist.append(new_task)
                st.write(f"Added {task}!")
    if remove == True:
        found = False

        for existing_task in tasklist:
            if existing_task.name == task:
                found = True
                tasklist.remove(existing_task)

        if found == True:
            st.write(f"Removed {task}!")
        else:
            st.write(f"{task} does not exist!")

task_sys(task,tasklist)


if tasklist == []: # *** Task displaying ***
    st.header("No tasks!")
else: # ***Tasks not finished***
    st.header("Your tasks:")
    total_tasks = len(tasklist)
    st.subheader(f"{total_tasks} Tasks.")
    for i, taskk in enumerate(tasklist): #***Taskk == 
        i += 1
        checked = st.checkbox(taskk.name, key=f"task_{i}") # ***Task check if its done or not***
        if checked == True:
            taskk.complete()
        elif checked == False:
            taskk.uncomplete()
        else:
           pass
            

        st.write(taskk.completed)


tasks_completed = 0

for a in tasklist:
    if a.completed:
        tasks_completed += 1

ttask = len(tasklist)

st.write(f"{tasks_completed} / {ttask} tasks completed.")

if ctask == []:
    st.header("No completed tasks.")
else:   
    if task.completed == True:
        st.header("Finished tasks:")
        ctask.append(task)
        tasklist.remove(task)

        for i, tassk in ctask:
            i += 1
            st.markdown(tassk)




