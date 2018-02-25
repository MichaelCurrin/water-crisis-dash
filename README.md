# Water Dashboard

>Reporting on Twitter trending data related to the Cape Town water crisis (Python2 Flask web server)

The only path currently in this server is an HTML page viewable at [michaelcurrin.pythonanywhere.com](https://michaelcurrin.pythonanywhere.com). The server queries a SQLite database that contains trending topic data retrieved from the [Twitter API](https://dev.twitter.com/docs). Data is added on a daily schedule using my [twitterverse](https://github.com/MichaelCurrin/twitterverse) repo, which runs as a separate application and can be used to fetch either high-level trending topics or individual tweet data.

The data which is shown on the server is a filtered view of all the trending data which has been stored in my database over a few months. Therefore it is easy to broaden or narrow the query to displaying relevant data around the Cape Town water crisis, or to focus the query on a different topic in South Africa. It is also easy to broaden the query to other English-speaking locations for which I have daily data, since I retrieve data for many countries and cities in areas like United States and Europe.

I have plans to expand the visualisations on the server using the Python [dash](https://plot.ly/products/dash/) library or JavaScript's [D3](https://d3js.org/) library.

- [Installation instructions](docs/installation_instructions.md)
- [Usage instructions](docs/usage_instructions.md)

