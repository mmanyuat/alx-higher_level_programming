#!/usr/bin/python3

"""
Module to import Mysqldb and take in arguments
from user
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    This is the entry point of the Mysqldb
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    query = """
    SELECT id, name FROM states WHERE name = '{}'
    ORDER BY id ASC
    """.format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
