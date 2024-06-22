#!/usr/bin/python3
"""
This script connects to a MySQL database and executes a query to fetch states
where the name matches a provided argument. It prints the fetched results
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Entry point of the script to connect to mysql"""
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    query = """
    SELECT * FROM cities ORDER by id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
