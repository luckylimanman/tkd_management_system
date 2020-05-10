# coding=UTF-8
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, Date, Enum
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(Enum("Male", "Female"))
    phone_number = Column(String(50))
    registration_date = Column(Date)
    birthday = Column(Date)
    belt = Column(String(50))
    validity_date = Column(Date)
    validity_count = Column(Integer)
    unlimited_count = Column(Boolean)
    gym = Column(String(50))


class Gym(Base):
    __tablename__ = 'gym'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Roster(Base):
    __tablename__ = 'roster'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer)
    member_name = Column(String(50))
    training_date = Column(Date, default=datetime.datetime.now().strftime('%Y-%m-%d')) # noqa
    training_gym = Column(String(50))




engine = create_engine('mysql+mysqlconnector://root:final@mysql:3306/testbase') # noqa

Base.metadata.create_all(bind=engine)

DBSession = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
