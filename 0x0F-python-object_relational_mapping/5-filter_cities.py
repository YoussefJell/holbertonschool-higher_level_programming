#!/usr/bin/python3
"""Module 5-filter_cities"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    state_name = argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities JOIN states \
 ON states.id = cities.state_id where states.name = %(state_name)s ORDER BY cities.id ASC", {'state_name': state_name})
    query_rows = cursor.fetchall()

print(", ".join(row[0] for row in query_rows))

cursor.close()
db.close()
