# Expense-Tracker-Python
# 🐍 CLI Personal Expense Tracker

A modular, lightweight Command Line Interface (CLI) application built in Python and SQLite3 for personal finance management, category analytics, and user authentication.

---

## 🌟 Features

* **User Authentication:** Secure user signup and sign-in pipelines linking spending records directly to unique user IDs.
* **Transaction Management:** Add, log, and organize expenses with metadata (amount, category, date, and descriptions).
* **Financial Aggregations:** Calculate total spending and filter expense histories by specific categories.
* **Relational Integrity:** Backed by an optimized SQLite database enforcing foreign key relationships between users and expense records.

---

## 🏗️ System & Database Schema

The application follows a modular architecture separating database connections (`db.py`), business logic (`expense_manager.py`), file handling, and the interactive CLI interface (`main.py`).

```text
               +-----------------------+
               |        main.py        |  <-- CLI Menu & User Prompt Loop
               +-----------+-----------+
                           |
                           v
              +-------------------------+
              |   expense_manager.py    |  <-- Auth & Calculation Engine
              +------------+------------+
                           |
                           v
               +-----------------------+
               |         db.py         |  <-- SQLite Connection Manager
               +-----------+-----------+
                           |
                           v
                   [  expenses.db  ]
