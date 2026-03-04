"""
setup_db.py — Creates a SQLite database with sample data.

Run this script once before running queries.py.

PYTHON CONCEPTS INTRODUCED:
  - import       : loading a module (like referencing a library or schema)
  - variables    : storing values
  - strings      : text in quotes
  - lists        : ordered collections, written as [item1, item2, ...]
  - tuples       : like lists but immutable, written as (item1, item2)
  - functions    : reusable blocks of code defined with `def`
  - with blocks  : automatic cleanup (like a transaction that auto-closes)
"""

import sqlite3  # sqlite3 is built into Python — no install needed

# ── VARIABLES ────────────────────────────────────────────────────────────────
# In Python, you just write:  name = value  (no data type declaration needed)
DB_FILE = "bookstore.db"  # This is the file SQLite will create on disk


# ── FUNCTIONS ────────────────────────────────────────────────────────────────
# `def` defines a function.  Everything indented below it is part of the body.
# Indentation (spaces/tabs) is how Python groups code — there are no BEGIN/END.
def create_tables(cursor):
    """Create the tables. The triple-quoted string is a docstring (like a comment)."""

    # cursor.execute() runs a SQL statement — exactly like you'd expect
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            country     TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT    NOT NULL,
            author_id   INTEGER REFERENCES authors(author_id),
            genre       TEXT,
            price       REAL,
            in_stock    INTEGER DEFAULT 1   -- 1 = true, 0 = false in SQLite
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id     INTEGER REFERENCES books(book_id),
            quantity    INTEGER,
            sale_date   TEXT    -- SQLite stores dates as text
        )
    """)


def insert_sample_data(cursor):
    """Load sample data into the tables."""

    # A list of tuples — each tuple is one row to insert.
    # Lists use square brackets [ ], tuples use parentheses ( ).
    authors = [
        ("Toni Morrison",    "USA"),
        ("Gabriel García Márquez", "Colombia"),
        ("Chimamanda Ngozi Adichie", "Nigeria"),
        ("Haruki Murakami",  "Japan"),
        ("Zadie Smith",      "UK"),
    ]

    # executemany() inserts all rows in one call — the ? are placeholders
    # (same idea as parameterized queries you may know from other drivers)
    cursor.executemany(
        "INSERT INTO authors (name, country) VALUES (?, ?)",
        authors
    )

    books = [
        ("Beloved",                         1, "Fiction",   14.99, 1),
        ("Song of Solomon",                 1, "Fiction",   13.50, 1),
        ("One Hundred Years of Solitude",   2, "Fiction",   15.99, 1),
        ("Love in the Time of Cholera",     2, "Fiction",   12.00, 0),
        ("Purple Hibiscus",                 3, "Fiction",   11.99, 1),
        ("Americanah",                      3, "Fiction",   14.00, 1),
        ("Norwegian Wood",                  4, "Fiction",   13.99, 1),
        ("Kafka on the Shore",              4, "Fantasy",   15.00, 1),
        ("White Teeth",                     5, "Fiction",   12.50, 1),
        ("On Beauty",                       5, "Fiction",   11.00, 0),
    ]

    cursor.executemany(
        "INSERT INTO books (title, author_id, genre, price, in_stock) VALUES (?, ?, ?, ?, ?)",
        books
    )

    sales = [
        (1, 3, "2024-01-15"),
        (1, 2, "2024-01-22"),
        (3, 5, "2024-02-01"),
        (5, 1, "2024-02-14"),
        (6, 4, "2024-02-20"),
        (7, 2, "2024-03-05"),
        (9, 3, "2024-03-10"),
        (2, 1, "2024-03-18"),
        (3, 2, "2024-04-02"),
        (6, 2, "2024-04-15"),
    ]

    cursor.executemany(
        "INSERT INTO sales (book_id, quantity, sale_date) VALUES (?, ?, ?)",
        sales
    )


# ── MAIN BLOCK ───────────────────────────────────────────────────────────────
# `if __name__ == "__main__":` means: only run this code when you execute
# *this* file directly.  If another file imports this one, it won't run.
# Think of it as the entry point of the script.
if __name__ == "__main__":

    # `with` opens a connection and automatically closes it when the block ends.
    # `as conn` gives the connection a name you can use inside the block.
    with sqlite3.connect(DB_FILE) as conn:

        # A cursor is how you send commands to the database
        cursor = conn.cursor()

        create_tables(cursor)
        insert_sample_data(cursor)

        # conn.commit() saves the changes — just like COMMIT in SQL
        conn.commit()

    # Printing uses f-strings: f"text {variable} more text"
    # The variable's value is substituted where {variable} appears.
    print(f"Database created: {DB_FILE}")
    print("Tables: authors, books, sales")
    print("Run queries.py next.")
