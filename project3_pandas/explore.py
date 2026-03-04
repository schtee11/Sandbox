"""
explore.py — Load a DataFrame and explore its structure.

This is the pandas equivalent of:
  DESCRIBE TABLE employees;
  SELECT * FROM employees LIMIT 5;
  SELECT COUNT(*) FROM employees;

PYTHON CONCEPTS:
  - import ... as   : give a module a shorter alias
  - DataFrame       : pandas' core data structure (like a SQL table)
  - attributes      : data attached to an object, accessed with dot notation
  - methods         : functions attached to an object, called with obj.method()
"""

import pandas as pd   # `pd` is the universal alias everyone uses

# ─────────────────────────────────────────────────────────────
# SETUP: create sample data directly in pandas
# (so this file works standalone without project2's CSVs)
# ─────────────────────────────────────────────────────────────

# A DataFrame can be created from a list of dicts — each dict = one row
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
# `df` is the conventional variable name for a DataFrame


# ─────────────────────────────────────────────────────────────
# STRUCTURE: describe the table (like DESCRIBE TABLE or \d in psql)
# ─────────────────────────────────────────────────────────────
print("=== df.shape — rows and columns ===")
print(df.shape)           # (15, 6) means 15 rows, 6 columns
print(f"  {df.shape[0]} rows, {df.shape[1]} columns")

print("\n=== df.columns — column names ===")
print(df.columns.tolist())  # converts the Index object to a plain Python list

print("\n=== df.dtypes — data types of each column ===")
print(df.dtypes)
# int64   = integer
# object  = string (pandas calls strings "object")
# float64 = decimal

print("\n=== df.info() — compact summary ===")
df.info()

print("\n=== df.describe() — statistics for numeric columns ===")
# Like SELECT MIN, MAX, AVG, STDDEV all at once
print(df.describe())


# ─────────────────────────────────────────────────────────────
# PREVIEW: look at a few rows
# ─────────────────────────────────────────────────────────────
print("\n=== df.head(5) — first 5 rows ===")
# SQL: SELECT * FROM employees LIMIT 5
print(df.head(5))

print("\n=== df.tail(3) — last 3 rows ===")
print(df.tail(3))

print("\n=== df.sample(3) — 3 random rows ===")
print(df.sample(3))


# ─────────────────────────────────────────────────────────────
# ACCESS: select individual columns
# ─────────────────────────────────────────────────────────────
print("\n=== df['name'] — a single column (a Series) ===")
# SQL: SELECT name FROM employees
# A single column is called a "Series" in pandas
print(df["name"])

print("\n=== df[['name', 'salary']] — multiple columns ===")
# SQL: SELECT name, salary FROM employees
# Double brackets [[ ]] because you're passing a LIST of column names
print(df[["name", "salary"]])


# ─────────────────────────────────────────────────────────────
# COUNTS
# ─────────────────────────────────────────────────────────────
print("\n=== len(df) — row count ===")
# SQL: SELECT COUNT(*) FROM employees
print(len(df))

print("\n=== df['dept'].value_counts() — count per category ===")
# SQL: SELECT dept, COUNT(*) FROM employees GROUP BY dept ORDER BY COUNT(*) DESC
print(df["dept"].value_counts())

print("\n=== df['dept'].nunique() — number of distinct values ===")
# SQL: SELECT COUNT(DISTINCT dept) FROM employees
print(df["dept"].nunique())

print("\n=== df['dept'].unique() — list of distinct values ===")
# SQL: SELECT DISTINCT dept FROM employees
print(df["dept"].unique())
