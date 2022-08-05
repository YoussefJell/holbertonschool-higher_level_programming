#!/usr/bin/python3
"""Module 11-model_state_insert"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
