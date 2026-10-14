# Lab 5 — Static Code Analysis

Name: Shivansh Sharma
SRN: PES2UG24CS474
Section: H

Forked lab repository (same contents as this folder — fixed `todo_manager.py`,
before/after reports for Pylint, Bandit and Flake8, and 3 commits, one per tool):

https://github.com/shivanshpap/L5_37_todo_manager

Submission report: `PES2UG24CS474_SE_LAB5.pdf`

Results: Pylint 10.00/10 · Flake8 0 issues · Bandit 0 issues.

---

# Lab 5: Static Code Analysis — To-Do List & Task Manager

**Your file:** `todo_manager.py`

Follow the lab handout for the full instructions.

## About the program

A task manager. It adds tasks with a priority, marks them complete, lists pending tasks in priority order, searches by keyword, suggests a task to do next, and saves tasks to tasks.pkl and tasks.json.

The code works, but only just. It has quality, style and security problems of the kind Pylint, Flake8 and Bandit are built to find.

## What to do

1. **Run it first** and read the output carefully:

   ```bash
   python todo_manager.py
   ```

   It runs a short demonstration and needs no input. Note what it prints, so you can check that it still behaves the same after your fixes.

2. **Install the tools:**

   ```bash
   python -m pip install pylint bandit flake8
   ```

3. **Run the analysis and save the reports:**

   ```bash
   python -m pylint todo_manager.py > pylint_report.txt
   python -m bandit -r todo_manager.py > bandit_report.txt
   python -m flake8 todo_manager.py > flake8_report.txt
   ```

4. **Document the issues** in `issues.md` using this table (at least 4 rows, high and medium severity first):

   | Issue | Type | Line(s) | Description | Fix Approach |
   |-------|------|---------|-------------|--------------|
   | ...   | ...  | ...     | ...         | ...          |

5. **Fix the code.** Fix at least 4 of the issues you documented, then rerun all three tools to confirm they are gone. Repeat until you are satisfied. The program should still do its job when you are done.

6. **Reflect.** Answer the four reflection questions from the handout in `reflection.md`.

## Deliverables

- `todo_manager.py`: your cleaned version, with at least 4 issues fixed.
- `issues.md`: the completed issue table.
- `reflection.md`: your answers to the reflection questions.
- `PES2UG24CS474_SE_LAB5.pdf`: lab report document.
