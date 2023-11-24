#!/usr/bin/python3
"""script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co_nnect = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    c_ursor = co_nnect.cursor()
    c_ursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    get_rows = c_ursor.fetchall()
    for row in get_rows:
        if row[1].startswith("N"):
            print(row)
    c_ursor.close()
    co_nnect.close()
