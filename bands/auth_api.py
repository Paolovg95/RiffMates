from typing import Any
from django.conf import settings
from django.http import HttpRequest
from ninja.security import APIKeyHeader

class APIkey(APIKeyHeader):
    param_name = "X-API-KEY" # Name of HTTP header where the key gets found
    def authenticate(self, request, key):
        if key == settings.API_KEY_SETTINGS:
            return key
        # Return the key if the values match, otherwise use the default return value of a function: None

api_key = APIkey()
#
