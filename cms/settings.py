from os.path import join
from sys import path

# Django settings for cms project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SNAKE_CMS_ROOT = '/var/django-code/snake-cms/'
# URL without the host name, 
# eg. /snake-cms/ for http://www.example.com/snake-cms/.
SNAKE_CMS_URL = '/'
# URL without the host name, 
# eg. /snake-cms/media/ for http://www.example.com/snake-cms/media/.
SNAKE_CMS_MEDIA_URL = '/media/'

#
# No need to change the paths below if you followed the 
# instructions in the README file.
#

# Add snake-cms to the python path
path.append( SNAKE_CMS_ROOT )

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(SNAKE_CMS_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = SNAKE_CMS_MEDIA_URL 

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = join(SNAKE_CMS_URL, 'media/admin/')

#django-tinymce settings
#TINYMCE_JS_URL = join(SNAKE_CMS_MEDIA_URL, 'jscripts/tiny_mce/tiny_mce_src.js')
#TINYMCE_JS_ROOT = join(SNAKE_CMS_ROOT, 'media/jscripts/tiny_mce/')
#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,paste,searchreplace",
#    'relative_urls': False,
#    'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
#}
#TINYMCE_SPELLCHECKER = False
#TINYMCE_COMPRESSOR = True
#TINYMCE_FILEBROWSER = True

#django-filebrowser settings
FILEBROWSER_DEBUG = False
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_DIRECTORY = '' #Leave empty to use whole MEDIA_ROOT
FILEBROWSER_URL_FILEBROWSER_MEDIA = join(SNAKE_CMS_MEDIA_URL, 'filebrowser/')
FILEBROWSER_PATH_MEDIA = join(MEDIA_ROOT, 'filebrowser/')
FILEBROWSER_URL_TINYMCE = join(SNAKE_CMS_MEDIA_URL, 'jscripts/tiny_mce/')
FILEBROWSER_PATH_TINYMCE = join(MEDIA_ROOT, 'admin/tinymce/jscripts/tiny_mce/')
FILEBROWSER_SAVE_FULL_URL = True

# Grappelli settings
GRAPPELLI_ADMIN_HEADLINE = 'Snake-cms'
GRAPPELLI_ADMIN_TITLE = 'Snake-cms'
GRAPPELLI_ADMIN_URL = join(SNAKE_CMS_URL, 'admin/')

#Regular Django settings, change these if needed.
ADMINS = (
    ('Admin', 'webmaster@example.com'),
)
MANAGERS = ADMINS

# To get an e-mail when someone comments, please fill in a
# mail server.
DEFAULT_FROM_EMAIL = 'postmaster@example.com'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = '25'

# Del.icio.us credentials
DELICIOUS_USER = ''
DELICIOUS_PASSWORD = ''

# Database settings
DATABASE_ENGINE = 'sqlite3'
# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/var/django-code/snake-cms/db/snake-cms.sqlite3'
# Or path to database file if using sqlite3.
DATABASE_USER = ''
# Not used with sqlite3.
DATABASE_PASSWORD = ''
# Not used with sqlite3.
DATABASE_HOST = ''
# Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''
# Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Stockholm'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'SET A SECRET KEY'

#AKISMET API key
AKISMET_API_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

#Context processors for Grappelli
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'cms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(SNAKE_CMS_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.markup',
    'cms',
    'cms.search',
    'snakelog',
    'tagging',
    'filebrowser',
    'sorl.thumbnail',
    'grappelli',
    #'tinymce',
)
