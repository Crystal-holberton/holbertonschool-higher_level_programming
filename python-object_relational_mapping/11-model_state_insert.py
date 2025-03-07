#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database"""

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
    # Create new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    # Print the new state's ID
    print(new_state.id)
    # Close session
    session.close()
