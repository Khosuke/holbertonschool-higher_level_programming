#!/usr/bin/python3
"""
This script that lists all 'states' with a 'name'
starting with 'N' (upper N) from the database 'hbtn_0e_0_usa':
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for rows in rows:
        print(rows)
    cur.close()
    db_connect.close()
