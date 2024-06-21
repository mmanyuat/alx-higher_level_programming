#!/usr/bin/python3
"""
This module connects to mysql database and retrieves from
the state filtered by letter N
"""

import MySQLdb
import sys
if __name__ == "__main__":
    """
    main entry point of the mysql, will take the arguments
    as the mysql credentials
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    query = """
    SELECT id, name FROM states
    Where name LIKE 'N%' ORDER
    BY id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
