#!/usr/bin/python3
"""Changes the name of a State object with id=2 to 'New Mexico"""

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
    # Fetch the state with id=2
    state = session.query(State).filter_by(id=2).first()
    # Update state name if found
    if state:
        state.name = "New Mexico"
        session.commit()
    # Close session
    session.close()
