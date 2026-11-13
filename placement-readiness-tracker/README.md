# Placement Readiness Tracker

Command-line tool (Python) for the placement cell. It records students' practice-test scores
(aptitude, verbal, coding), calculates averages and grades, finds the top scorer and flags
students who need extra practice.

Built for IRP-II (CSE2596), B.Tech CSE Semester V, IILM University.

## Files

| File | Purpose |
| --- | --- |
| `tracker.py` | Main tool: student data, input validation, functions and result table (Tasks 1-2) |
| `runner_up.py` | Second-highest distinct score, reads from standard input (Task 3) |

## How to run

Requires Python 3.8 or newer. No extra libraries.

```bash
python tracker.py                                  # asks for one more student, then prints results
echo "5 70 85 85 60 90" | python runner_up.py      # prints 85
```

Grading rule: A for average 80 and above, B for 60 and above, C for 40 and above,
otherwise "Needs practice".

## Sample output

```text
Enter student name: Sana Khan
Enter roll number: abc
  Roll number must be a number.
Enter roll number: 106
Enter aptitude score (0-100): 150
  Score must be between 0 and 100. Try again.
Enter aptitude score (0-100): -5
  Score must be between 0 and 100. Try again.
Enter aptitude score (0-100): 55
Enter verbal score (0-100): 61
Enter coding score (0-100): 48

=== Result Table ===
Name            Roll     Apt  Verbal  Coding  Average  Grade
--------------------------------------------------------------------
Aarav Sharma    101       82      76      91    83.00  A
Diya Verma      102       64      70      58    64.00  B
Kabir Singh     103       45      52      38    45.00  C
Meera Iyer      104       30      35      28    31.00  Needs practice
Rohan Gupta     105       90      85      88    87.67  A
Sana Khan       106       55      61      48    54.67  C

Top scorer: Rohan Gupta (roll 105) with average 87.67

Needs practice (default limit 40):
  - Meera Iyer (roll 104), average 31.00

Needs practice (limit 50):
  - Kabir Singh (roll 103), average 45.00
  - Meera Iyer (roll 104), average 31.00
```
