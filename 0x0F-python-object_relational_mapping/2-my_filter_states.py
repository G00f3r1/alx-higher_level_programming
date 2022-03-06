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
    cur.execute("""SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC""".format(arg))
    rows = cur.fetchall()

    for row in rows:
        print(row)
