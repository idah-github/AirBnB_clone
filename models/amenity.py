#!/usr/bin/python3
"""
Def Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Child amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
