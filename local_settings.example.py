# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

JOBS_NEW_THRESHOLD = 1
JOBS_NOTIFICATION_LIST = [] # list of email addresses

GATEKEEPER_ENABLE_AUTOMODERATION = True
GATEKEEPER_DEFAULT_STATUS = 0
GATEKEEPER_MODERATOR_LIST = JOBS_NOTIFICATION_LIST