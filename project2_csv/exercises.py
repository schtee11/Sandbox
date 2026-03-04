"""
exercises.py — Practice exercises for Project 2.

Run:  python exercises.py
"""

import csv
from collections import defaultdict


def read_csv(filename):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


# ─────────────────────────────────────────────────────────────
# EXERCISE 1
# Print all employees who have been with the company for MORE
# than 4 years, sorted by years descending.
#
# SQL: SELECT name, years FROM employees WHERE years > 4 ORDER BY years DESC
#
# Python hint:
#   veterans = [emp for emp in employees if int(emp["years"]) > 4]
#   veterans = sorted(veterans, key=lambda e: int(e["years"]), reverse=True)
# ─────────────────────────────────────────────────────────────
def exercise_1(employees):
    print("\n=== Exercise 1: Veterans (years > 4) ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 2
# Count employees per city and print each city with its count.
#
# SQL: SELECT city, COUNT(*) FROM employees GROUP BY city ORDER BY city
#
# Python hint:  use defaultdict(int) and += 1 inside a for loop
# ─────────────────────────────────────────────────────────────
def exercise_2(employees):
    print("\n=== Exercise 2: Headcount per city ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 3
# Find the highest and lowest salary in the entire dataset.
# Print both names and salaries.
#
# SQL: SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1
#      SELECT name, salary FROM employees ORDER BY salary ASC  LIMIT 1
#
# Python hint:
#   highest = max(employees, key=lambda e: int(e["salary"]))
#   lowest  = min(employees, key=lambda e: int(e["salary"]))
# ─────────────────────────────────────────────────────────────
def exercise_3(employees):
    print("\n=== Exercise 3: Highest and lowest salary ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 4
# For each department, print the department NAME (join with departments)
# and average salary, sorted by average salary descending.
#
# SQL:
#   SELECT d.name, AVG(e.salary)
#   FROM employees e JOIN departments d ON d.dept_id = e.dept_id
#   GROUP BY d.name ORDER BY AVG(e.salary) DESC
#
# Python hints:
#   - Build a dept_lookup dict first
#   - Use defaultdict(list) to collect salaries
#   - Use sum(lst)/len(lst) for average
# ─────────────────────────────────────────────────────────────
def exercise_4(employees, departments):
    print("\n=== Exercise 4: Avg salary per department ===")
    # TODO


# ─────────────────────────────────────────────────────────────
# EXERCISE 5 (stretch)
# Write a CSV file containing only employees in Engineering,
# with columns: name, salary, years.
# Sort by years descending.
#
# Python hint:
#   engineering = [emp for emp in employees if emp["dept_id"] == "1"]
#   with open("engineering.csv", "w", newline="") as f:
#       writer = csv.DictWriter(f, fieldnames=["name", "salary", "years"])
#       ...
# ─────────────────────────────────────────────────────────────
def exercise_5(employees):
    print("\n=== Exercise 5: Write Engineering CSV ===")
    # TODO


if __name__ == "__main__":
    employees   = read_csv("employees.csv")
    departments = read_csv("departments.csv")

    exercise_1(employees)
    exercise_2(employees)
    exercise_3(employees)
    exercise_4(employees, departments)
    exercise_5(employees)

    print("\nDone.")
