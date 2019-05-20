#!/usr/bin/env python3
"""
Water dashboard main application file.
"""
from flask import Flask
from sqlalchemy import create_engine

import config
import lib


SQL_ENGINE = create_engine("sqlite:///{}".format(config.db_path))

with open(config.query_path) as f_in:
    SQL = f_in.read()

app = Flask(__name__, static_url_path='/static')


WATER = dict(
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
)
ELECTION = dict(
    title="Twitter Trends",
    subtitle="South Africa elections 2019",
    paragraph='''
        The data includes trending terms on Twitter from 1 Jan 2019
        to present. The table below has been filtered to topics which
        trended in South Africa which match the elections, voting,
        specific parties or similar terms.<br><br>
    
        See the <a href="https://github.com/MichaelCurrin/twitterverse">Twitterverse repo</a>
        on Github.com - it was created to scrape tweets and trending topics.<br><br>
        
        Volume is the <i>global</i> count of tweets about the topic, in
        the past 24 hours, at the time the value was stored. The max
        volume shown below is the highest recorded value since the start
        of the available data. If not available then it was below
        10,000 tweets and therefore was too low for Twitter to make
        available.
    ''',
)


@app.route('/')
def root():
    """Web app root.

    Execute a fixed query and return the results in an HTML table form.
    """
    conn = SQL_ENGINE.connect()

    query = conn.execute(SQL)
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

    chosen_topic = ELECTION
    html = lib.build_html(
        row_data=cast_result,
        **chosen_topic,
    )

    return html


if __name__ == '__main__':
    # Set the host to not be localhost, such that the server is visible on
    # other devices on the network. This is useful for mobile device testing.
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
