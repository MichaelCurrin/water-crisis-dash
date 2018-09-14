#!/usr/bin/env python3
"""
Water dashboard main application file.
"""
import os

from flask import Flask
from sqlalchemy import create_engine

import config
import lib

assert os.access(config.db_path, os.R_OK), (
    "Create the database or symlink then restart the application."
    " Expected path: {}".format(config.db_path)
)
SQL_ENGINE = create_engine("sqlite:///{}".format(config.db_path))

with open(config.query_path) as f_in:
    SQL_QUERY = f_in.read()

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def root():
    """
    Web app root.

    Execute a fixed query and return the results in an HTML table form.
    """
    conn = SQL_ENGINE.connect()

    query = conn.execute(SQL_QUERY)
    result = query.cursor.fetchall()

    cast_result = (
        (
            row[0],
            row[1],
            row[2],
            row[3],
            "not available" if row[4] is None else "{:,d}".format(int(row[4]))
        )
        for row in result
    )

    html = lib.build_html(
        title="CPT Water Trends",
        subtitle="Water crisis topics trending in Cape Town",
        paragraph=' Data has been scraped from the Twitter API since August'
            ' 2017 and new data is added daily using my'
            ' <a href="https://github.com/MichaelCurrin/twitterverse">'
            'twitterverse</a> repo. '
            '<br><br> '
            'Trending topics have been filtered to terms related to the water'
            ' crisis such as dam, drought, water, crisis and day zero. '
            ' The code for this Flask web server is available in my'
            ' <a href="https://github.com/MichaelCurrin/water_crisis_dash">'
            'Water Crisis</a> repo on Github.'
            '<br><br> '
            'Volume is the <i>global</i> count of tweets about the topic, in'
            ' the past 24 hours, at the time the value was stored. The max'
            ' volume shown below is the highest recorded value since the start'
            ' of the available data. If not available then it was below'
            ' 10,000 tweets and therefore was too low for Twitter to make'
            ' available.',
        row_data=cast_result
    )

    return html


if __name__ == '__main__':
    # Set the host to be anything, such that the server is visible on
    # other devices on the network. This is useful for mobile device testing.
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
