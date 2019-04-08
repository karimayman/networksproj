import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()



class Questions(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(400), nullable=False)
    answer = Column(String(80), nullable=False)

class Used(Base):
    __tablename__ = 'used'

    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(Questions)

class Choices(Base):
    __tablename__ = 'choices'

    choice = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(Questions)

# We added this serialize function to be able to send JSON objects in a
# serializable format
    
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
print('database created')