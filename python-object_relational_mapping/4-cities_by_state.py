#!/usr/bin/python3
"""
This script that lists all cities
from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
        )

    cur = db_connect.cursor()
    request = f"SELECT cities.id, cities.name, states.name\
        FROM states JOIN cities ON states.id = cities.state_id "
    cur.execute(request)
    rows = cur.fetchall()
    for rows in rows:
        print(rows)
    cur.close()
    db_connect.close()
