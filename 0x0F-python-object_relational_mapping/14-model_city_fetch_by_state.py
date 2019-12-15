#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """list all elements of State table"""
    arg = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                           sys.argv[2],
                                                           sys.argv[3])
    engine = create_engine(arg, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).all()
    for x in states:
        if x[0].id == x[1].state_id:
            print("{}: ({}) {}".format(x[0].name, x[1].id, x[1].name))
