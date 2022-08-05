#!/usr/bin/python3
"""Module 3-my_safe_filter_states"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    name = argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %(name)s ORDER BY id ASC",
        {'name': name})
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
