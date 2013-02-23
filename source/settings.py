#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Olivier Crave'
SITENAME = u'Cravesoft'
SITEURL = 'http://www.cravesoft.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('Github', 'http://github.com/cravesoft'),
          ('Twitter', 'http://twitter.com/cravesoft'),
          ('Facebook', 'http://www.facebook.com/cravesoft'),)

DEFAULT_PAGINATION = 10

REVERSE_ARCHIVE_ORDER = True

GOOGLE_ANALYTICS = 'UA-537852-1'

# Take the ``date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'

# ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)

