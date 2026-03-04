"""
queries.py — Run SQL queries from Python and work with the results.

PYTHON CONCEPTS INTRODUCED:
  - for loops     : iterate over rows in a result set
  - f-strings     : format output with variable values
  - list          : collect rows into a Python list
  - dict          : access columns by name instead of position
  - if/elif/else  : conditional logic (like CASE WHEN)
  - None          : Python's NULL
"""

import sqlite3

DB_FILE = "bookstore.db"


def run_query(conn, sql, params=()):
    """
    A helper function that runs any SELECT and returns all rows.

    Parameters
    ----------
    conn   : the database connection
    sql    : the SQL string to run
    params : optional tuple of values to substitute for ? placeholders

    Returns
    -------
    A list of rows.  Each row is a sqlite3.Row object you can access
    like a dict:  row["column_name"]
    """
    cursor = conn.cursor()
    cursor.execute(sql, params)
    return cursor.fetchall()   # fetchall() = get every row as a list


def print_separator(title):
    """Print a section header so output is easy to read."""
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print(f"{'=' * 55}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 1: Simple SELECT — looping over rows
# ─────────────────────────────────────────────────────────────
def example_all_books(conn):
    print_separator("All books (title, genre, price)")

    rows = run_query(conn, "SELECT title, genre, price FROM books ORDER BY title")

    # A for loop walks through each row one at a time.
    # `row` is a new variable that holds the current row each iteration.
    for row in rows:
        # row["title"] accesses the column by name (works because of row_factory below)
        print(f"  {row['title']:<35} {row['genre']:<10} ${row['price']:.2f}")
        #                         ^                  ^             ^
        #   :<35 means left-align in 35 chars   :.2f means 2 decimal places


# ─────────────────────────────────────────────────────────────
# EXAMPLE 2: WHERE clause + if/else in Python
# ─────────────────────────────────────────────────────────────
def example_availability(conn):
    print_separator("Book availability (if/else demo)")

    rows = run_query(conn, "SELECT title, price, in_stock FROM books ORDER BY title")

    for row in rows:
        # Python if/elif/else works like CASE WHEN / ELSE in SQL
        if row["in_stock"] == 1:
            status = "In stock"
        else:
            status = "OUT OF STOCK"

        print(f"  {row['title']:<35} {status}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 3: JOIN — same SQL, but results handled in Python
# ─────────────────────────────────────────────────────────────
def example_books_with_authors(conn):
    print_separator("Books with author names (JOIN)")

    sql = """
        SELECT  b.title,
                a.name  AS author,
                a.country,
                b.price
        FROM    books  b
        JOIN    authors a ON a.author_id = b.author_id
        ORDER   BY a.name, b.title
    """

    rows = run_query(conn, sql)

    for row in rows:
        print(f"  {row['author']:<30} | {row['title']:<35} | ${row['price']:.2f}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 4: GROUP BY — aggregate in SQL, display in Python
# ─────────────────────────────────────────────────────────────
def example_sales_by_author(conn):
    print_separator("Total units sold per author (GROUP BY + JOIN)")

    sql = """
        SELECT  a.name          AS author,
                SUM(s.quantity) AS total_sold
        FROM    sales   s
        JOIN    books   b ON b.book_id   = s.book_id
        JOIN    authors a ON a.author_id = b.author_id
        GROUP   BY a.name
        ORDER   BY total_sold DESC
    """

    rows = run_query(conn, sql)

    # `enumerate` gives you both the position (rank) and the row
    for rank, row in enumerate(rows, start=1):
        print(f"  #{rank}  {row['author']:<35} {row['total_sold']} units")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 5: Parameterized query — user input safely passed in
# ─────────────────────────────────────────────────────────────
def example_books_by_country(conn, country):
    print_separator(f"Books by authors from: {country}")

    sql = """
        SELECT  b.title, a.name AS author, b.price
        FROM    books   b
        JOIN    authors a ON a.author_id = b.author_id
        WHERE   a.country = ?
        ORDER   BY b.title
    """

    # Pass the parameter as a tuple — the ? gets replaced safely
    rows = run_query(conn, sql, params=(country,))
                                            # ^ the comma makes it a tuple

    if not rows:   # `not rows` is True when the list is empty
        print(f"  No books found for country: {country}")
    else:
        for row in rows:
            print(f"  {row['title']:<35} by {row['author']}")


# ─────────────────────────────────────────────────────────────
# EXAMPLE 6: Building a summary dict from query results
# ─────────────────────────────────────────────────────────────
def example_price_stats(conn):
    print_separator("Price statistics per genre (dict demo)")

    sql = """
        SELECT  genre,
                COUNT(*)    AS book_count,
                MIN(price)  AS min_price,
                MAX(price)  AS max_price,
                AVG(price)  AS avg_price
        FROM    books
        GROUP   BY genre
    """

    rows = run_query(conn, sql)

    # Build a dictionary: genre → stats
    # A dict is written as {key: value, key: value, ...}
    stats = {}
    for row in rows:
        stats[row["genre"]] = {
            "count": row["book_count"],
            "min":   row["min_price"],
            "max":   row["max_price"],
            "avg":   row["avg_price"],
        }

    # Now use the dict
    for genre, s in stats.items():   # .items() gives key-value pairs
        print(f"  {genre:<12}  count={s['count']}  "
              f"min=${s['min']:.2f}  max=${s['max']:.2f}  avg=${s['avg']:.2f}")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    with sqlite3.connect(DB_FILE) as conn:
        # This one line makes rows behave like dicts (column access by name)
        conn.row_factory = sqlite3.Row

        example_all_books(conn)
        example_availability(conn)
        example_books_with_authors(conn)
        example_sales_by_author(conn)
        example_books_by_country(conn, "Nigeria")
        example_books_by_country(conn, "France")   # should return nothing
        example_price_stats(conn)

    print("\nDone.")
