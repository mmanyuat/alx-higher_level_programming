#!/usr/bin/python3

"""
This are two module, one ot use python mysqldb
and the other to collect arguments as inputs
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    This is the entry point of the code
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    query = """
    SELECT id, name FROM states WHERE name = %s
    ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
