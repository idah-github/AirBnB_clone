#!/usr/bin/python3
"""init method for models module"""

from models.engine.file.storage import FileStorage


storage = FileStorage()
storage.reload()
