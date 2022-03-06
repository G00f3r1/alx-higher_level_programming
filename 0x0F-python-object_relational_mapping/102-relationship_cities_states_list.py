#!/usr/bin/python3
"""
script that lists all City objects
from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get citiys
    and the states they are in
    """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    citys = session.query(City).order_by(City.id)

    for city in citys:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
