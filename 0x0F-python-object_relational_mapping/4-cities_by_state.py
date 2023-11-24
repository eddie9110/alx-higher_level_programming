#!/usr/bin/python3
"""script lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co_nnect = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    c_ursor = co_nnect.cursor()
    c_ursor.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """)
    get_rows = c_ursor.fetchall()
    for row in get_rows:
        print(row)
    c_ursor.close()
    co_nnect.close()
