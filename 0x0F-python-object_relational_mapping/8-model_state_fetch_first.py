#!/usr/bin/python3
"""Module 8-model_state_fetch_first"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)
    states = session.query(State).order_by(State.id).first()
    if states:
        print(f'{states.id}: {states.name}')
    else:
        print()
