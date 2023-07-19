#!/usr/bin/python3
"""
Script that manage storage engine and use SQLAlchemy
adding db storage as a new storage.
"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


# dialect = "mysql"
# driver = "mysqldb"
user = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')


class DBStorage:
    """Class that manages storage engine for hbnb models in SQL format"""
    __classes = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None

    def __init__(self):
        """Initializes Instance into DBStorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to return a dictionary of objects"""
        new_dict = {}
        if cls in self.__classes:
            result = DBStorage.__session.query(cls)
            for row in result:
                key = "{}.{}".format(row.__class__.__name__, row.id)
                new_dict[key] = row
        elif cls is None:
            for cl in self.__classes:
                result = DBStorage.__session.query(cl)
                for row in result:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    new_dict[key] = row
        return new_dict

    def new(self, obj):
        """add new object to the current database"""
        DBStorage.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        DBStorage.__session.delete(obj)

    def reload(self):
        """creates the current database session """
        Base.metadata.create_all(DBStorage.__session)
        session_factory = sessionmaker(bind=DBStorage.__session,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session

    def close(self):
        """ call close on private session. """
        self.__session.close()
