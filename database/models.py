from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True, index=True)
    avatar = Column(LargeBinary)
    gender = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)