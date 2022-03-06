#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get state id
    """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    arg = argv[4]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    insts = session.query(State).filter(State.name == arg).first()

    if insts is not None:
        print("{}".format(insts.id))
    else:
        print("Not found")
