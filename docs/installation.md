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

## Setup Python environment

Create and activate virtual environment.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install packages into it.

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
