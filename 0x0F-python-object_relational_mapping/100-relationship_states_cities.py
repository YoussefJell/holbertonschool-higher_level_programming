#!/usr/bin/python3
"""Module 9-model_state_filter_a"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()
