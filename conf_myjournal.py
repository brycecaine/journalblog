#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from journalblog.custom.readers import TxtReader

READERS = {'txt': TxtReader}
DEFAULT_DATE = 'fs'

PATH = 'content_myjournal'
SITENAME = 'Bryce Caine'
OUTPUT_PATH = '/usr/share/nginx/www'
SITEURL = 'http://192.168.1.154'
USE_FOLDER_AS_CATEGORY = True
# FILENAME_METADATA = '(?P<date>\d{4}\.\d{1}[1-9]\d{1}\.\d{1}[1-9]\d{1}).*'
# FILENAME_METADATA = '(?P<date>\d{4}\.\d{2}\.\d{2}).*'
FILENAME_METADATA = '(?P<title>.*)(?P<date>\d{4}\.\d{2}\.\d{2}).*'
# FILENAME_METADATA = '(?P<title>.*).*'
AUTHOR = 'Bryce Caine'

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
"""
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
"""

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', '.']
THEME = '/home/brycecaine/workspace/journalblog/pelican-themes/zurb-F5-basic'
