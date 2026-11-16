# ELEC 4 - Python Programming

- **Full name:** Jit Lee S. Romero
- **Section:** IV-BSIT C
- **Course:** ELEC 4 - Python Programming

## Set 1 Activities

| Activity | Description | Folder |
| --- | --- | --- |
| P1 - Student Grade Calculator | A menu-driven program that validates grades and uses functions to return the average, highest grade, lowest grade, and pass/fail status. | [set1/p1](set1/p1/) |
| P2 - Custom Module: student_utils | A grade report that imports four reusable functions from a custom module, demonstrates two import styles, and uses datetime to show when the report was generated. | [set1/p2](set1/p2/) |

## How to Run P1

Python 3 is required. No additional packages are needed.
Open a terminal in the repository's root folder and run:

```sh
python set1/p1/p1_grade_calculator.py
```

For the Python installation on this computer, use this PowerShell command:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" .\set1\p1\p1_grade_calculator.py
```

1. Choose **1 - Enter grades** and enter the number of grades.
2. Enter each grade. Grades must be numeric values from 0 to 100; invalid entries are requested again.
3. Choose **2 - View results** to display the average, highest, lowest, and pass/fail status. The passing average is 75.
4. Choose **3 - Exit** to end the program.

The menu continues until Exit is selected. Choosing Enter grades again replaces the previous grades.

## P1 Sample Run and Screenshots

The screenshots show two grades, **80** and **99**, with these results:

```text
Jit Lee S. Romero | IV-BSIT C
Average: 89.50
Highest: 99.00
Lowest: 80.00
Status: PASS
```

![P1 results showing the student's name, average, highest grade, lowest grade, and pass/fail status](set1/p1/screenshots/P1_view_result.png)

Additional screenshots:

- [Menu options](set1/p1/screenshots/P1_options.png)
- [Entering grades](set1/p1/screenshots/P1_entering_grades.png)

The explanation of local and global variables is in the comment at the bottom of [p1_grade_calculator.py](set1/p1/p1_grade_calculator.py).

## How to Run P2

Keep [student_utils.py](set1/p2/student_utils.py) and [p2_main.py](set1/p2/p2_main.py) in the same folder.
From the repository's root folder, run:

```sh
python set1/p2/p2_main.py
```

For the Python installation on this computer, use this PowerShell command:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" .\set1\p2\p2_main.py
```

Enter the number of grades, then enter each grade. The program prints one report and ends.
For grades **80** and **99**, the results are an average of **89.50**, a highest grade of **99.00**, a lowest grade of **80.00**, and **PASS**.
The report also displays the student's name and the date and time it was generated.

The main program uses `import student_utils` to call three functions with the module name, and `from student_utils import determine_status` to call the status function directly.
It uses `from datetime import datetime` from the standard library for the report timestamp.

### P2 Screenshot

Pending: capture an actual program run showing the name, report timestamp, average, highest grade, lowest grade, and pass/fail result.
Save the screenshot in `set1/p2/screenshots/`; it will be displayed here once supplied.
