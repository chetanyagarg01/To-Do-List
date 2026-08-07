import tdlfunc
tdl = 1 
while tdl == 1:
    print ("1. Add a task, 2. View tasks, 3. Edit a task, 4. Delete a task, 5. Exit")
    choice = input ("Enter your choice: ")
    if choice == "1":
        file = open ("tasks.txt", "a")
        task = input ("Enter a task: ")
        file.write (task + "\n")
        file.close ()
    elif choice == "2":
        file = open ("tasks.txt", "r")
        tasks = file.readlines()
        for i, task in enumerate(tasks):
            print (f"{i+1}. {task}", end = "")
        file.close ()
    elif choice == "3":
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
    elif choice == "4":
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
    elif choice == "5":
        tdl = 0 
        print ("Exiting the program.")
        break
    else:
        print ("Invalid choice. Please try again.")
    tdl = int(input("\nDo you want to continue? (1 for Yes, 0 for No): "))
    if tdl == 0:
        print ("Exiting the program.")
        break 
    
