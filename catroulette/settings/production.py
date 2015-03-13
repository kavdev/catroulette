from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ======================================================================================================== #
#                                      Session/Security Configuration                                      #
# ======================================================================================================== #

# Cookie Settings
SESSION_COOKIE_NAME = 'CATSessionID'

ALLOWED_HOSTS = [
    'katroulette.herokuapp.com'
]
