"""
analyze.py — SQL-style data analysis on CSV files using pure Python.

Each example shows the SQL equivalent so you can see the mapping.

PYTHON CONCEPTS:
  - csv.DictReader        : reads CSV rows as dicts
  - list comprehensions   : [expr for item in iterable if condition]
  - sorted() + key        : sorting by any field
  - defaultdict           : dict that creates default values automatically
  - lambda                : tiny inline function
  - int() / float()       : converting strings to numbers
"""

import csv
from collections import defaultdict   # part of Python's standard library


# ─────────────────────────────────────────────────────────────
# UTILITY: read a CSV into a list of dicts
# ─────────────────────────────────────────────────────────────
def read_csv(filename):
    """
    Returns a list of dicts.  Each dict is one row; keys are column names.

    Note: csv.DictReader reads ALL values as strings.
    You have to convert numbers yourself: int("42") → 42
    """
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)   # list() turns the reader into an actual list


def print_separator(title):
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print(f"{'=' * 55}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 1: SELECT *  (just read and print all rows)
# SQL: SELECT * FROM employees
# ─────────────────────────────────────────────────────────────
def example_select_all(employees):
    print_separator("All employees (SELECT *)")

    for emp in employees:
        # emp is a dict like: {"emp_id": "1", "name": "Alice Chen", ...}
        # Values are strings — convert salary with int() for display
        print(f"  {emp['emp_id']:>3}  {emp['name']:<22}  dept={emp['dept_id']}  "
              f"salary=${int(emp['salary']):,}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 2: WHERE  (filter rows with an if statement)
# SQL: SELECT name, salary FROM employees WHERE salary > 90000
# ─────────────────────────────────────────────────────────────
def example_where(employees):
    print_separator("High earners (WHERE salary > 90000)")

    # A list comprehension is like SELECT ... WHERE in one line:
    #   [expression  for variable in iterable  if condition]
    high_earners = [
        emp for emp in employees
        if int(emp["salary"]) > 90000
    ]

    # Sort by salary descending
    # sorted() returns a new sorted list; it doesn't change the original
    # key=lambda emp: int(emp["salary"])  means "sort by the salary field"
    # reverse=True  means highest first
    high_earners = sorted(high_earners, key=lambda emp: int(emp["salary"]), reverse=True)

    for emp in high_earners:
        print(f"  {emp['name']:<22}  ${int(emp['salary']):,}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 3: WHERE ... IN (...)
# SQL: SELECT name, city FROM employees WHERE city IN ('Austin', 'Denver')
# ─────────────────────────────────────────────────────────────
def example_where_in(employees):
    print_separator("Employees in Austin or Denver (WHERE city IN (...))")

    target_cities = ["Austin", "Denver"]   # this is your IN list

    # `emp["city"] in target_cities` checks list membership — same as SQL IN
    filtered = [emp for emp in employees if emp["city"] in target_cities]

    for emp in filtered:
        print(f"  {emp['name']:<22}  {emp['city']}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 4: GROUP BY + COUNT
# SQL: SELECT dept_id, COUNT(*) AS headcount FROM employees GROUP BY dept_id
# ─────────────────────────────────────────────────────────────
def example_group_by_count(employees):
    print_separator("Headcount per department (GROUP BY + COUNT)")

    # defaultdict(int) creates a dict where missing keys start at 0
    # This lets you do headcount[key] += 1 without checking if key exists first
    headcount = defaultdict(int)

    for emp in employees:
        headcount[emp["dept_id"]] += 1   # += 1 is the COUNT equivalent

    # Sort by dept_id (as integer) for clean output
    for dept_id in sorted(headcount, key=int):
        print(f"  dept {dept_id}: {headcount[dept_id]} employees")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 5: GROUP BY + SUM + AVG
# SQL: SELECT dept_id, SUM(salary), AVG(salary) FROM employees GROUP BY dept_id
# ─────────────────────────────────────────────────────────────
def example_group_by_agg(employees):
    print_separator("Salary totals per department (GROUP BY + SUM/AVG)")

    # defaultdict(list) starts each key with an empty list
    # We'll collect all salaries for each dept, then compute stats
    salaries_by_dept = defaultdict(list)

    for emp in employees:
        salaries_by_dept[emp["dept_id"]].append(int(emp["salary"]))

    for dept_id in sorted(salaries_by_dept, key=int):
        sal_list = salaries_by_dept[dept_id]
        total = sum(sal_list)                  # sum() is a Python built-in
        avg   = total / len(sal_list)          # len() = count of items
        print(f"  dept {dept_id}: total=${total:,}  avg=${avg:,.0f}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 6: JOIN (lookup data from another list)
# SQL: SELECT e.name, d.name AS dept_name
#      FROM employees e JOIN departments d ON d.dept_id = e.dept_id
# ─────────────────────────────────────────────────────────────
def example_join(employees, departments):
    print_separator("Employees with department names (JOIN)")

    # Build a lookup dict: dept_id → dept name
    # This is the Python equivalent of a hash join
    dept_lookup = {d["dept_id"]: d["name"] for d in departments}
    #             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # This is a "dict comprehension" — like a list comprehension but for dicts

    for emp in sorted(employees, key=lambda e: e["name"]):
        dept_name = dept_lookup.get(emp["dept_id"], "Unknown")
        print(f"  {emp['name']:<22}  {dept_name}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 7: ORDER BY + LIMIT
# SQL: SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5
# ─────────────────────────────────────────────────────────────
def example_top_n(employees, n=5):
    print_separator(f"Top {n} salaries (ORDER BY salary DESC LIMIT {n})")

    sorted_employees = sorted(employees, key=lambda e: int(e["salary"]), reverse=True)

    # List slicing:  some_list[:n]  gives you the first n items
    top_n = sorted_employees[:n]

    for i, emp in enumerate(top_n, start=1):
        print(f"  #{i}  {emp['name']:<22}  ${int(emp['salary']):,}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 8: Write results to a new CSV (like INSERT INTO or CTAS)
# ─────────────────────────────────────────────────────────────
def example_write_results(employees, departments):
    print_separator("Write summary to output.csv")

    dept_lookup = {d["dept_id"]: d["name"] for d in departments}

    # Build a new list with just the columns we want
    output_rows = []
    for emp in employees:
        output_rows.append({
            "name":      emp["name"],
            "dept_name": dept_lookup.get(emp["dept_id"], "Unknown"),
            "city":      emp["city"],
            "salary":    emp["salary"],
            "years":     emp["years"],
        })

    # Sort by salary descending before writing
    output_rows = sorted(output_rows, key=lambda r: int(r["salary"]), reverse=True)

    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "dept_name", "city", "salary", "years"])
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"  Wrote {len(output_rows)} rows to output.csv")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    employees   = read_csv("employees.csv")
    departments = read_csv("departments.csv")

    example_select_all(employees)
    example_where(employees)
    example_where_in(employees)
    example_group_by_count(employees)
    example_group_by_agg(employees)
    example_join(employees, departments)
    example_top_n(employees, n=5)
    example_write_results(employees, departments)

    print("\nDone.")
