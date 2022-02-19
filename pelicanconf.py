AUTHOR = 'Malachi Ivey'
SITENAME = 'Thoughts on Data'
SITEURL = 'https://www.thoughtsondata.dev/'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = './voce'
DEFAULT_DATE_FORMAT = "%b %d, %Y"  
LOAD_CONTENT_CACHE = False
MANGLE_EMAILS = False



DEFAULT_PAGINATION = 14

# Theme specific

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

# Blogroll
LINKS = (('Index', 'https://thoughtsondata.dev/'),
         ('About', 'https://thoughtsondata.dev/pages/about.html'),
         ('Mailing List', 'https://docs.google.com/forms/d/e/1FAIpQLSdpjM_LVVvRCKhuFiYqemRuycfRChsM-Pr3nIho5mDO7c9qOw/viewform?usp=sf_link'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/thoughtsondata'),
          ('Email', 'mailto:hello@thoughtsondata.dev'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True