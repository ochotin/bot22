import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "a98cc641-b332-403d-8e75-c8ca3ffe7bd4")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "47a14da1b29c494aa8c5c27a93e47070")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "switzerlandnorth.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("INSTRUMENTATION_KEY", "698adf12-cc2c-4701-8b47-d68f39a3bb79")
