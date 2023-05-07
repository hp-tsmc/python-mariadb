# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="example",
        host="mariadb",
        port=3306,
        database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#retrieving information 
some_name = "Georgi" 
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) 

for first_name, last_name in cur: 
    print(f"First name: {first_name}, Last name: {last_name}")
    
#insert information 
try: 
    cur.execute("INSERT INTO employees (emp_no,birth_date,first_name,last_name,gender,hire_date) VALUES (?, ?, ?, ?, ?, ?)", (0,"1991/02/03T10:10:10","DB","test",'M',"1991/02/03T10:10:10")) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()