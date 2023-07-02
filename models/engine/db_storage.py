#!/usr/bin/python3
"""
Script that manage storage engine and use SQLAlchemy
adding db storage as a new storage
"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                    .format(dialect, driver, user, passwd,
                                            host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session and return a dictionary"""

        dictionary = {}
        classes = {User, State, City, Amenity, Place, Review}

        if cls in classes:
            dic = self.__session.query(cls).all()
            for el in dic:
                key = el.__class__.name__+ '.'+ el.id
                dictionary[key] = el
        elif cls is None:
            dic = []
            for cls in classes:
                dic += self.__session.query(cls).all()
                for el in dic:
                    key= el.__class__.__name__+'.'+el.id
                    dictionary[key]=  el

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