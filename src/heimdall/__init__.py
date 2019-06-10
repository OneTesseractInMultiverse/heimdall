import logging

from flask import (
    Flask
)
from flask_jwt_extended import (
    JWTManager
)
from heimdall.background_tasks import (
    init_async_service
)
from heimdall.persistence.repositories.application_repository import (
    ApplicationRepository
)
from flask_sqlalchemy import (
    SQLAlchemy
)


# ------------------------------------------------------------------------------
# SETUP GENERAL APPLICATION
# ------------------------------------------------------------------------------

__version__ = '1.0.0'
app = Flask('heimdall-identity-server')
app.logger.info("Starting... Heimdall Identity Server (Initializing)")
app.config.from_object('config')
app.logger.info("Starting... Heimdall Identity Server (Configuration Loaded)")
app.debug = True

# ------------------------------------------------------------------------------
# SETUP JWT
# ------------------------------------------------------------------------------
"""
    This API uses JWT Tokens to Authenticate call from consumers. In order to be
    able to authenticate the call and verify JWT Tokens, we must setup 
"""

# jwt = JWTManager(app)

# ------------------------------------------------------------------------------
# DATABASE CONNECTION
# ------------------------------------------------------------------------------
db = SQLAlchemy(app)

# ------------------------------------------------------------------------------
# CENTRALIZED REPOSITORY OBJECTS
# ------------------------------------------------------------------------------

applications = ApplicationRepository(db=db)

# ------------------------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------------------------
"""
    Setup very basic synchronous logging on the API. Possibly this should be 
    replaced later with an implementation that integrates with RSyslog using
    asynchronous logging to prevent blocking flask's main thread
    
    @see http://flask.pocoo.org/docs/dev/logging/
"""


# ------------------------------------------------------------------------------
# LOAD RESOURCE ENDPOINTS
# ------------------------------------------------------------------------------
"""
    We import all HTTP resource endpoints after initializing all application 
    settings that must exist prior importing the endpoints
"""

from heimdall.endpoints import *
app.logger.info("Running... Heimdall Identity Server (Started)")

