#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get the cities
    """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(State)
    for state, city in result.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
