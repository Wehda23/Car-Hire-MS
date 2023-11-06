"""
Settings.py File exists for purpose of saving default variables that are going to be used across the application.

such as a DEFAULT_LOGS_DIR (FOLDER) where log files are being saved, Database Settings etc..
"""
import os

"""
======================================> Database Settings
"""

HOST: str = "localhost"
MYSQL_USER: str = os.getenv("MYSQL_USER")
MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
DATBASE_NAME: str = "CarHire"  # os.getenv("MYSQL_DB_NAME")

# Raise error incase those fields are empty
if not MYSQL_USER:
    raise ValueError("MYSQL_USER environment variable is not set")
if not MYSQL_PASSWORD:
    raise ValueError("MYSQL_PASSWORD environment variable is not set")

"""
======================================> End of Database Settings
"""
