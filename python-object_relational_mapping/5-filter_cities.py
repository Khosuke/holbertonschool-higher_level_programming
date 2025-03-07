#!/usr/bin/python3
"""
This script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
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
    filter_state_name = sys.argv[4]
    request = f"SELECT cities.name FROM cities JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = '{filter_state_name}' ORDER BY cities.id ASC"
    cur.execute(request)
    rows = cur.fetchall()
    print(', '.join(city[0] for city in rows))
    cur.close()
    db_connect.close()
