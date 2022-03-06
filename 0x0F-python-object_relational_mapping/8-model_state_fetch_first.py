#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    inst = session.query(State).filter(State.id).first()

    if inst is not None:
        print("{}: {}".format(inst.id, inst.name))
    else:
        print("Nothing")
