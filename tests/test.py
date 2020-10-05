# Import the PyTiny module
from pytiny import PyTiny
import unittest


# Initialize the database
db = PyTiny()

# Set some data
db.set("key", "value")
db.set("database", "pytiny")

# Get data
db.get("key")

# Delete
db.delete("database")

# Export
db.export("./Backup")

# Bring
db.bring("./Backup")

# Reset
db.reset()
