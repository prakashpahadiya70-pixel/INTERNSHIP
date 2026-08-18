import sqlite3


DATABASE_NAME = "data/company.db"


def create_database():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary INTEGER,
                email TEXT
            )
        """)

        employees = [
            (101, "Rahul Sharma", "IT", 50000, "rahul@company.com"),
            (102, "Priya Patel", "HR", 45000, "priya@company.com"),
            (103, "Amit Verma", "Finance", 55000, "amit@company.com"),
            (104, "Neha Singh", "IT", 60000, "neha@company.com"),
            (105, "Rohit Jain", "Sales", 40000, "rohit@company.com")
        ]

        cursor.executemany("""
            INSERT OR IGNORE INTO employees
            (employee_id, name, department, salary, email)
            VALUES (?, ?, ?, ?, ?)
        """, employees)

        connection.commit()
        connection.close()

        return "Database created successfully."

    except Exception as e:
        return f"Database Error: {str(e)}"


def query_database(query):
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        connection.close()

        return rows

    except Exception as e:
        return f"Database Error: {str(e)}"


if __name__ == "__main__":

    print(create_database())

    print("\nEmployee Records:")
    print(query_database("SELECT * FROM employees"))

    print("\nIT Employees:")
    print(query_database(
        "SELECT * FROM employees WHERE department = 'IT'"
    ))