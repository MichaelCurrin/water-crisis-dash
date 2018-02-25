# Installation Instructions

*Note: this currently this repo is intended to use SQLite database file created by the [twitteverse](https://github.com/MichaelCurrin/twitterverse) application, so queries in this repo will only work based if the appropriate database file is present and has data to represent. When that is done, instead of copying the data to the water_dash `var` directory, it is recommended to create a symlink. These instructions will be added in future.*

This project requires Python2 and virtualenv. 

```bash
$ sudo apt-get install virtualenv
```

```bash
$ git clone git@github.com:MichaelCurrin/water_crisis_dash.git
$ cd water_dash
$ # Create a virtualenvironment named `virtualenv`, which will be
$ # ignored, as it is listed in .gitignore file.
$ virtualenv virtualenv
$ source virtualenv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
