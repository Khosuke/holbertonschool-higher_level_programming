#!/usr/bin/python3
"""
This script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!
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
    filter_name = sys.argv[4]
    request = f"SELECT * FROM states WHERE name = '{filter_name}'"
    cur.execute(request)
    rows = cur.fetchall()
    for rows in rows:
        print(rows)
    cur.close()
    db_connect.close()
