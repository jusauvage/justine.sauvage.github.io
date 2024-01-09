# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://jusauvage.github.io/justine.sauvage.github.io/'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Configuration
MENUITEMS = (
    ('Home', '/'),
)




DISPLAY_PAGES_ON_MENU = True

USE_FOLDER_AS_CATEGORIES = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = 'home'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
