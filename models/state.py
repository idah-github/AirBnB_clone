#!/usr/bin/python3
"""Child State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Rep a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
