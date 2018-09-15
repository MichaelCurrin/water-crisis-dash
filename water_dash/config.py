"""
Configuration file.

TODO: Move filepaths out to a config parser or use argparser to take
names on app start, using config names as fallback.
"""
import os


DB_NAME = 'db.sqlite'
QUERY_NAME = 'ct_water_trends.sql'

APP_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__))
)
DB_PATH = os.path.join(APP_DIR, 'var', DB_NAME)
QUERY_PATH = os.path.join(APP_DIR, 'sql', QUERY_NAME)
