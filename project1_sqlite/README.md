# Project 1: Python Basics + SQLite

Since you already know SQL, this is the fastest way to get comfortable with
Python syntax. You'll write real SQL queries *from Python* against a SQLite
database, so the output will feel familiar even as the syntax is new.

## What You'll Learn

| Python concept       | SQL parallel                          |
|----------------------|---------------------------------------|
| `def` (function)     | Stored procedure / reusable logic     |
| `for` loop           | Cursor / row-by-row processing        |
| `list`               | Result set (multiple rows)            |
| `dict`               | A single row (column → value)         |
| `if` / `else`        | `CASE WHEN`                           |
| `sqlite3` module     | Your database driver                  |

## Files

- `setup_db.py` — Creates the database and loads sample data
- `queries.py`  — Runs queries and prints results using Python
- `exercises.py` — Blank exercises for you to try

## How to Run

```bash
python setup_db.py   # run this first to create the database
python queries.py    # run queries against it
python exercises.py  # try the exercises
```
