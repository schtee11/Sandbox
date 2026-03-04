# Python Learning Projects

A hands-on Python learning path designed for someone who already knows SQL.
Each project introduces new Python concepts by connecting them to things you
already understand from SQL.

---

## Learning Path

### Project 1 — `project1_sqlite/`
**Python Basics + SQLite**

You already know SQL. This project lets you run real SQL queries from Python,
which builds confidence while teaching core Python syntax:
- Variables, strings, and numbers
- Functions (`def`)
- Loops (`for`)
- Lists and dictionaries (think: rows and columns)
- Connecting to a SQLite database

### Project 2 — `project2_csv/`
**CSV Data Processing (Python as a query engine)**

Learn to read and write CSV files, then filter and summarize data using pure
Python — the same things you'd do with SELECT, WHERE, and GROUP BY in SQL.
Teaches:
- Reading/writing files
- List comprehensions (a very Pythonic way to filter data)
- Dictionaries for aggregation
- Functions and modules

### Project 3 — `project3_pandas/`
**pandas: SQL Operations in Python**

`pandas` is a library that makes Python feel a lot like SQL. This project maps
common SQL patterns directly to pandas code side-by-side.
Teaches:
- Installing and importing libraries
- DataFrames (like a SQL table)
- Filtering, grouping, joining, and sorting data
- Saving results to CSV or SQL

---

## How to Use These Projects

1. Work through projects in order (1 → 2 → 3)
2. Each project folder has:
   - A `README.md` explaining the concepts
   - A main Python script with comments explaining every step
   - Exercises at the bottom to try on your own
3. Run scripts from the terminal: `python script_name.py`

## Prerequisites

- Python 3.8 or higher (`python --version`)
- For Project 3: `pip install pandas`
