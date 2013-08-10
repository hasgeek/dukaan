# -*- coding: utf-8 -*-
#: Cache type
CACHE_TYPE = 'redis'
#: Google Analytics code
GA_CODE = ''
#: Google site verification code (inserted as a meta tag)
GOOGLE_SITE_VERIFICATION = ''
#: Typekit code
TYPEKIT_CODE = ''
#: Database backend
SQLALCHEMY_DATABASE_URI = 'sqlite://'
#: Secret key
SECRET_KEY = 'make this something random'
#: Lastuser server
LASTUSER_SERVER = ''
#: Lastuser client id
LASTUSER_CLIENT_ID = ''
#: Lastuser client secret
LASTUSER_CLIENT_SECRET = ''
#: Mail settings
#: MAIL_FAIL_SILENTLY : default True
#: MAIL_SERVER : default 'localhost'
#: MAIL_PORT : default 25
#: MAIL_USE_TLS : default False
#: MAIL_USE_SSL : default False
#: MAIL_USERNAME : default None
#: MAIL_PASSWORD : default None
#: DEFAULT_MAIL_SENDER : default None
MAIL_FAIL_SILENTLY = False
MAIL_SERVER = 'localhost'
DEFAULT_MAIL_SENDER = ('HasGeek', 'test@example.com')
MAIL_DEFAULT_SENDER = DEFAULT_MAIL_SENDER
#: Logging: recipients of error emails
ADMINS = []
#: Log file
LOGFILE = 'error.log'
