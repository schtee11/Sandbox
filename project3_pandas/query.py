"""
query.py — Filter, sort, group, join, and aggregate with pandas.

Each section shows the SQL equivalent side by side.

PYTHON CONCEPTS:
  - Boolean indexing  : df[df["col"] > value]  ← the pandas WHERE clause
  - .groupby()        : aggregation by category
  - .merge()          : joining DataFrames
  - .agg()            : multiple aggregations at once
  - .assign()         : add a computed column (like a SELECT expression)
  - method chaining   : df.filter().sort().head()  ← pipe operations together
"""

import pandas as pd

# ── Sample data (same as explore.py) ────────────────────────
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

departments_data = [
    {"dept": "Engineering", "budget": 850000, "manager": "Eva Johansson"},
    {"dept": "Marketing",   "budget": 420000, "manager": "Grace Liu"},
    {"dept": "Sales",       "budget": 600000, "manager": "Hector Gomez"},
    {"dept": "HR",          "budget": 310000, "manager": "Frank Okafor"},
    {"dept": "Finance",     "budget": 500000, "manager": "Irene Dubois"},
]

df   = pd.DataFrame(employees_data)
dept = pd.DataFrame(departments_data)


def sep(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


# ─────────────────────────────────────────────────────────────
# WHERE: filter rows
# ─────────────────────────────────────────────────────────────
sep("WHERE salary > 90000")
# SQL: SELECT name, salary FROM employees WHERE salary > 90000
high = df[df["salary"] > 90000][["name", "salary"]]
print(high)

sep("WHERE dept = 'Engineering'")
# SQL: SELECT * FROM employees WHERE dept = 'Engineering'
eng = df[df["dept"] == "Engineering"]
print(eng)

sep("WHERE salary > 70000 AND years >= 4  (AND condition)")
# SQL: SELECT name FROM employees WHERE salary > 70000 AND years >= 4
# In pandas AND is &, OR is |, NOT is ~.  Each condition needs parentheses.
result = df[(df["salary"] > 70000) & (df["years"] >= 4)][["name", "salary", "years"]]
print(result)

sep("WHERE city IN ('Austin', 'Denver')")
# SQL: SELECT name, city FROM employees WHERE city IN ('Austin', 'Denver')
result = df[df["city"].isin(["Austin", "Denver"])][["name", "city"]]
print(result)

sep("WHERE name LIKE '%a%'  (case-insensitive)")
# SQL: SELECT name FROM employees WHERE LOWER(name) LIKE '%a%'
result = df[df["name"].str.contains("a", case=False)][["name"]]
print(result)


# ─────────────────────────────────────────────────────────────
# ORDER BY
# ─────────────────────────────────────────────────────────────
sep("ORDER BY salary DESC")
# SQL: SELECT name, salary FROM employees ORDER BY salary DESC
print(df[["name", "salary"]].sort_values("salary", ascending=False))

sep("ORDER BY dept ASC, salary DESC")
# SQL: SELECT name, dept, salary FROM employees ORDER BY dept, salary DESC
print(df[["name", "dept", "salary"]].sort_values(
    ["dept", "salary"],
    ascending=[True, False]
))


# ─────────────────────────────────────────────────────────────
# GROUP BY
# ─────────────────────────────────────────────────────────────
sep("GROUP BY dept — headcount, avg salary, total salary")
# SQL: SELECT dept, COUNT(*), AVG(salary), SUM(salary)
#      FROM employees GROUP BY dept ORDER BY dept
summary = (
    df.groupby("dept")["salary"]
    .agg(
        headcount="count",   # COUNT(*)
        avg_salary="mean",   # AVG(salary)
        total_salary="sum",  # SUM(salary)
    )
    .reset_index()           # moves "dept" from the index back into a column
    .sort_values("total_salary", ascending=False)
)
summary["avg_salary"] = summary["avg_salary"].round(0).astype(int)
print(summary)

sep("GROUP BY dept, city — employees per combination")
# SQL: SELECT dept, city, COUNT(*) FROM employees GROUP BY dept, city
combo = df.groupby(["dept", "city"]).size().reset_index(name="count")
print(combo.sort_values(["dept", "city"]))


# ─────────────────────────────────────────────────────────────
# COMPUTED COLUMNS (SELECT expressions)
# ─────────────────────────────────────────────────────────────
sep("Computed column: annual bonus = salary * 0.10")
# SQL: SELECT name, salary, salary * 0.10 AS bonus FROM employees
result = df[["name", "salary"]].assign(bonus=df["salary"] * 0.10)
print(result.head())


# ─────────────────────────────────────────────────────────────
# JOIN
# ─────────────────────────────────────────────────────────────
sep("INNER JOIN employees ON dept.dept = employees.dept")
# SQL: SELECT e.name, e.salary, d.budget, d.manager
#      FROM employees e JOIN departments d ON d.dept = e.dept
joined = df.merge(dept, on="dept", how="inner")
print(joined[["name", "dept", "salary", "budget", "manager"]].head(8))

sep("LEFT JOIN — all employees, with dept info where available")
# SQL: SELECT ... FROM employees e LEFT JOIN departments d ON ...
left = df.merge(dept, on="dept", how="left")
print(left[["name", "dept", "manager"]].head(5))


# ─────────────────────────────────────────────────────────────
# HAVING (filter after groupby)
# ─────────────────────────────────────────────────────────────
sep("HAVING avg_salary > 80000 (filter after GROUP BY)")
# SQL: SELECT dept, AVG(salary) FROM employees
#      GROUP BY dept HAVING AVG(salary) > 80000
grouped = df.groupby("dept")["salary"].mean().reset_index(name="avg_salary")
result  = grouped[grouped["avg_salary"] > 80000].sort_values("avg_salary", ascending=False)
result["avg_salary"] = result["avg_salary"].round(0).astype(int)
print(result)


# ─────────────────────────────────────────────────────────────
# SUBQUERY style: top earner per department
# SQL: SELECT dept, name, salary FROM employees e
#      WHERE salary = (SELECT MAX(salary) FROM employees WHERE dept = e.dept)
# ─────────────────────────────────────────────────────────────
sep("Top earner per department (like a correlated subquery)")
# idxmax() finds the index of the max value in each group
idx = df.groupby("dept")["salary"].idxmax()
top_earners = df.loc[idx][["dept", "name", "salary"]].sort_values("dept")
print(top_earners)


# ─────────────────────────────────────────────────────────────
# SAVE TO FILE
# ─────────────────────────────────────────────────────────────
sep("Save summary to CSV and SQLite")
summary.to_csv("dept_summary.csv", index=False)
print("Saved dept_summary.csv")

# pandas can also write directly to a SQLite database!
import sqlite3
with sqlite3.connect("pandas_output.db") as conn:
    df.to_sql("employees", conn, if_exists="replace", index=False)
    summary.to_sql("dept_summary", conn, if_exists="replace", index=False)
print("Saved tables to pandas_output.db")
print("  Tables: employees, dept_summary")
print("\nDone.")
