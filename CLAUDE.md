# CLAUDE.md — AI Assistant Guide for This Repository

## Overview

This repository contains **three progressive Python learning projects** designed
for SQL-familiar learners. Each project introduces Python idioms by mapping them
to equivalent SQL operations. There is no build system, framework, or external
CI — the projects are standalone educational scripts.

---

## Repository Structure

```
Sandbox/
├── CLAUDE.md                        ← this file
├── README.md                        ← learning path overview
├── project1_sqlite/                 ← Python basics + sqlite3
│   ├── README.md
│   ├── setup_db.py                  ← creates bookstore.db + sample data
│   ├── queries.py                   ← annotated SQL-from-Python examples
│   └── exercises.py                 ← practice problems (TODO stubs)
├── project2_csv/                    ← pure Python as a query engine
│   ├── README.md
│   ├── generate_data.py             ← writes employees.csv + departments.csv
│   ├── analyze.py                   ← annotated filter/sort/group examples
│   └── exercises.py                 ← practice problems (TODO stubs)
└── project3_pandas/                 ← pandas: SQL operations in Python
    ├── README.md
    ├── explore.py                   ← DataFrame structure and basics
    ├── query.py                     ← filter, group, join, aggregate examples
    └── exercises.py                 ← practice problems (TODO stubs)
```

---

## How to Run Each Project

**Project 1 (SQLite)**
```bash
cd project1_sqlite
python setup_db.py   # run once to create bookstore.db
python queries.py    # worked examples
python exercises.py  # fill in the TODOs
```

**Project 2 (CSV)**
```bash
cd project2_csv
python generate_data.py  # run once to create employees.csv, departments.csv
python analyze.py        # worked examples
python exercises.py      # fill in the TODOs
```

**Project 3 (pandas)**
```bash
pip install pandas   # only external dependency in the entire repo
cd project3_pandas
python explore.py    # DataFrame structure basics
python query.py      # filter/group/join examples
python exercises.py  # fill in the TODOs
```

---

## Dependencies

| Project | Dependencies | Install |
|---------|-------------|---------|
| project1_sqlite | `sqlite3` (stdlib) | none needed |
| project2_csv | `csv`, `collections` (stdlib) | none needed |
| project3_pandas | `pandas` | `pip install pandas` |

Python 3.8+ required. No `requirements.txt`, `pyproject.toml`, or `setup.py`
exists because this is intentionally dependency-light for a teaching context.

---

## Code Conventions

### Style
- **PEP 8** throughout: 4-space indentation, 79-char line limit loosely observed
- **snake_case** for all functions and variables
- **UPPER_CASE** for module-level constants (e.g., `DB_FILE = "bookstore.db"`)
- **f-strings** for all string formatting (no `.format()` or `%` style)
- No type hints (intentionally omitted to keep code approachable for beginners)

### Docstrings and Comments
Every file starts with a module-level docstring listing `PYTHON CONCEPTS INTRODUCED`.

```python
"""
setup_db.py — Creates a SQLite database with sample data.

PYTHON CONCEPTS INTRODUCED:
  - import       : loading a module
  - variables    : storing values
  - with blocks  : automatic cleanup
"""
```

Section headers use visual separators:
```python
# ── SECTION NAME ─────────────────────────────────────────────
```
or
```python
# ─────────────────────────────────────────────────────────────
# EXAMPLE 3: WHERE ... IN (...)
# SQL: SELECT name, city FROM employees WHERE city IN ('Austin', 'Denver')
# ─────────────────────────────────────────────────────────────
```

Every non-trivial operation includes the SQL equivalent as an inline comment:
```python
# SQL: SELECT name, salary FROM employees WHERE salary > 90000
high_earners = [emp for emp in employees if int(emp["salary"]) > 90000]
```

### Function Naming
- **`example_*()`** — worked, fully implemented example functions
- **`exercise_*()`** — student practice functions with TODO stubs and SQL hints
- **`create_*()`** — schema/data creation (project1)
- **`insert_*()`** — data loading (project1)
- **Utility functions** are small and defined at module top: `read_csv()`,
  `print_separator()` / `sep()`, `run_query()`

### Key Python Patterns Used (preserve these when adding examples)
```python
# context manager for DB/file access
with sqlite3.connect(DB_FILE) as conn:
    ...

# list comprehension (the "WHERE clause" pattern)
result = [row for row in rows if int(row["salary"]) > 90000]

# sorted with lambda key
sorted_rows = sorted(rows, key=lambda r: int(r["salary"]), reverse=True)

# defaultdict for aggregation (the "GROUP BY" pattern)
from collections import defaultdict
by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept_id"]].append(int(emp["salary"]))

# dict comprehension for lookup tables (the "JOIN" pattern)
dept_lookup = {d["dept_id"]: d["name"] for d in departments}

# pandas boolean indexing
high = df[df["salary"] > 90000]
result = df[(df["salary"] > 70000) & (df["years"] >= 4)]

# pandas AND = &, OR = |, NOT = ~ — each condition needs parentheses
```

---

## Sample Data Schema

All three projects use the same conceptual dataset (employees + departments)
to make cross-project comparisons easy.

**Project 1 — bookstore domain (SQLite)**
- `authors`: author_id, name, country (5 rows)
- `books`: book_id, title, author_id, genre, price, in_stock (10 rows)
- `sales`: sale_id, book_id, quantity, sale_date (10 rows)
- Persisted to: `project1_sqlite/bookstore.db`

**Project 2 — employee/department domain (CSV)**
- `employees.csv`: emp_id, name, dept_id, salary, city (15 rows)
- `departments.csv`: dept_id, name, budget (5 rows)
- Persisted to: `project2_csv/employees.csv`, `project2_csv/departments.csv`

**Project 3 — employee/department domain (in-memory)**
- Same employees + departments as Project 2, but defined as Python lists of
  dicts at the top of each script (no file I/O needed)
- Numeric types are correct from the start (unlike CSV where everything is str)

---

## Pedagogical Conventions (important for adding new content)

1. **SQL comment before every Python operation** — learners map what they know
   to what they're learning. Never add a Python operation without its SQL twin.

2. **Introduce one new concept per example** — don't combine multiple new ideas
   in a single example function.

3. **Exercises follow examples** — for every concept shown in `queries.py` /
   `analyze.py` / `query.py`, there is a corresponding exercise stub in
   `exercises.py` with:
   - A docstring stating the goal
   - A SQL equivalent in a comment
   - A Python structure hint (e.g., `# result = [... for ... in ... if ...]`)
   - A `pass` or empty list placeholder

4. **Progressive difficulty** — earlier files in each project are simpler.
   Do not add advanced concepts (e.g., nested comprehensions, complex closures)
   to early examples.

5. **No error handling in examples** — `try/except` is intentionally absent to
   reduce noise. Only add it in exercises explicitly focused on error handling.

---

## What Not to Do

- **Do not add a `requirements.txt`** unless introducing a new third-party
  library intentionally as a teaching concept.
- **Do not add type hints** — this is a beginner-focused codebase.
- **Do not split examples into multiple files** beyond the established
  4-file-per-project pattern (README, setup/generate, examples, exercises).
- **Do not use `pathlib`, `argparse`, or other stdlib modules** unless that
  module is itself a teaching target for the project.
- **Do not add a test suite** — the exercises *are* the tests. Automated test
  infrastructure would add complexity counter to the project's goals.

---

## Git Workflow

There is a single commit establishing the baseline (`57a2c70`). When making
changes:

```bash
# Develop on a feature branch
git checkout -b claude/<description>-<session-id>

# Commit with a descriptive message referencing what was added/changed
git commit -m "Add GROUP BY examples to project2 analyze.py"

# Push
git push -u origin <branch-name>
```

Commit messages should reference the specific project and file changed.
No squashing convention — individual meaningful commits are preferred.
