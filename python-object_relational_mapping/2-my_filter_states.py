#!/usr/bin/python3
"""
This script that takes in an argument and displays
all values in the 'states' table of 'hbtn_0e_0_usa'
where 'name' matches the argument.
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
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    rows = cur.fetchall()
    for rows in rows:
        print(rows)
    cur.close()
    db_connect.close()
