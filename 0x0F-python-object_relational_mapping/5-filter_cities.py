#!/usr/bin/python3
"""
script that lists all states from
the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the state list
    """

    host = "localhost"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    arg = argv[4]

    dbConn = MySQLdb.connect(host, user, passwd, db)

    cur = dbConn.cursor()
    cur.execute("""SELECT cities.name
            FROM cities
            INNER JOIN  states ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC;""", (arg,))
    rows = cur.fetchall()

    if rows is not None:
        print(", ".join(row[0] for row in rows))
