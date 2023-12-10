#!/usr/bin/python3
"""
Child User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Rep a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
