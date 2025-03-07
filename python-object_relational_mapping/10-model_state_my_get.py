#!/usr/bin/python3
"""Prints the State object with the given name from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Fetch state with given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    # Print state ID if found, else print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")
    # Close session
    session.close()
