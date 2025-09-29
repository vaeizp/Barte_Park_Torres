import calendar
from datetime import date

def display_homework_calendar(year, month, assignments):
    """
    Displays the calendar for a given month and year,
    highlighting days with homework assignments.
    """
    cal = calendar.monthcalendar(year, month)
    print(f"\n{' '.join(calendar.day_abbr)}\n") # Print day abbreviations

    for week in cal:
        for day in week:
            if day == 0: # Day 0 represents padding for days outside the month
                print("   ", end=" ")
            else:
                current_date = date(year, month, day)
                date_str = current_date.strftime("%Y-%m-%d")

                if date_str in assignments:
                    print(f"[{day:2}]", end="") # Highlight day with brackets
                else:
                    print(f"{day:3}", end=" ")
        print() # Newline for each week

    print("\nHomework Assignments:")
    for date_str, tasks in assignments.items():
        if date.fromisoformat(date_str).year == year and date.fromisoformat(date_str).month == month:
            print(f"{date_str}:")
            for task in tasks:
                print(f"  - {task}")

homework_assignments = {
    "2025-10-15": ["Math: Chapter 3 problems", "Science: Lab report due"],
    "2025-10-20": ["English: Essay draft", "History: Read Chapter 5"]
}
if 1 == 1:
    try:
        year = int(input("Enter year (e.g., 2025): "))
        month = int(input("Enter month (1-12): "))
        display_homework_calendar(year, month, homework_assignments)
    except ValueError:
        print("Invalid input. Please enter valid numbers for year and month.")