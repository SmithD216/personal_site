#!/bin/bash
#A simple script to load up the local Django server.
#Run by typing source server.sh
source site_env/bin/activate
python3 manage.py runserver