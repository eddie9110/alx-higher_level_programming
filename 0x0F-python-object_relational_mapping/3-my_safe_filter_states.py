#!/usr/bin/python3
"""script lists all states that are argument, safe from MySQL injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co_nnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    c_ursor = co_nnect.cursor()
    c_ursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id",
        (argv[4], ))
    get_rows = c_ursor.fetchall()
    for row in get_rows:
        print(row)
    c_ursor.close()
    co_nnect.close()
