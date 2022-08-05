#!/usr/bin/python3
"""Module 12-model_state_update_id_2"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
