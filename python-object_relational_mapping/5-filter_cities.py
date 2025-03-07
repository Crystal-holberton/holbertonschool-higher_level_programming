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
    # Execute query to select all cities with their respective state names
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    # Fetch all results and print them
    results = cursor.fetchall()
    print(", ".join(city[0] for city in results))
    # Close cursor and database connection
    cursor.close()
    db.close()
