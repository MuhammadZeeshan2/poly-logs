from enum import Enum

LANGUAGES = ["English", "Roman Urdu", "Urdu"]
CHANNELS = ["Facebook", "Web", "WhatsApp"]


class ErrorCodes:
    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    EMAIL_TAKEN = "Email is already taken."
    REFRESH_TOKEN_NOT_VALID = "Refresh token is not valid."
    REFRESH_TOKEN_REQUIRED = "Refresh token is required either in the body or cookie."

    USERNAME_OR_EMAIL_ALREADY_EXISTS = "User with this username or email already exists"
    USER_NOT_FOUND = "User not found"

class LogLevel(str, Enum):
    ERROR = "error"       # Capture exceptions, stack traces, and error messages for troubleshooting.
    INFO = "info"         # General operational messages that track application flow and important events.
    DEBUG = "debug" 



class LogType(str, Enum):
    APPLICATION_LOGS = "application_logs"               # General logs related to application performance and errors.
    SECURITY_LOGS = "security_logs"                     # Logs related to authentication and authorization events.
    PERFORMANCE_LOGS = "performance_logs"               # Logs that monitor system performance metrics.
    EVENT_LOGS = "event_logs"                           # Logs capturing user activities and system events.
    COMPLIANCE_LOGS = "compliance_logs"                 # Logs related to data access and change management.
    NETWORK_LOGS = "network_logs"                        # Logs that track API calls and responses.
    INTEGRATION_LOGS = "integration_logs"               # Logs related to third-party service interactions.
    CUSTOM_LOGS = "custom_logs"                         # Logs tailored for specific business needs.
