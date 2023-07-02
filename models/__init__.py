#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
