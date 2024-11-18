from django.conf import settings
from django.core.checks import Warning

REMOVED_SETTINGS = {
    "1.2": {
        "DATABASE_ENGINE",
        "DATABASE_HOST",
        "DATABASE_NAME",
        "DATABASE_OPTIONS",
        "DATABASE_PASSWORD",
        "DATABASE_PORT",
        "DATABASE_USER",
        "TEST_DATABASE_CHARSET",
        "TEST_DATABASE_COLLATION",
        "TEST_DATABASE_NAME",
    },
    "1.4": {
        "TRANSACTIONS_MANAGED",
    },
    "1.5": {
        "AUTH_PROFILE_MODULE",
    },
    "1.7": {
        "SOUTH_DATABASE_ADAPTER",
        "SOUTH_DATABASE_ADAPTERS",
        "SOUTH_AUTO_FREEZE_APP",
        "SOUTH_TESTS_MIGRATE",
        "SOUTH_LOGGING_ON",
        "SOUTH_LOGGING_FILE",
        "SOUTH_MIGRATION_MODULES",
        "SOUTH_USE_PYC",
        "TEST_CREATE",
        "TEST_USER_CREATE",
        "TEST_PASSWD",
        "TEST_DATABASE_ENGINE",
        "TEST_DATABASE_HOST",
        "TEST_DATABASE_OPTIONS",
        "TEST_DATABASE_PASSWORD",
        "TEST_DATABASE_PORT",
        "TEST_DATABASE_USER",
    },
    "1.8": {
        "SEND_BROKEN_LINK_EMAILS",
        "CACHE_MIDDLEWARE_ANONYMOUS_ONLY",
    },
    "1.10": {
        "ALLOWED_INCLUDE_ROOTS",
        "LOGOUT_URL",
        "TEMPLATE_CONTEXT_PROCESSORS",
        "TEMPLATE_DEBUG",
        "TEMPLATE_DIRS",
        "TEMPLATE_LOADERS",
        "TEMPLATE_STRING_IF_INVALID",
    },
    "2.0": {
        "MIDDLEWARE_CLASSES",
    },
    "2.1": {
        "USE_ETAGS",
        "SECURE_BROWSER_XSS_FILTER",
    },
    "3.0": {
        "DEFAULT_CONTENT_TYPE",
        "PASSWORD_RESET_TIMEOUT_DAYS",
    },
    "3.1": {
        "DEFAULT_FILE_STORAGE",
        "FILE_CHARSET",
    },
    "4.0": {
        "DEFAULT_HASHING_ALGORITHM",
    },
    "5.0": {
        "USE_L10N",
        "USE_DEPRECATED_PYTZ",
        "CSRF_COOKIE_MASKED",
    },
    "5.1": {
        "STATICFILES_STORAGE",
    },
}


def check_removed_settings(**kwargs):
    """
    This check warns users who still use deprecated settings variables.
    """

    warnings = []
    for setting_name in dir(settings):
        for django_version, removed_settings in REMOVED_SETTINGS.items():
            if setting_name.isupper() and setting_name in removed_settings:
                warning_id = f"W0{django_version.replace(".", "")}/{setting_name.lower()}"
                warnings.append(
                    Warning(
                        f"The {setting_name!r} setting was removed in Django {django_version} and its use is not "
                        f"recommended.",
                        hint=f"Please refer to the documentation: "
                        f"https://docs.djangoproject.com/en/stable/releases/{django_version}/"
                        f"#features-removed-in-{django_version.replace('.', '-')}.",
                        obj=setting_name,
                        id=f"removals.{warning_id}",
                    )
                )

    return warnings
