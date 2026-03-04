"""
exercises.py — Practice exercises for Project 1.

Each exercise has:
  - A description of what to do
  - A SQL hint (since you know SQL)
  - A Python hint showing what the structure should look like
  - A TODO comment where you write your code

Run your solution with:  python exercises.py
"""

import sqlite3

DB_FILE = "bookstore.db"


def run_query(conn, sql, params=()):
    cursor = conn.cursor()
    cursor.execute(sql, params)
    return cursor.fetchall()


# ─────────────────────────────────────────────────────────────
# EXERCISE 1
# List all authors and the number of books they have,
# sorted by most books first.
#
# SQL hint:
#   SELECT a.name, COUNT(b.book_id) AS book_count
#   FROM authors a LEFT JOIN books b ON b.author_id = a.author_id
#   GROUP BY a.name ORDER BY book_count DESC
#
# Python hint:
#   for row in rows:
#       print(f"  {row['name']} — {row['book_count']} books")
# ─────────────────────────────────────────────────────────────
def exercise_1(conn):
    print("\n=== Exercise 1: Author book counts ===")
    # TODO: write your SQL and loop here


# ─────────────────────────────────────────────────────────────
# EXERCISE 2
# Print all books priced above $13.00, along with their price.
# Use a parameterized query so the threshold can be changed easily.
#
# SQL hint:  SELECT title, price FROM books WHERE price > ? ORDER BY price DESC
#
# Python hint:
#   threshold = 13.00
#   rows = run_query(conn, sql, params=(threshold,))
# ─────────────────────────────────────────────────────────────
def exercise_2(conn):
    print("\n=== Exercise 2: Books over $13.00 ===")
    threshold = 13.00
    # TODO: write your query and loop here


# ─────────────────────────────────────────────────────────────
# EXERCISE 3
# Calculate total revenue per book (price × quantity sold).
# Print each book title and its total revenue, highest first.
#
# SQL hint:
#   SELECT b.title, SUM(b.price * s.quantity) AS revenue
#   FROM books b JOIN sales s ON s.book_id = b.book_id
#   GROUP BY b.title ORDER BY revenue DESC
#
# Python hint:
#   print(f"  {row['title']:<35}  ${row['revenue']:.2f}")
# ─────────────────────────────────────────────────────────────
def exercise_3(conn):
    print("\n=== Exercise 3: Revenue per book ===")
    # TODO: write your query and loop here


# ─────────────────────────────────────────────────────────────
# EXERCISE 4
# Build a Python list of titles for books that are OUT OF STOCK.
# Print the list at the end.
#
# SQL hint:  SELECT title FROM books WHERE in_stock = 0
#
# Python hint:
#   out_of_stock = []          # start with an empty list
#   for row in rows:
#       out_of_stock.append(row["title"])   # add each title
#   print(out_of_stock)
# ─────────────────────────────────────────────────────────────
def exercise_4(conn):
    print("\n=== Exercise 4: Out-of-stock titles ===")
    # TODO: collect titles into a list and print it


# ─────────────────────────────────────────────────────────────
# EXERCISE 5 (stretch)
# Add a new author and one of their books to the database,
# then print all books by that author to confirm the insert.
#
# SQL hint:
#   INSERT INTO authors (name, country) VALUES (?, ?)
#   -- then get the new author_id with cursor.lastrowid
#   INSERT INTO books (title, author_id, genre, price, in_stock) VALUES (?, ?, ?, ?, ?)
#
# Python hint:
#   cursor = conn.cursor()
#   cursor.execute("INSERT INTO authors ...", ("Name", "Country"))
#   new_id = cursor.lastrowid   # the auto-generated primary key
#   cursor.execute("INSERT INTO books ...", ("Title", new_id, ...))
#   conn.commit()
# ─────────────────────────────────────────────────────────────
def exercise_5(conn):
    print("\n=== Exercise 5: Insert a new author and book ===")
    # TODO: insert data and verify with a SELECT


if __name__ == "__main__":
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row

        exercise_1(conn)
        exercise_2(conn)
        exercise_3(conn)
        exercise_4(conn)
        exercise_5(conn)

    print("\nDone.")
