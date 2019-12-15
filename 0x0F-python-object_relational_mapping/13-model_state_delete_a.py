#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
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

    states = session.query(State).all()
    for elements in states:
        if 'a' in elements.name:
            session.delete(elements)
    session.commit()
