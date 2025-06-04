import sqlite3

class SQLiteCRUD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish a connection to the database."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connected.")

    def create_table(self, table_name, columns):
        """Create a table with the given name and columns."""
        column_definitions = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Table '{table_name}' created.")

    def insert_data(self, table_name, data):
        """Insert data into the table."""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()
        print("Data inserted.")

    def read_data(self, table_name):
        """Read all data from the table."""
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, table_name, update_values, condition):
        """Update data in the table."""
        set_clause = ", ".join([f"{col} = ?" for col in update_values.keys()])
        condition_clause = " AND ".join([f"{col} = ?" for col in condition.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}"
        self.cursor.execute(query, tuple(update_values.values()) + tuple(condition.values()))
        self.connection.commit()
        print("Data updated.")

    def delete_data(self, table_name, condition):
        """Delete data from the table."""
        condition_clause = " AND ".join([f"{col} = ?" for col in condition.keys()])
        query = f"DELETE FROM {table_name} WHERE {condition_clause}"
        self.cursor.execute(query, tuple(condition.values()))
        self.connection.commit()
        print("Data deleted.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    db = SQLiteCRUD("example.db")
    db.connect()

    # Create a table
    db.create_table("users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "age": "INTEGER"})

    # Insert data
    db.insert_data("users", {"name": "Alice", "age": 25})
    db.insert_data("users", {"name": "Bob", "age": 30})

    # Read data
    print("Users:", db.read_data("users"))

    # Update data
    db.update_data("users", {"age": 26}, {"name": "Alice"})

    # Delete data
    db.delete_data("users", {"name": "Bob"})

    # Read data again
    print("Users after update and delete:", db.read_data("users"))

    # Close connection
    db.close_connection()