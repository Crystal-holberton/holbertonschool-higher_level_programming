#!/usr/bin/python3
"""write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
        )
    cursor = db.cursor()
    # Execute query to select all cities with their respective state names, sorted by city id
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    # Fetch all results and print them
    results = cursor.fetchall()
    for row in results:
        print(row)
    # Close cursor and database connection
    cursor.close()
    db.close()
