"""
Placement Readiness Tracker
IRP-II (CSE2596) Assignment - Tasks 1 and 2.
"""

# Each student is a dictionary; all students are stored in a list.
students = [
    {"name": "Aarav Sharma", "roll_no": 101, "aptitude": 82, "verbal": 76, "coding": 91},
    {"name": "Diya Verma",   "roll_no": 102, "aptitude": 64, "verbal": 70, "coding": 58},
    {"name": "Kabir Singh",  "roll_no": 103, "aptitude": 45, "verbal": 52, "coding": 38},
    {"name": "Meera Iyer",   "roll_no": 104, "aptitude": 30, "verbal": 35, "coding": 28},
    {"name": "Rohan Gupta",  "roll_no": 105, "aptitude": 90, "verbal": 85, "coding": 88},
]


def read_score(subject):
    """Keep asking until the user enters a whole number between 0 and 100."""
    while True:
        text = input(f"Enter {subject} score (0-100): ")
        try:
            score = int(text)              # input() gives str, so convert to int
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= score <= 100:
            return score
        print("  Score must be between 0 and 100. Try again.")


def add_student_from_input(students):
    """Read one more student from the keyboard and add it to the list."""
    name = input("Enter student name: ").strip()
    while True:
        try:
            roll_no = int(input("Enter roll number: "))
            break
        except ValueError:
            print("  Roll number must be a number.")
    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    students.append(student)


def average(student):
    """Return the mean of the three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Return the grade for an average score."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average."""
    best = students[0]
    for s in students:
        if average(s) > average(best):
            best = s
    return best


def needs_practice(students, limit=40):
    """Return the students whose average is below limit (default 40)."""
    weak = []
    for s in students:
        if average(s) < limit:
            weak.append(s)
    return weak


def print_table(students):
    """Print a neatly formatted result table using a loop."""
    print(f"{'Name':<16}{'Roll':<7}{'Apt':>5}{'Verbal':>8}{'Coding':>8}{'Average':>9}  Grade")
    print("-" * 68)
    for s in students:
        avg = average(s)
        print(f"{s['name']:<16}{s['roll_no']:<7}{s['aptitude']:>5}{s['verbal']:>8}"
              f"{s['coding']:>8}{avg:>9.2f}  {grade(avg)}")


def main():
    add_student_from_input(students)
    print("\n=== Result Table ===")
    print_table(students)

    top = top_scorer(students)
    print(f"\nTop scorer: {top['name']} (roll {top['roll_no']}) with average {average(top):.2f}")

    print("\nNeeds practice (default limit 40):")
    for s in needs_practice(students):
        print(f"  - {s['name']} (roll {s['roll_no']}), average {average(s):.2f}")

    print("\nNeeds practice (limit 50):")
    for s in needs_practice(students, 50):
        print(f"  - {s['name']} (roll {s['roll_no']}), average {average(s):.2f}")


if __name__ == "__main__":
    main()
