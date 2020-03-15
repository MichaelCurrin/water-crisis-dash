"""
Library file.
"""
import os

from sqlalchemy import create_engine

import config


def get_connection():
    """
    Create and return a connection to the configured SQLite database.`
    """
    assert os.access(config.DB_PATH, os.R_OK), (
        "Create the database or symlink then restart the application."
        " Expected path: {}".format(config.DB_PATH)
    )
    sql_engine = create_engine("sqlite:///{}".format(config.DB_PATH))

    return sql_engine.connect()


def fetch_data(query):
    """
    Expect a SQL query, execute it and return rows and field names.
    """
    with get_connection() as conn:
        query = conn.execute(query)
        rows = query.cursor.fetchall()
        fields = [col[0] for col in query.cursor.description]

    return rows, fields


def build_html(title, row_data, subtitle="", paragraph=""):
    """
    Use templates to build HTML with dynamic table rows.

    Footer is kept at the bottom of the page thanks to:
        http://matthewjamestaylor.com/blog/keeping-footers-at-the-bottom-of-the-page

    @param title: Title value to use in metadata and body.
    @param row_data: List of row of data as lists or tuples, to add to the HTML
        table output.
    @param subtitle: Optional subtitle for the page.
    @param paragraph: Optional paragraph text for the page.

    @return: HTML template with title and table rows filled in.
    """
    base = """
<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>

        <style>

            html {{
                font-family: Arial, Helvetica, sans-serif;
            }}

            table {{
                width: 200;
            }}

            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
            }}

            th, td {{
               padding: 5px;
            }}

            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}

            @media (max-width: 1000px)  {{
                /* horizontal scrollbar for tables if mobile screen */
                table {{
                    overflow-x: auto;
                    width: 100%;
                }}
            }}

        </style>
    </head>

    <body>
        <h1>{title}</h1>

        <h2>{subtitle}</h2>
        <p><i>Application by Michael Currin</i></p>

        <p>{paragraph}</p>

        <table>
            <tr>
                <th>Topic</th>
                <th>Last Trended</th>
                <th>First Trended</th>
                <th>Days Mentioned</th>
                <th>Max Volume</th>
            </tr>
            {table_data}
        </table>
    </body>

</html>
    """

    row_template = """
            <tr>
                <td>{}</td>
                <td align="center">{}</td>
                <td align="center">{}</td>
                <td align="right">{}</td>
                <td align="right">{}</td>
            </tr>
    """

    formatted_rows = [row_template.format(*row) for row in row_data]

    return base.format(
        title=title,
        subtitle=subtitle,
        paragraph=paragraph,
        table_data="\n".join(formatted_rows),
    )
