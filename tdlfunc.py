def addtask (): 
    file = open ("tasks.txt", "a")
    task = input ("Enter a task: ")
    file.write (task + "\n")
    file.close ()

def vtask (): 
    file = open ("tasks.txt", "r")
    tasks = file.readlines()
    for i, task in enumerate(tasks):
        print (f"{i+1}. {task}", end = "")
    file.close ()

def edtask ():
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

def deltask ():
    file = open ("tasks.txt", "r")
    tasks = file.readlines()
    file.close ()
    print ("Current tasks:")
    for i, task in enumerate(tasks):
        print (f"{i+1}. {task}", end = "")
    delete_index = int(input("\nEnter the number of the task to delete: ")) - 1
    if 0 <= delete_index < len(tasks):
        del tasks[delete_index]
        file = open ("tasks.txt", "w")
        file.writelines(tasks)
        file.close ()

def comptask (): 
    file = open ("tasks.txt", "r")
    tasks = file.readlines()
    file.close ()
    print ("Current tasks:")
    for i, task in enumerate(tasks):
        print (f"{i+1}. {task}", end = "")
    complete_index = int(input("\nEnter the number of the task to mark as complete: ")) - 1
    if 0 <= complete_index < len(tasks):
        completed_task = tasks[complete_index].strip() + " (Completed)\n"
        tasks[complete_index] = completed_task
        file = open ("tasks.txt", "w")
        file.writelines(tasks)
        file.close ()
    vtask() # Display the updated list of tasks after marking one as complete

def extask (): 
    print ("Exiting the program.")
    exit()