#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import os
class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False) 
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""
    
    @property
    def cities(self):
        cities = models.storage.all(City)
        state_qu = self.id
        cities_list = []
        for key, value in cities.items():
            if value.state_id == self.id:
                cities_list.append(value)
        return cities_list
