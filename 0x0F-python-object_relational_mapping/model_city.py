#!/usr/bin/python3
"""Module model_city"""
from sqlalchemy import ForeignKey, Column, Integer, String
from model_state import Base


class City(Base):
    """class for the model_city module"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
