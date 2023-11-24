#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co_nnect = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    c_ursor = co_nnect.cursor()
    c_ursor.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
        """, (argv[4],))
    cities = c_ursor.fetchall()
    cities = [city[1] for city in cities]
    print(", ".join(cities))
    c_ursor.close()
    co_nnect.close()
