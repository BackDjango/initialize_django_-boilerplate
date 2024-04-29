from datetime import timedelta


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": "SECRET_KEY",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}
