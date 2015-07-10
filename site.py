#!/usr/bin/env/python
import sys, os
sys.path.append('/Users/margaret/anaconda/lib/python2.7/site-packages')
from flask import Flask, Markup, render_template, render_template_string
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from flask_frozen import Freezer
from collections import OrderedDict
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/posts.html")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    posts = posts[:4] # whatever
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

@app.route('/posts/archive.html')
def archive():
    all_posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    groupby_month = {}
    for post in all_posts:
        # month = convert_month(post['date'][:7])
        month = post['date'][:7]
        if month in groupby_month:
            groupby_month[month].append(post)
        else:
            groupby_month[month] = [post]
    groupby_month = OrderedDict(sorted(groupby_month.items(), key=lambda item: item[0], reverse=True))
    return render_template('archive.html', archive=groupby_month, date_formatter=convert_month)

def convert_month(date):
    """date is a string with format 'yyyy-mm' """
    months = {'01':'January',
              '02':'February',
              '03':'March',
              '04':'April',
              '05':'May',
              '06':'June',
              '07':'July',
              '08':'August',
              '09':'September',
              '10':'October',
              '11':'November',
              '12':'December'}
    raw_date = date.split('-')
    return ' '.join([months[raw_date[1]], raw_date[0]])


@app.route("/projects.html")
def projects():
    return render_template('projects.html')

@app.route("/berkeley.html")
def berkeley():
    return render_template('berkeley.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
