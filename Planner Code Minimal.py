import json
from datetime import datetime
import time
import random

filename = "tasks.json"

# -------------------------
# Load tasks
# -------------------------
try:
    with open(filename, "r") as file:
        data = json.load(file)
        tasks = data["tasks"]
except FileNotFoundError:
    print("Error: The file 'tasks.json' was not found.")
except:
    tasks = []
    print("You currently have no tasks to finish.\n")


# -------------------------
# Main while loop
# -------------------------
print(" .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.")
time.sleep(0.25)
print(" | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
time.sleep(0.25)
print(" | |   ____       | || |   ___        | || |       _      | || |    ___  ___  | || |              | || |      __      | || |              | || |  ______      | || |     _ ,      | || |  ___    __   | || |      __      | |")
time.sleep(0.25)
print(" | |  |_   _ ,    | || |  |   |       | || |     / , \\    | || |  |   ,|_   | | || |              | || |   .'    `.   | || |              | || | |   _   ,    | || |    /   ,     | || | |  ,  /  _|  | || |     /  \\     | |")
time.sleep(0.25)
print(" | |  | |__) |    | || |   | |        | || |    / /,\\ \\   | || |  |   , | |   | || |    ______    | || |  /  .--.  ,  | || |    ______    | || |  | |__) |    | || |   / /,'  ,   | || | | | , /|  |  | || |    / /\\ ,    | |")
time.sleep(0.25)
print(" | |  |  __/      | || |  | |   _     | || |   /  ___, \\  | || |  | |, ,| |   | || |   |______|   | || |  | |    | |  | || |   |______|   | || |  |  _ /      | || |  /  ___   ,  | || | | |  , | |   | || |   / /__\\ \\   | |")
time.sleep(0.25)
print(" | |  | |         | || |  | |__/ |    | || | _/ /_   ,  \\ | || | | |,   |_ _  | || |              | || |  ,  `--'  /  | || |              | || |  | |  , |_   | || | /  /   /   , | || | | |, _|  |_  | || | _/ /    , ,_ | |")
time.sleep(0.25)
print(" | |  |_____|     | || |  |________|  | || ||____|  |____|| || | |___|,____|  | || |              | || |   `.____.'   | || |              | || | |___|  |___| | || ||____|  |____|| || ||_____||_____|| || ||____|  |____|| |")
time.sleep(0.25)
print(" | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
time.sleep(0.25)
print(" | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
time.sleep(0.25)
print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'")
a = True
print("Welcome...")
time.sleep(0.5)
print("To PLAN-O-RAMA!")
time.sleep(0.15)
print("\n")

time.sleep(1.5)
print("=" * 100)  # Cute little loading bar I wanted to add
print("Loading tracker assets")
print("\nPlease wait")
count = 0
bar_length = 10
while count < bar_length:
    w = random.randint(1,3)
    print("█", end="█")
    time.sleep((w - 0.5))
    count += 1
while a == True:

    print("\nWelcome, humble student! What would you like to do?")
    print("\n")
    time.sleep(1)
    print("1 - Add Task")
    time.sleep(0.5)
    print("2 - View Already Added Tasks")
    time.sleep(0.5)
    print("3 - Mark Complete a Task")
    time.sleep(0.5)
    print("4 - Exit the application")
    time.sleep(2)
    print("")

    choice = input("Enter choice (Please ensure you input the number!): ")

    # ---------------------------------
    # Add Task
    # ---------------------------------
    if choice == "1":

        print("\n↓↓↓↓↓↓↓↓↓↓↓↓\n")
        time.sleep(1)
        print("You have chosen")
        time.sleep(0.2)
        print("Add Task")
        time.sleep(0.2)

        # -------------------------
        # Subject (anything can be inputted, not empty)
        # -------------------------
        while True:
            subject = input("Enter Subject: ")
            if subject:
                break
            else:
                print("Oopsies! Subject cannot be empty! Let's try that again!")
                time.sleep(1)

        time.sleep(0.5)

        # -------------------------
        # Task Name (anything can be inputted, not empty)
        # -------------------------
        while True:
            task_name = input("Task Name: ")
            if task_name:
                break
            else:
                print("Whoops! Task name cannot be empty! Let's try that again!")
                time.sleep(1)

        time.sleep(0.5)

        # -------------------------
        # Requirement Details (this is completely optional, but i cleaned it up to match the format)
        # -------------------------
        requirement = input("Requirement Details: ")
        time.sleep(0.5)

        # -------------------------
        # Deadline (format is strictly MM/DD/YY)
        # -------------------------
        while True:
            deadline = input("Deadline (MM/DD/YY): ")
            try:
                datetime.strptime(deadline, "%m/%d/%y") # .strptime helps convert a string representation of a specific date into a Python object (datetime)
                break
            except ValueError:
                print("Wait! Use the format MM/DD/YY (e.g., 04/15/26). Let's do that again!")
                time.sleep(1)

        time.sleep(0.5)

        # -------------------------
        # Exact Time (format is strictly HH:MM AM/PM)
        # -------------------------
        while True:
            exact_time_deadline = input("Exact Time (HH:MM AM/PM): ")
            if exact_time_deadline == "":
                exact_time_deadline = "N/A"
                break
            try:
                datetime.strptime(exact_time_deadline, "%I:%M %p")
                break
            except ValueError:
                print("Hold up! Use HH:MM AM/PM. Please do not use the 24-hour time format. Let's try that again!")
                time.sleep(1)

        time.sleep(0.5)

        # -------------------------
        # Urgency (choices are limited to Low, Medium, or High)
        # -------------------------
        while True:
            urgency = input("Urgency (Low/Medium/High): ").capitalize()
            if urgency in ["Low", "Medium", "High"]:
                break
            else:
                print("That's not part of the choices! D: Choose Low, Medium, or High.")
                time.sleep(1)

        time.sleep(0.5)

        status = "Pending"

        task = {
            "subject": subject,
            "task_name": task_name,
            "requirement": requirement,
            "deadline": deadline,
            "time": exact_time_deadline,
            "urgency": urgency,
            "status": status
        }

        tasks.append(task)
        
        with open(filename, "w") as file:
            json.dump({"tasks": tasks}, file, indent=4)

        print("\nTask added successfully!")
        print("I pray your productivity comes alive and well!\n")

    elif choice == "2":
        print("You chose: \nList of Tasks")

        if len(tasks) == 0:
            print("You've accomplished all your tasks. So proud of you!")
        else:
            print(tasks)

    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to complete. Keep up the good work!")
        else:
            task_accom = int(input("Enter the number of the completed task: "))

            if 0 < task_accom <= len(tasks):
                tasks[task_accom - 1]["status"] = "Completed"

                with open(filename, "w") as file:
                    json.dump({"tasks": tasks}, file, indent=4)

                print("\nCUE THE CONFETTI!")
                print("Task completed! Congratulations!")
            else:
                print("That task number does not exist. Please enter another number.")
                time.sleep(1)
                print("Returning to main menu...")
    elif choice == "4":
        print(f"Terminating the Program", end="")
        time.sleep(0.5)
        print(f".", end="")
        time.sleep(0.5)
        print(f".", end="")
        time.sleep(0.5)
        print(f".", end="")
        time.sleep(1)
        a = False
