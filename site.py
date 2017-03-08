#!/usr/bin/env python
import sys, os
sys.path.append('/Users/margaret/anaconda/lib/python2.7/site-packages')
from flask import Flask, Markup, render_template, render_template_string
from flask_frozen import Freezer
DEBUG = True

app = Flask(__name__)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/links/')
def links():
  return render_template('links.html')

@app.route("/projects/")
def projects():
    return render_template('projects.html')

@app.route("/makeup/")
def makeup():
    return render_template('makeup.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/404.html")
def static_404():
  return render_template('404.html')

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
