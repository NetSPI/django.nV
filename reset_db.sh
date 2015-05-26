#!/bin/bash
rm db.sqlite3 &> /dev/null
python manage.py migrate
python manage.py loaddata fixtures/*
