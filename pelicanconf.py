#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yumebayashi'
SITENAME = 'yumebayashi\'s note'
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'Japan'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#GoogleAnalytics
GOOGLE_ANALYTICS = 'UA-56655645-8'

#Disqus
DISQUS_SITENAME = 'yumebayashisnote'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME
THEME = './pelican-octopress-theme-master'

SEARCH_BOX = True

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math']
# STATIC_PATHS = ['images']
