# Project 3: pandas — SQL Operations in Python

`pandas` is the most popular Python library for data analysis. It introduces
the **DataFrame** — essentially a table you can manipulate with Python code.

If you know SQL, you already know *what* you want to do. This project teaches
you *how to say it* in pandas.

## Install pandas

```bash
pip install pandas
```

## What You'll Learn

| SQL                                    | pandas                                         |
|----------------------------------------|------------------------------------------------|
| `SELECT col1, col2 FROM t`             | `df[["col1", "col2"]]`                         |
| `SELECT * FROM t WHERE salary > 90000` | `df[df["salary"] > 90000]`                     |
| `SELECT * FROM t ORDER BY salary DESC` | `df.sort_values("salary", ascending=False)`    |
| `SELECT * FROM t LIMIT 5`             | `df.head(5)`                                   |
| `SELECT COUNT(*) FROM t`               | `len(df)` or `df["col"].count()`               |
| `SELECT AVG(salary) FROM t`            | `df["salary"].mean()`                          |
| `GROUP BY dept`                        | `df.groupby("dept")`                           |
| `SELECT dept, SUM(salary) GROUP BY dept` | `df.groupby("dept")["salary"].sum()`         |
| `JOIN`                                 | `df1.merge(df2, on="key")`                     |
| `UNION`                                | `pd.concat([df1, df2])`                        |
| `CREATE TABLE AS SELECT`               | `df.to_csv("output.csv")`                      |
| Reading a CSV                          | `pd.read_csv("file.csv")`                      |
| Reading from SQLite                    | `pd.read_sql("SELECT ...", conn)`              |

## Files

- `explore.py`   — Load data and explore a DataFrame (like DESC TABLE + SELECT *)
- `query.py`     — Filter, sort, group, and join operations
- `exercises.py` — Practice problems

## How to Run

```bash
# Make sure you ran project2's generate_data.py first, OR
# run the data setup at the top of each script (it creates its own data)
python explore.py
python query.py
python exercises.py
```
