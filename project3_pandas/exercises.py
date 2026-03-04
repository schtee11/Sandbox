"""
exercises.py — Practice exercises for Project 3 (pandas).

Run:  python exercises.py
"""

import pandas as pd

employees_data = [
    {"emp_id":  1, "name": "Alice Chen",    "dept": "Engineering", "salary": 95000,  "years": 4, "city": "Austin"},
    {"emp_id":  2, "name": "Bob Rivera",    "dept": "Engineering", "salary": 87000,  "years": 2, "city": "Austin"},
    {"emp_id":  3, "name": "Carol Smith",   "dept": "Marketing",   "salary": 72000,  "years": 6, "city": "Chicago"},
    {"emp_id":  4, "name": "David Park",    "dept": "Sales",       "salary": 68000,  "years": 1, "city": "Denver"},
    {"emp_id":  5, "name": "Eva Johansson", "dept": "Engineering", "salary": 110000, "years": 8, "city": "Austin"},
    {"emp_id":  6, "name": "Frank Okafor",  "dept": "HR",          "salary": 61000,  "years": 3, "city": "Chicago"},
    {"emp_id":  7, "name": "Grace Liu",     "dept": "Marketing",   "salary": 78000,  "years": 5, "city": "Denver"},
    {"emp_id":  8, "name": "Hector Gomez",  "dept": "Sales",       "salary": 74000,  "years": 7, "city": "Austin"},
    {"emp_id":  9, "name": "Irene Dubois",  "dept": "Finance",     "salary": 92000,  "years": 9, "city": "Chicago"},
    {"emp_id": 10, "name": "James Wright",  "dept": "Engineering", "salary": 99000,  "years": 5, "city": "Denver"},
    {"emp_id": 11, "name": "Karen Patel",   "dept": "Finance",     "salary": 88000,  "years": 3, "city": "Austin"},
    {"emp_id": 12, "name": "Leo Nakamura",  "dept": "Marketing",   "salary": 65000,  "years": 2, "city": "Chicago"},
    {"emp_id": 13, "name": "Mia Torres",    "dept": "Sales",       "salary": 71000,  "years": 4, "city": "Denver"},
    {"emp_id": 14, "name": "Nick Hassan",   "dept": "HR",          "salary": 58000,  "years": 1, "city": "Austin"},
    {"emp_id": 15, "name": "Olivia Brown",  "dept": "Engineering", "salary": 105000, "years": 6, "city": "Chicago"},
]

df = pd.DataFrame(employees_data)


# ─────────────────────────────────────────────────────────────
# EXERCISE 1
# Show all employees in Chicago with salary > 70000.
# Only print the name, dept, and salary columns.
#
# SQL: SELECT name, dept, salary FROM employees
#      WHERE city = 'Chicago' AND salary > 70000
#
# Hint: use & to combine conditions, each in parentheses
# ─────────────────────────────────────────────────────────────
def exercise_1(df):
    print("\n=== Exercise 1: Chicago, salary > 70000 ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 2
# For each city, find the total salary bill and number of employees.
# Sort by total salary descending.
#
# SQL: SELECT city, SUM(salary), COUNT(*) FROM employees
#      GROUP BY city ORDER BY SUM(salary) DESC
#
# Hint: df.groupby("city")["salary"].agg(...)
# ─────────────────────────────────────────────────────────────
def exercise_2(df):
    print("\n=== Exercise 2: Salary by city ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 3
# Add a "level" column based on salary:
#   < 70000  → "Junior"
#   70000–90000 → "Mid"
#   > 90000  → "Senior"
# Then print name, salary, and level for all rows.
#
# Hint: use pd.cut() or np.where(), or a list comprehension + df.assign()
#
# pd.cut example:
#   df.assign(level=pd.cut(
#       df["salary"],
#       bins=[0, 69999, 90000, float("inf")],
#       labels=["Junior", "Mid", "Senior"]
#   ))
# ─────────────────────────────────────────────────────────────
def exercise_3(df):
    print("\n=== Exercise 3: Add salary level column ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 4
# Find the employee(s) with the longest tenure (most years)
# in each department.
#
# SQL equivalent (correlated subquery):
#   SELECT dept, name, years FROM employees e
#   WHERE years = (SELECT MAX(years) FROM employees WHERE dept = e.dept)
#
# Hint: df.groupby("dept")["years"].idxmax() gives the row index
#       df.loc[idx] selects those rows
# ─────────────────────────────────────────────────────────────
def exercise_4(df):
    print("\n=== Exercise 4: Longest-tenured employee per dept ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 5 (stretch)
# Rank employees within their department by salary (1 = highest).
# Add a "dept_rank" column and print the full DataFrame sorted by
# dept, then dept_rank.
#
# Hint: df.groupby("dept")["salary"].rank(method="dense", ascending=False)
# ─────────────────────────────────────────────────────────────
def exercise_5(df):
    print("\n=== Exercise 5: Salary rank within department ===")
    # TODO


if __name__ == "__main__":
    exercise_1(df)
    exercise_2(df)
    exercise_3(df)
    exercise_4(df)
    exercise_5(df)
    print("\nDone.")
