#!/usr/bin/env bash
# sqlite3 var/db.sqlite -column -header < sql/cape_town_tweets.sql

sqlite3 var/db.sqlite -csv -header < sql/za_activism.sql

# sqlite3 var/db.sqlite -column -header < sql/sandton_worldwide.sql
