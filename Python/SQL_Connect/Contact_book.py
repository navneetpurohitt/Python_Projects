import streamlit as st  
import sqlite3
import pandas as pd
# database_setup.py

def create_database():
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    ''')

    # Example queries:
    # 1. SELECT * FROM contacts;
    # 2. INSERT INTO contacts (name, phone, email) VALUES ('Alice', '9876543210', 'alice@example.com');
    # 3. UPDATE contacts SET phone = '1112223333' WHERE name = 'Alice';
    # 4. DELETE FROM contacts WHERE name = 'Alice';
    # 5. SELECT name, phone FROM contacts WHERE email IS NOT NULL;
    # 6. SELECT COUNT(*) FROM contacts;
    # 7. SELECT * FROM contacts ORDER BY name ASC;
    # 8. SELECT * FROM contacts WHERE phone LIKE '123%';
    # 9. ALTER TABLE contacts ADD COLUMN address TEXT;
    # 10. DROP TABLE contacts;

    # Insert initial data
    # cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', ('John Doe', '1234567890', 'john@example.com'))
    
    query = st.text_input("Enter your query: ")
    button = st.button("Execute Query")
    if button:
        if query:
            try:
                data = pd.read_sql(query, conn)
                st.write(data)
                st.success("Query executed successfully!")

            except sqlite3.Error as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query.")
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    st.title("Contact Book")
    st.write("Welcome to the Contact Book application!")
    
    create_database()