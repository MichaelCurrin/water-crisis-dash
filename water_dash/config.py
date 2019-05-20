# -*- coding: utf-8 -*-
"""
Configuration file.

TODO: Move filepaths out to a config parser or use argparser to take
names on app start, using config names as fallback.
"""
import os


db_name = 'db.sqlite'
query_name = 'elections.sql'
source_data_query = 'elections_source.sql'

app_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__))
)
db_path = os.path.join(app_dir, 'var', db_name)
query_path = os.path.join(app_dir, query_name)
