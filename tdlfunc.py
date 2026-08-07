def addtask (): 
    file = open ("tasks.txt", "a")
    task = input ("Enter a task: ")
    file.write (task + "\n")
    file.close ()

def viewtasks (): 
    file = open ("tasks.txt", "r")
    tasks = file.readlines()
    for i, task in enumerate(tasks):
        print (f"{i+1}. {task}", end = "")
    file.close ()

def edittask ():
    file = open ("tasks.txt", "r")
    tasks = file.readlines()
    file.close ()
    print ("Current tasks:")
    for i, task in enumerate(tasks):
        print (f"{i+1}. {task}", end = "")
    edit_index = int(input("\nEnter the number of the task to edit: ")) - 1
    if 0 <= edit_index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[edit_index] = new_task + "\n"
        file = open ("tasks.txt", "w")
        file.writelines(tasks)
        file.close ()