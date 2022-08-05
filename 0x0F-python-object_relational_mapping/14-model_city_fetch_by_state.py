#!/usr/bin/python3
"""Module 9-model_state_filter_a"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)

    all_states = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)

    for city, state in all_states:
        print(f"{state.name}: ({city.id}) {city.name}")
