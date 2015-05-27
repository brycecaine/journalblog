#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys

args = sys.argv
PATH = args[1]

subpath = args[1].split('/')[1]

if subpath == 'personaljournal':
    SITENAME = 'Bryce Caine'
    FILENAME_METADATA = '(?P<title>[a-zA-Z_]+)\.md'
    site_subdomain = 'brycecaine'
else:
    SITENAME = 'Ancestor Journals'
    FILENAME_METADATA = 'journal_(?P<author>[a-zA-Z_]+)_(?P<date>\d{4}\.\d{2}\.\d{2}).*'
    site_subdomain = 'ancestorjournals'

OUTPUT_PATH = '/home/brycecaine/workspace/%s.github.io' % site_subdomain
SITEURL = 'http://%s.github.io' % site_subdomain
USE_FOLDER_AS_CATEGORY = False

TIMEZONE = 'Europe/Paris'

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
