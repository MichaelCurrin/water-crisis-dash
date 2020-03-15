#!/usr/bin/env python3
"""
Main application file.
"""
import csv
from io import StringIO

from flask import Flask
from flask import make_response
from flask_caching import Cache

import config
import lib


# Read queries scripts at app start.
with open(config.QUERY_PATH) as f_in:
    SQL_QUERY = f_in.read()
with open(config.SOURCE_DATA_PATH) as f_in:
    SQL_SOURCE = f_in.read()

cache = Cache(config=config.CACHE_OPTIONS)
app = Flask(__name__, static_url_path="/static")
cache.init_app(app)


def to_csv(rows, fields):
    """
    Convert data to downloadable CSV file.
    """
    str_buffer = StringIO()
    writer = csv.writer(str_buffer)
    writer.writerows([fields])
    writer.writerows(rows)

    output = make_response(str_buffer.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"

    return output


@app.route("/")
@cache.cached()
def root():
    """
    Web app root.

    Execute a fixed query and return the results in an HTML table form.
    """
    results, _ = lib.fetch_data(SQL_QUERY)

    cast_result = (
        (
            row[0],
            row[1],
            row[2],
            row[3],
            "not available" if row[4] is None else "{:,d}".format(int(row[4])),
        )
        for row in results
    )

    title = config.TARGET["title"]
    subtitle = config.TARGET["subtitle"]
    paragraph = config.TARGET["paragraph"]
    html = lib.build_html(title, cast_result, subtitle, paragraph)

    return html


@app.route("/export.csv")
@cache.cached()
def request_csv():
    """
    Endpoint to allow a user to download a CSV.
    """
    results, fields = lib.fetch_data(SQL_SOURCE)

    return to_csv(results, fields)


if __name__ == "__main__":
    app.run(**config.RUN_OPTIONS)
