#!/usr/bin/python3
"""
Script that manage storage engine and use SQLAlchemy
adding db storage as a new storage
"""
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
from os import getenv


class DBStorage:
    """Class that manages storage engine for hbnb models in SQL format"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes Instance into DBStorage"""
        dialect = "mysql"
        driver = "mysqldb"
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session and return a dictionary"""

        dictionary = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem
        else:
            for state in classes:
                query = self.__session.query(state)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dictionary[key] = elem
        return (dictionary)

    def new(self, obj):
        """add new object to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates the current database session """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))

    def close(self):
        """call remove method on the private session attribute
        self.__session or close on the class Session"""
        self.__session.remove()
