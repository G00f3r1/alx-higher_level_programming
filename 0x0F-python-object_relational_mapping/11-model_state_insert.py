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

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()

    insts = session.query(State).filter(State.name == "Louisiana").first()

    if insts is not None:
        print("{}".format(insts.id))
    else:
        print("Not found")
