#!/usr/bin/python3
"""Module 9-model_state_filter_a"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)
    for state in session.query(State).order_by(State.id).filter(
            State.name.contains('a')):
        session.delete(state)
    session.commit()
