import tdlfunc
tdl = 1 
while tdl == 1:
    print ("1. Add a task, 2. View tasks, 3. Edit a task, 4. Delete a task, 5. Mark task as complete, 6. Exit")
    choice = input ("Enter your choice: ")
    if choice == "1":
        tdlfunc.addtask()
    elif choice == "2":
        tdlfunc.vtask()
    elif choice == "3":
        tdlfunc.edtask()
    elif choice == "4":
        tdlfunc.deltask()
    elif choice == "5":
        tdlfunc.comptask()
    elif choice == "6":
        tdlfunc.extask()
        break 
    else:
        print ("Invalid choice. Please try again.")
    print ("\ncontinuing the program.")
    if tdl != 1:
        print ("Exiting the program.")
        break
    
