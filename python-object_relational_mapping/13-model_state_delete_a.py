#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' from the database"""

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
    # Query and delete all states with 'a' in the name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    # Commit changes to DB
    session.commit()
    # Close session
    session.close()
