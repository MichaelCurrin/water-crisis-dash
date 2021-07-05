# Installation Instructions

*Note: this currently this repo is intended to use SQLite database file created by the [twitterverse](https://github.com/MichaelCurrin/twitterverse) application, so queries in this repo will only work based if the appropriate database file is present and has data to represent. When that is done, instead of copying the data to the water_dash `var` directory, it is recommended to create a symlink. These instructions will be added in future.*

## Install OS-level dependencies

### Linux

```bash
$ sudo apt-get install python3
```

### Mac

```bash
$ brew install python@3
```

## Clone the repo

```bash
$ git clone git@github.com:MichaelCurrin/water-crisis-dash.git
$ cd water-crisis-dash
```

## Set up Python environment

Create and activate virtual environment.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install packages into it.

```bash
$ make install
```


## Python Anywhere

For _PythonAnywhere.com_ setup.

Setup virtual environment.

`venv` is not installed and Python 3.5 is the latest available in the terminal, but 3.4 is the default. So setup a new env with this:

```sh
$ virtualenv -p python3.5 ~/.local/virtualenvs/water-crisis-dash
$ ln -s ~/.local/virtualenvs/water-crisis-dash venv
$ source venv/bin/activate
```

Install packages into it.

```sh
$ make install
```
