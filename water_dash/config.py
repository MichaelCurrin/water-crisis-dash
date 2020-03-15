"""
Configuration file.

TODO: Move filepaths out to a config parser or use argparser to take
names on app start, using config names as fallback.
"""
import os


# Set the host to be anything, such that the server is visible on
# other devices on the network. This is useful for mobile device testing.
# Turn off dotenv to avoid warning on app start for installing python-dotenv.
RUN_OPTIONS = dict(host="0.0.0.0", port=5000, debug=True, load_dotenv=False)

# These caused errors when passed to app.run in run options so do them separately.
CACHE_OPTIONS = dict(CACHE_TYPE="simple", CACHE_DEFAULT_TIMEOUT=60 * 60 * 4)

WATER = dict(
    title="CPT Water Trends",
    subtitle="Water crisis topics trending in Cape Town",
    paragraph=" Data has been scraped from the Twitter API since August"
    " 2017 and new data is added daily using my"
    ' <a href="https://github.com/MichaelCurrin/twitterverse">'
    "twitterverse</a> repo. To prevent storage limits from being exceeded on"
    " PythonAnywhere, only data from 1 Jan 2019 is available."
    "<br><br> "
    "Trending topics have been filtered to terms related to the water"
    " crisis such as dam, drought, water, crisis and day zero. "
    " The code for this Flask web server is available in my"
    ' <a href="https://github.com/MichaelCurrin/water-crisis-dash">'
    "Water Crisis</a> repo on Github."
    "<br><br> "
    "Volume is the <i>global</i> count of tweets about the topic, in"
    " the past 24 hours, at the time the value was stored. The max"
    " volume shown below is the highest recorded value since the start"
    " of the available data. If not available then it was below"
    " 10,000 tweets and therefore was too low for Twitter to make"
    " available.",
    query_name="ct_water_trends.sql",
    source_data_query="ct_water_trends_source.sql",
)
ELECTION = dict(
    title="Twitter Trends",
    subtitle="South Africa elections 2019",
    paragraph="""
        The data includes trending terms on Twitter from 1 Jan 2019
        to present. The table below has been filtered to topics which
        trended in South Africa which match the elections, voting,
        specific parties or similar terms.<br>
        <br>
        Get source data as a CSV: <a href="/download"><button>Download</button><a/><br>
        <br>
        See the <a href="https://github.com/MichaelCurrin/twitterverse">Twitterverse repo</a>
        on Github.com - it was created to scrape tweets and trending topics.<br>
        <br>
        Max Volume is the <i>global</i> count of tweets about the topic, in
        the past 24 hours, at the time the value was stored. The max
        volume shown below is the highest recorded value since the start
        of the available data. If not available then it was below
        10,000 tweets and therefore was too low for Twitter to make
        available.
    """,
    query_name="elections.sql",
    source_data_query="elections_source.sql",
)
CORONA = dict(
    title="Covid-19 crisis",
    subtitle="Twitter trends report on the corona virus",
    paragraph="""
        The table below shows daily trend data for the Worldwide level, starting
        from 1 Jan 2019. Data is pulled data from Twitter API and stored in a DB
        using my
        <a href="https://github.com/MichaelCurrin/twitterverse">twitterverse</a> repo.
        <br><br>

        Trending topics have been filtered to terms
        related to the corona outbreak. The code for this Flask web server is
        available in my <a href="https://github.com/MichaelCurrin/water-crisis-dash">Water Crisis</a>
        repo on Github.
        <br><br>
        Get source data as a CSV: <a href="/export.csv"><button>Download</button><a/>
        <br><br>

        Volume is the <i>global</i> count of tweets about
        the topic, in the <i>past 24 hours</i>, at the time the value was stored. The max
        volume shown below is the highest recorded value for that term, since the
        start of the available data, so it is not necessarily the latest but it
        still gives an idea of signifiance. If not available then it was below
        10,000 tweets and therefore was too low for Twitter to make available.
    """,
    query_name="coronavirus.sql",
    source_data_query="coronavirus_source.sql",
)


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

DB_NAME = "db.sqlite"

# Customize
TARGET = CORONA

QUERY_NAME = TARGET["query_name"]
SOURCE_DATA_QUERY = TARGET["source_data_query"]

DB_PATH = os.path.join(APP_DIR, "var", DB_NAME)
QUERY_PATH = os.path.join(APP_DIR, "sql", QUERY_NAME)
SOURCE_DATA_PATH = os.path.join(APP_DIR, "sql", SOURCE_DATA_QUERY)
