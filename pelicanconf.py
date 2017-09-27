# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Khalid Grandi'
SITENAME = "xaled's blog"
SITEURL = 'https://xaled.github.io'
TIMEZONE = "UTC"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

#GITHUB_URL = 'http://github.com/xaled/'
#DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2017, 9, 22, 3, 14, 15)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


SOCIAL = (('twitter', 'http://twitter.com/khalid_grandi'),
          ('github', 'http://github.com/xaled'),)

# global metadata to all the contents
DEFAULT_METADATA = {'meta': 'meta'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
#foobar = "barbaz"

THEME = 'themes/blueidea'
OUTPUT_PATH = 'output'
PATH = 'content'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
# Custom Home page bootstrap
#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
#PAGINATED_DIRECT_TEMPLATES = (('blog',))
#TEMPLATE_PAGES = {'home.html': 'index.html',}


# CUSTOM theme: blueidea:
DISPLAY_SEARCH_FORM=True
DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_CATEGORIES_ON_SUBMENU=True
#LINKS = (('twitter', 'http://twitter.com/khalid_grandi'), ('github', 'http://github.com/xaled'),)


