REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "auth-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "auth-refresh-token",
    "REGISTER_SERIALIZER": "accounts.serializers.UserRegistrationSerializer",
}

AUTH_USER_MODEL = "accounts.User"
