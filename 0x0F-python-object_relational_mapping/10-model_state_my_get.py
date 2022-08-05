#!/usr/bin/python3
"""Module 10-model_state_my_get"""
from operator import contains
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)
    for state in session.query(State):
        if state.name == argv[4]:
            print(state.id)
            break
    else:
        print("Not found")
