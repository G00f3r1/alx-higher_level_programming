#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Delete state objects on the database
    """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    del_state = session.query(State).filter(State.name.contains('a'))
    for state in del_state:
        session.delete(state)
    session.commit()
