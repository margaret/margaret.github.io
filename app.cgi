#!/usr/bin/python
from wsgiref.handlesr import CGIHandler
from site.py import app

CGIHandler().run(app)
