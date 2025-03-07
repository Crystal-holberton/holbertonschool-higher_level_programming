#!/usr/bin/python3
"""write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
        )
    cursor = db.cursor()
    # Execute query to select states matching the given name
    query = "SELECT *\
        FROM states\
        WHERE BINARY name = %s\
        ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    # Fetch all results and print them
    for state in cursor.fetchall():
        print(state)
    # Close cursor and database connection
    cursor.close()
    db.close()
