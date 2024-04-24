import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(15), unique=True)
    password = Column(Integer)
    email = Column(String(50), unique=True)
    subscription_date = Column(String(20))

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50))
    climate = Column(String(50), nullable=True)
    diameter = Column(Integer, nullable=True)
    terrain = Column(String(50), nullable=True)
    # favorite_id = Column(Integer, ForeignKey('favorite.id'))
    # favorite = relationship(Favorite)

class Characters(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(50), unique=True)
    skin_color = Column(String(50), nullable=True)
    height = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
