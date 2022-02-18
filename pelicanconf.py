AUTHOR = 'Malachi Ivey'
SITENAME = 'Thoughts on Data'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = './voce'
DEFAULT_DATE_FORMAT = "%b %d, %Y"  
USER_LOGO_URL = "images/tod.png"

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

# Blogroll
LINKS = (('Index', 'https://thoughtsondata.dev/'),
         ('About', 'https://thoughtsondata.dev/pages/about.html'),
         ('Mailing List', 'https://docs.google.com/forms/d/e/1FAIpQLSdpjM_LVVvRCKhuFiYqemRuycfRChsM-Pr3nIho5mDO7c9qOw/viewform?usp=sf_link'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/thoughtsondata'),
          ('Email', 'mailto:hello@thoughtsondata.dev'),)

DEFAULT_PAGINATION = 14

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True