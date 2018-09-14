# Water Dashboard

>Reporting on Twitter trending data related to the Cape Town water crisis (Python3 [Flask](http://flask.pocoo.org/) web server)

There is only one web page currently on this server. It is viewable at [michaelcurrin.pythonanywhere.com](https://michaelcurrin.pythonanywhere.com). On a request, webserver queries a SQLite database that contains trending topic data retrieved from the [Twitter API](https://dev.twitter.com/docs). That data is added on a daily schedule using my [twitterverse](https://github.com/MichaelCurrin/twitterverse) repo, which runs as a separate application and can be used to fetch either high-level trending topics or individual tweet data.

The data which is shown on the server is a filtered view of all the trending data which has been stored in my database over a few months. Therefore it is easy to broaden or narrow the query to displaying relevant data around the Cape Town water crisis, or to focus the query on a different topic in South Africa. It is also easy to broaden the query to other English-speaking locations for which I have daily data, since I retrieve data for many countries and cities in areas like United States and Europe.


## Documentation

- [Installation instructions](docs/installation.md)
- [Usage instructions](docs/usage.md)


## Future

I have plans to expand the visualizations on the server using something liek one of these:
- the Python [dash](https://plot.ly/products/dash/) library
- JavaScript's [D3](https://d3js.org/) library.

