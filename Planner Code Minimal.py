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
    print("1 - Add Task")
    print("2 - View Already Added Tasks")
    print("3 - Mark Complete a Task")
    print("4 - Exit the application")

    choice = input("Enter choice: ")

    # ---------------------------------
    # Add Task
    # ---------------------------------
    if choice == "1":

        print("\n↓↓↓↓↓↓↓↓↓↓↓↓\n")

        subject = input("Enter Subject: ")
        task_name = input("Task Name: ")
        requirement = input("Requirement Details: ")
        deadline = input("Deadline (MM/DD/YY): ")
        exact_time_deadline = input("Exact Time (HH:MM AM/PM): ")
        urgency = input("Urgency (Low/Medium/High): ")

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