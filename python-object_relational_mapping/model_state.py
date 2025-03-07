#!/usr/bin/python3
"""Definition of the State class and instance Base"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance
Base = declarative_base()


class State(Base):
    """State class that maps to the states table in the database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
