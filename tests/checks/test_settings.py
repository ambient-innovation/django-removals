from unittest import mock

import django
from django.core import checks
from django.test import SimpleTestCase, override_settings


class RemovedSettingsCheckTests(SimpleTestCase):
    @override_settings(TRANSACTIONS_MANAGED=True)
    def test_check_removed_settings_found_match(self):
        all_issues = checks.run_checks(tags=None)

        self.assertGreaterEqual(len(all_issues), 1)

        self.assertIn(
            checks.Warning(
                "The 'TRANSACTIONS_MANAGED' setting was removed in Django 1.8 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.8/#features-removed-in-1-8.",
                obj="TRANSACTIONS_MANAGED",
                id="removals.W018/transactions_managed",
            ),
            all_issues,
        )

    @override_settings(SILENCED_SYSTEM_CHECKS=("removals.W018/transactions_managed",))
    def test_ignoring_specific_warning_works(self):
        all_issues = checks.run_checks(tags=None)

        self.assertNotIn(
            checks.Warning(
                "The 'TRANSACTIONS_MANAGED' setting was removed in Django 1.8 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.8/#features-removed-in-1-8.",
                obj="TRANSACTIONS_MANAGED",
                id="removals.W018/transactions_managed",
            ),
            all_issues,
        )

    @override_settings(USE_L10N=True)
    @mock.patch.object(django, "VERSION", new=(4, 2, 0))
    def test_dont_check_newer_than_installed_django_versions(self, *args):
        all_issues = checks.run_checks(tags=None)

        self.assertNotIn(
            checks.Warning(
                "The 'USE_L10N' setting was removed in Django 5.0 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "5.0/#features-removed-in-5-0.",
                obj="USE_L10N",
                id="removals.W050/use_l10n",
            ),
            all_issues,
        )

    @override_settings(EMAIL_HOST="smtp.example.com")
    @mock.patch.object(django, "VERSION", new=(7, 0, 0))
    def test_check_removed_settings_django_61_email_deprecation(self, *args):
        all_issues = checks.run_checks(tags=None)

        self.assertIn(
            checks.Warning(
                "The 'EMAIL_HOST' setting was removed in Django 7.0 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "7.0/#features-removed-in-7-0.",
                obj="EMAIL_HOST",
                id="removals.W070/email_host",
            ),
            all_issues,
        )

    @override_settings(SIGNED_COOKIE_LEGACY_SALT_FALLBACK=True)
    @mock.patch.object(django, "VERSION", new=(7, 0, 0))
    def test_check_removed_settings_signed_cookie_legacy_salt_fallback(self, *args):
        all_issues = checks.run_checks(tags=None)

        self.assertIn(
            checks.Warning(
                "The 'SIGNED_COOKIE_LEGACY_SALT_FALLBACK' setting was removed in Django 7.0 and its use is not "
                "recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "7.0/#features-removed-in-7-0.",
                obj="SIGNED_COOKIE_LEGACY_SALT_FALLBACK",
                id="removals.W070/signed_cookie_legacy_salt_fallback",
            ),
            all_issues,
        )

    @override_settings(LOGOUT_URL="/logout")
    @mock.patch.object(django, "VERSION", new=(1, 9, 0))
    def test_double_digit_minor_not_flagged_on_older_django(self, *args):
        # "1.10" must compare as (1, 10), i.e. newer than the installed (1, 9),
        # so the removal is not flagged. A naive float() would read it as 1.1.
        all_issues = checks.run_checks(tags=None)

        self.assertNotIn(
            checks.Warning(
                "The 'LOGOUT_URL' setting was removed in Django 1.10 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.10/#features-removed-in-1-10.",
                obj="LOGOUT_URL",
                id="removals.W0110/logout_url",
            ),
            all_issues,
        )

    @override_settings(LOGOUT_URL="/logout")
    def test_non_float_django_versions(self, *args):
        all_issues = checks.run_checks(tags=None)

        self.assertIn(
            checks.Warning(
                "The 'LOGOUT_URL' setting was removed in Django 1.10 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.10/#features-removed-in-1-10.",
                obj="LOGOUT_URL",
                id="removals.W0110/logout_url",
            ),
            all_issues,
        )
