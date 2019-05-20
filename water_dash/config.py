# -*- coding: utf-8 -*-
"""
Configuration file.

TODO: Move filepaths out to a config parser or use argparser to take
names on app start, using config names as fallback.
"""
import os


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

db_name = 'db.sqlite'
query_name = 'elections.sql'
source_data_query = 'elections_source.sql'

app_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__))
)
db_path = os.path.join(app_dir, 'var', db_name)
query_path = os.path.join(app_dir, query_name)
