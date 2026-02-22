# 💰 Python Budget Tracker

A secure, terminal-based banking and budget management application written in Python. This project features user authentication, robust input validation, role-based access control (Admin vs. Standard User), and persistent data storage using JSON.

## 🚀 Features

### Authentication System
* **Account Creation:** Users can sign up with a username, password, and an automatically validated email address (using Regex).
* **Secure Login:** Verifies credentials against a persistent JSON database.
* **Role-Based Access:** Automatically detects if a logging-in user has `Admin` privileges or `Standard User` privileges and routes them to the correct dashboard.

### 👤 Standard User Dashboard
Standard users have access to their own personal financial tools:
* **Check Balance:** View current account holdings.
* **Make a Deposit:** Add funds to the account (with validation to prevent negative deposits).
* **Make an Exposit:** Withdraw or deduct funds safely (prevents overdrafting below $0).
* **Peer-to-Peer Transactions:** Send money directly to another registered user using their unique User ID. The system safely rolls back if the receiver ID does not exist.

### 🛡️ Admin Control Panel
Administrators have full CRUD (Create, Read, Update, Delete) access to the database:
* **Track Users:** View a formatted list of all registered users, their IDs, credentials, and balances.
* **Add Users:** Manually register new users into the system with custom starting balances.
* **Modify Users:** Update a specific user's username, email, password, or balance.
* **Delete Users:** Permanently remove a user from the database via their ID.

## 🛠️ Project Architecture

The application is built using Object-Oriented Programming (OOP) principles and is split across three main files:

* `Budget_Tracker.py`: The main execution file. It handles the user interface, terminal clearing, loading animations, input validation (`try...except` blocks), and the main nested-loop menu architecture.
* `users.py`: The backend logic. Contains the `user` class, the `admin` class, and methods for financial transactions and database reading/writing.
* `users.json`: The database. A dynamically updated JSON file that acts as persistent storage for all user objects.

## 💻 Prerequisites

This project uses standard Python libraries. No external dependencies or `pip` installs are required.
* Python 3.x
* Built-in modules used: `json`, `os`, `time`, `re`

## ⚙️ How to Run

1. Clone the repository to your local machine.
2. Open a terminal or command prompt in the project directory.
3. Run the main Python script:
   ```bash
   python Budget_Tracker.py
