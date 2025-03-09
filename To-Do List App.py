print("Welcome to To-Do List!") # Welcome

tasks = [] # Tasks array
tasksCompleted = 0 # Completed tasks

# Viewing task function
def view_task():
    # Outputting tasks line by line
    for task in tasks:
        print(f"{task}") 

# Adding task function
def add_task():
    while True:
        add = input("Type in a task to add it and type 'exit' when finished: ") # User can add tasks
        # When user is done adding tasks
        if add.lower() == "exit":
            print("List has been updated.")
            break
        # When user adds a task
        else:
            print("Task added!")
            tasks.append(add)

# Deleting task function
def delete_task():
    while True: 
        # Outputting tasks line by line
        for task in tasks:
            print(f"{task}")

        delete = int(input("Enter the task number you want to delete and type 0 when finished: ")) # User can delete tasks
        # Deleting tasks if there input is valid
        if delete <= len(tasks)+1 and delete >= 1 and delete != 0:
            print("Task deleted!")
            tasks.pop(delete-1)
        # User is done deleting tasks
        elif delete == 0:
            print("List has been updated.")
            break

# Completing task function
def complete_task():
    global tasksCompleted # Making tasks completed global so it can be accessed
    while True:
        # All tasks completed
        if len(tasks) == 0:
            print("Well done! You have completed all of your", tasksCompleted, "tasks today...")
            exit()

        # Outputting tasks line by line
        for task in tasks:
            print(f"{task}")

        completeIndex = int(input("Enter the task number you have completed(press 0 to exit): ")) # User can complete a task
        # User wants to leave app
        if completeIndex == 0:
            print("Hope to see you again!")
            exit()
        # Completing task if user input is valid
        elif completeIndex <= len(tasks)+1 and completeIndex >= 1 and completeIndex != 0:
            tasks.pop(completeIndex - 1)
            tasksCompleted += 1


add_task() # Calling function to add tasks
view_task() # Calling function to view tasks
# Giving a chance to delete tasks
deleteQuestion = input("Do you want to delete a task(yes/no)? ")
if deleteQuestion.lower() == "yes":
    delete_task()
complete_task() # Calling function to complete tasks