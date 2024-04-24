import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    personajes_favoritos_id = Column(Integer, ForeignKey("Favoritos.id"))
    # personajes_favoritos = relationship("Favoritos_personajes")
    favoritos = relationship('Favoritos', backref='usuario', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    raza = Column(String(250))
    altura = Column(String(250))
    peso = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos', backref='personajes', lazy=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    raza = Column(String(250))
    altura = Column(String(250))
    peso = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos_', backref='planetas', lazy=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
