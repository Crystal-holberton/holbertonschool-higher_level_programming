#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    # Query all City objects with their corresponding State names
    results = session.query(City, State).join(State).order_by(City.id).all()
    # Print results in the required format
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    # Close session
    session.close()
