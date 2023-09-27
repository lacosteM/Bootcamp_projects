#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
            # Only 'admin' user can register new users
    
        # Only 'admin' user can register new users
        admin_username = "admin"
        entered_username = input("Enter your username: ")

        if entered_username == admin_username:
            new_username = input("Enter a new username: ")

            # Check if the new_username already exists in the user.txt file
            with open("user.txt", "r") as file:
                existing_users = [line.strip().split(":")[0] for line in file]

            if new_username in existing_users:
                print(f"Error: Username '{new_username}' already exists. Please try a different username.")
            else:
                new_password = input("Enter a new password: ")
                password_confirmation = input("Confirm the password: ")

                if new_password == password_confirmation:
                    with open("user.txt", "a") as file:
                        file.write(f"{new_username}:{new_password}\n")
                    print("User added successfully!")
                else:
                    print("Password confirmation failed. Please try again.")
        else:
            print("Only the 'admin' user can register new users.")

                


    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        


        # Prompt the user for task details
        assigned_username = input("Enter the username of the person the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Prepare the task data as a string
        task_data = f"{assigned_username}:{task_title}:{task_description}:{current_date}:{due_date}:No\n"

        # Add the task data to the tasks.txt file
        with open("tasks.txt", "a") as file:
            file.write(task_data)

        print("New task added successfully!")


    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        
        # Open the tasks.txt file in read mode
        with open("tasks.txt", "r") as file:
            # Read each line from the file and print task details
            for line in file:
                task_details = line.strip()
                line = line.split(", ")
                assigned_username, task_title, task_description, assigned_date, due_date, completed = task_details

                print("Task assigned to:", assigned_username)
                print("Task title:", task_title)
                print("Task description:", task_description)
                print("Date assigned:", assigned_date)
                print("Due date:", due_date)
                print("Completed:", completed)
                print()  # Adding an empty line for spacing between tasks




    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        
        user_logged_in = input("Enter your username: ")

        # Store user's tasks in a list
        user_tasks = []

        with open("tasks.txt", "r") as file:
            for line in file:
                task_details = line.strip().split(":")
                assigned_username, task_title, task_description, assigned_date, due_date, completed = task_details

                if user_logged_in == assigned_username:
                    user_tasks.append(task_details)

        if not user_tasks:
            print("You have no tasks.")
        else:
            print("Your tasks:")
            for i, task in enumerate(user_tasks, 1):
                task_title = task[1]
                task_description = task[2]
                completed_status = "Yes" if task[5] == "Yes" else "No"
                print(f"{i}. Task: {task_title}")
                print(f"   Description: {task_description}")
                print(f"   Due date: {task[4]}")
                print(f"   Completed: {completed_status}")
                print()

            # Prompt user to select a specific task
            while True:
                selected_task = input("Enter the number of the task you want to select (or -1 to return to the main menu): ")
                if selected_task == "-1":
                    break
                elif selected_task.isdigit():
                    selected_task_index = int(selected_task) - 1
                    if 0 <= selected_task_index < len(user_tasks):
                        selected_task_data = user_tasks[selected_task_index]

                        if selected_task_data[5] == "No":  # Check if the task is not completed
                            choice = input("Enter 'C' to mark the task as complete, 'E' to edit the task, or 'R' to return: ")
                            if choice.upper() == "C":
                                selected_task_data[5] = "Yes"
                                print("Task marked as complete.")
                            elif choice.upper() == "E":
                                new_assigned_date = input("Enter a new due date for the task (YYYY-MM-DD): ")
                                selected_task_data[4] = new_assigned_date
                                print("Task due date updated.")
                            elif choice.upper() == "R":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                        else:
                            print("This task is already completed and cannot be edited.")
                    else:
                        print("Invalid task number. Please try again.")
                else:
                    print("Invalid input. Please enter a number or -1.")

        
           

        

            
            # Prompt the user for their username
            user_logged_in = input("Enter your username: ")

            # Open the tasks.txt file in read mode
            with open("tasks.txt", "r") as file:
                # Read each line from the file and print matching user's tasks
                    for line in file:
                        task_details = line.strip().split(":")
                        assigned_username, task_title, task_description, assigned_date, due_date, completed = task_details

                        # Check if the username of the person logged in matches the assigned username
                        if user_logged_in == assigned_username:
                            print("Task assigned to:", assigned_username)
                            print("Task title:", task_title)
                            print("Task description:", task_description)
                            print("Date assigned:", assigned_date)
                            print("Due date:", due_date)
                            print("Completed:", completed)
                            print()  # Adding an empty line for spacing between tasks

    elif menu  == 'gr':
        pass
        total_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0

        # Calculate the statistics from the tasks.txt file
        with open("tasks.txt", "r") as file:
            for line in file:
                total_tasks += 1
                task_details = line.strip().split(":")
                completed = task_details[-1].strip()
                due_date = task_details[-2].strip()

                if completed == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    if datetime.datetime.strptime(due_date, "%Y-%m-%d").date() < datetime.date.today():
                        overdue_tasks += 1

        # Calculate percentages
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

        # Write the statistics to the task_overview.txt file
        with open("task_overview.txt", "w") as overview_file:
            overview_file.write(f"Total number of tasks: {total_tasks}\n")
            overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
            overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
            overview_file.write(f"Total number of tasks that are overdue: {overdue_tasks}\n")
            overview_file.write(f"Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%\n")
            overview_file.write(f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n")

        print("Task overview generated and saved to task_overview.txt")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")