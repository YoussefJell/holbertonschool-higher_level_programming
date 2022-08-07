#!/usr/bin/python3
"""Module relationship_city"""
from sqlalchemy import ForeignKey, Column, Integer, String
from relationship_state import Base


class City(Base):
    """class for the relationship_city module"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
