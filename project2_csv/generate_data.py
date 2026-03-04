"""
generate_data.py — Creates sample CSV files for Project 2.

Run this once to create:
  employees.csv
  departments.csv

PYTHON CONCEPTS:
  - csv.writer / csv.DictWriter  : writing CSV files
  - with open(...)               : safe file handling
  - lists of dicts               : each dict = one row
"""

import csv

# ── departments.csv ──────────────────────────────────────────
departments = [
    {"dept_id": 1, "name": "Engineering",  "budget": 850000},
    {"dept_id": 2, "name": "Marketing",    "budget": 420000},
    {"dept_id": 3, "name": "Sales",        "budget": 600000},
    {"dept_id": 4, "name": "HR",           "budget": 310000},
    {"dept_id": 5, "name": "Finance",      "budget": 500000},
]

# ── employees.csv ────────────────────────────────────────────
employees = [
    {"emp_id":  1, "name": "Alice Chen",       "dept_id": 1, "salary": 95000,  "years": 4, "city": "Austin"},
    {"emp_id":  2, "name": "Bob Rivera",       "dept_id": 1, "salary": 87000,  "years": 2, "city": "Austin"},
    {"emp_id":  3, "name": "Carol Smith",      "dept_id": 2, "salary": 72000,  "years": 6, "city": "Chicago"},
    {"emp_id":  4, "name": "David Park",       "dept_id": 3, "salary": 68000,  "years": 1, "city": "Denver"},
    {"emp_id":  5, "name": "Eva Johansson",    "dept_id": 1, "salary": 110000, "years": 8, "city": "Austin"},
    {"emp_id":  6, "name": "Frank Okafor",     "dept_id": 4, "salary": 61000,  "years": 3, "city": "Chicago"},
    {"emp_id":  7, "name": "Grace Liu",        "dept_id": 2, "salary": 78000,  "years": 5, "city": "Denver"},
    {"emp_id":  8, "name": "Hector Gomez",     "dept_id": 3, "salary": 74000,  "years": 7, "city": "Austin"},
    {"emp_id":  9, "name": "Irene Dubois",     "dept_id": 5, "salary": 92000,  "years": 9, "city": "Chicago"},
    {"emp_id": 10, "name": "James Wright",     "dept_id": 1, "salary": 99000,  "years": 5, "city": "Denver"},
    {"emp_id": 11, "name": "Karen Patel",      "dept_id": 5, "salary": 88000,  "years": 3, "city": "Austin"},
    {"emp_id": 12, "name": "Leo Nakamura",     "dept_id": 2, "salary": 65000,  "years": 2, "city": "Chicago"},
    {"emp_id": 13, "name": "Mia Torres",       "dept_id": 3, "salary": 71000,  "years": 4, "city": "Denver"},
    {"emp_id": 14, "name": "Nick Hassan",      "dept_id": 4, "salary": 58000,  "years": 1, "city": "Austin"},
    {"emp_id": 15, "name": "Olivia Brown",     "dept_id": 1, "salary": 105000, "years": 6, "city": "Chicago"},
]


def write_csv(filename, rows):
    """Write a list of dicts to a CSV file."""
    # rows[0].keys() gets the column names from the first dict
    fieldnames = list(rows[0].keys())

    # `with open(...) as f:` opens the file; it closes automatically when done.
    # "w"  = write mode (creates or overwrites the file)
    # newline="" is required for csv.writer on Windows
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()   # writes the header row
        writer.writerows(rows) # writes all data rows at once

    print(f"Wrote {len(rows)} rows to {filename}")


if __name__ == "__main__":
    write_csv("departments.csv", departments)
    write_csv("employees.csv",   employees)
    print("Run analyze.py next.")
