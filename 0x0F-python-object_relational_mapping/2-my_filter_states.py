#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co_nnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    c_ursor = co_nnect.cursor()
    query = """ SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
        states.id ASC"""
    query = query.format(argv[4])
    c_ursor.execute(query)
    get_rows = c_ursor.fetchall()
    for row in get_rows:
        print(row)
    c_ursor.close()
    co_nnect.close()

