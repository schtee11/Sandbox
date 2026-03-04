# Project 2: CSV Data Processing

In SQL you filter rows with `WHERE`, group them with `GROUP BY`, and sort with
`ORDER BY`. This project teaches you how to do the same things using pure Python
on CSV files — no database required.

## What You'll Learn

| SQL                        | Python equivalent                          |
|----------------------------|--------------------------------------------|
| `SELECT col FROM table`    | Loop over rows, access `row["col"]`        |
| `WHERE condition`          | `if` statement inside the loop             |
| `WHERE x IN (...)`         | `if x in some_list`                        |
| `GROUP BY / COUNT / SUM`   | Dictionary to accumulate counts/sums       |
| `ORDER BY col DESC`        | `sorted(data, key=..., reverse=True)`      |
| `LIMIT n`                  | Slice a list: `data[:n]`                   |
| `INSERT INTO`              | Write a row with `csv.DictWriter`          |

## New Python Concepts

- **`csv` module** — reading and writing CSV files
- **List comprehensions** — `[x for x in items if condition]`
- **`sorted()` with a key function** — sorting by any field
- **`defaultdict`** — a dict that auto-creates missing keys
- **`lambda`** — a tiny one-line function

## Files

- `generate_data.py` — Creates sample CSV files
- `analyze.py`       — Queries the CSVs using Python
- `exercises.py`     — Practice problems

## How to Run

```bash
python generate_data.py   # creates employees.csv and departments.csv
python analyze.py         # runs the analysis examples
python exercises.py       # try the exercises
```
