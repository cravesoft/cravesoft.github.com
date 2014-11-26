#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olivier Crave'
SITENAME = u'Cravesoft'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/cravesoft'),
          ('Twitter', 'http://twitter.com/cravesoft'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
THEME_STATIC_PATHS = ['static']
BOOTSTRAP_THEME = 'cravesoft'
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SIDEBAR = True
GITHUB_URL = 'https://github.com/cravesoft/'
CUSTOM_CSS = 'static/custom.css'
DISPLAY_BREADCRUMBS = False

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css', 'extra/CNAME']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
}

TEMPLATE_PAGES = {'apps.html': 'apps.html',
                  'games.html': 'games.html'}

#IGNORE_FILES = ['apps.html', 'games.html']
READERS = {'html': None}
