import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create Employees Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
)''')

# Create Departments Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Manager TEXT
)''')

# Insert Sample Data
cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", [
    (1, "Alice", "Sales", 50000, "2021-01-15"),
    (2, "Bob", "Engineering", 70000, "2020-06-10"),
    (3, "Charlie", "Marketing", 60000, "2022-03-20"),
])

cursor.executemany("INSERT INTO Departments VALUES (?, ?, ?)", [
    (1, "Sales", "Alice"),
    (2, "Engineering", "Bob"),
    (3, "Marketing", "Charlie"),
])

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully!")
