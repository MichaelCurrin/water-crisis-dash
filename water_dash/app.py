#!/usr/bin/env python3
"""
Water dashboard main application file.
"""
import csv
from io import StringIO

from flask import Flask
from flask import make_response

import config
import lib

with open(config.QUERY_PATH) as f_in:
    SQL_QUERY = f_in.read()

with open(config.source_data_query) as f_in:
    SQL_SOURCE = f_in.read()

app = Flask(__name__, static_url_path='/static')


@app.route('/')
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
            "not available" if row[4] is None else "{:,d}".format(int(row[4]))
        )
        for row in results
    )

    chosen_topic = config.ELECTION
    html = lib.build_html(
        row_data=cast_result,
        **chosen_topic,
    )

    return html


@app.route('/download')
def request_csv():
    results, fields = lib.fetch_data(SQL_SOURCE)

    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerows([fields])
    writer.writerows(results)
    output = make_response(buffer.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"

    return output


if __name__ == '__main__':
    # Set the host to be anything, such that the server is visible on
    # other devices on the network. This is useful for mobile device testing.
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
