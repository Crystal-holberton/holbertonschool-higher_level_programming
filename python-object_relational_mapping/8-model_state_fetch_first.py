#!/usr/bin/python3
"""Prints the first State object from the database"""

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
    # Fetch the first state ordered by id
    first_state = session.query(State).order_by(State.id).first()
    # Print result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    # Close session
    session.close()
