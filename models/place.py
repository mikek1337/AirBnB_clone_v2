#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
import os


class Place(BaseModel):
    """ A place to stay """
    if os.getenv("HBNB_STORAGE_TYPE") == "db":
        association_table = Table('place_amenity', Base.metadata,
                                  Column('place_id', String(60), ForeignKey(
                                      'places.id'), nullable=False),
                                  Column('amenity_id', String(60), ForeignKey(
                                      'amenities.id'), nullable=False)
                                  )
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128),  nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity",
                                 secondary=association_table,
                                 viewonly=False)

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    @property
    def amenities(self):
            '''
                 Returns a list containing the amenities ids
            '''
            return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
            '''
                Sets the amenities ids to a list
            '''
            self.amenity_ids = obj.id
            if obj.__class__.__name__ != "Amenity":
                return
            amenity_dict = models.storage.all(obj)
            place_id = self.id
            for key, val in amenity_dict.items():
                if self.id == val.place_id:
                    self.amenity_ids.append(val.id)
