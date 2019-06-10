import os


"""
    Some configurations might include sensitive information. These settings
    should be migrated to an encrypted password manager that provide sensitive
    values during runtime only when they are needed by the application. If
    Linux is being used, SecretService or Keychain might be a good option.
"""

# -----------------------------------------------------------------------------
# GENERAL FLASK CONFIGURATION
# -----------------------------------------------------------------------------
# SECRET_KEY = os.environ['SECRET_KEY']
# LOG_FILE = os.environ['LOG_FILE']

# -----------------------------------------------------------------------------
# JWT CONFIGURATIONS
# -----------------------------------------------------------------------------

# IF JWT ALGORITHM IS HS256 THEN USE SYMMETRIC CRYPTOGRAPHY
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

# IF JWT ALGORITHM IS SET TO RS256 THEN ASYMMETRIC CRYPTO IS USED SO A
# VALID PEM FORMATTED PUBLIC KEY MUST BE PROVIDED.
# JWT_PUBLIC_KEY = os.environ['JWT_PUBLIC_KEY']
# JWT_TOKEN_LOCATION = 'headers'
# JWT_ALGORITHM = os.environ['JWT_ALGORITHM']


# -----------------------------------------------------------------------------
# SQLALCHEMY
# -----------------------------------------------------------------------------
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

task_serializer = 'json'
accept_content = ['json']

# postgres://doadmin:i7spt62muvqvwaqm@dbx-london-quantica-service-do-user-3986174-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require
