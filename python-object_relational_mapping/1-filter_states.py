#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
        )
    cursor = db.cursor()
    # Execute query to select states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Fetch all results and print them
    for state in cursor.fetchall():
        print(state)
    # Close cursor and database connection
    cursor.close()
    db.close()
