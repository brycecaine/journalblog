#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content/blogs/personaljournal/bryce_caine'
SITENAME = 'Bryce Caine'
OUTPUT_PATH = 'output/personaljournal'
SITEURL = 'http://brycecaine.github.io'
USE_FOLDER_AS_CATEGORY = False

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
"""
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (
    ('github', 'https://github.com/brycecaine'),
    ('twitter', 'https://twitter.com/brycecaine'),
)
GITHUB_URL = 'http://github.com/brycecaine'
TWITTER_USERNAME = 'brycecaine'

DISQUS_SITENAME = 'brycecaine'
GOOGLE_ANALYTICS = 'UA-55396444-1'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', '.']
THEME = '/home/brycecaine/workspace/journalblog/pelican-themes/zurb-F5-basic'
