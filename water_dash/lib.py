"""
Library module.
"""
import os

from sqlalchemy import create_engine

import config


GA_SNIPPET = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-87705880-6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-87705880-6');
</script>
"""

# This hacky. Don't copy this approach. Rather use a .html file
# and use Flask + Jinja templating engine to render pages to 
# handle looping in a template.
BASE = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">

            <title>{title}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">

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

            {scripts}
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

ROW_TEMPLATE = """
    <tr>
        <td>{}</td>
        <td align="center">{}</td>
        <td align="center">{}</td>
        <td align="right">{}</td>
        <td align="right">{}</td>
    </tr>
"""


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

    @param title: Title value to use in metadata and body.
    @param row_data: List of row of data as lists or tuples, to add to the HTML
        table output.
    @param subtitle: Optional subtitle for the page.
    @param paragraph: Optional paragraph text for the page.

    @return: HTML template with title and table rows filled in.
    """
    formatted_rows = [ROW_TEMPLATE.format(*row) for row in row_data]

    return BASE.format(
        title=title,
        scripts=GA_SNIPPET,
        subtitle=subtitle,
        paragraph=paragraph,
        table_data="\n".join(formatted_rows),
    )
