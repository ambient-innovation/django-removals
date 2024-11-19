from unittest import mock

import django
from django.core import checks
from django.test import SimpleTestCase, override_settings


class RemovedSettingsCheckTests(SimpleTestCase):
    def test_check_removed_settings_no_match(self):
        all_issues = checks.run_checks(tags=None)

        self.assertEqual(len(all_issues), 0)

    @override_settings(TRANSACTIONS_MANAGED=True)
    def test_check_removed_settings_found_match(self):
        all_issues = checks.run_checks(tags=None)

        self.assertEqual(len(all_issues), 1)

        self.assertIn(
            checks.Warning(
                "The 'TRANSACTIONS_MANAGED' setting was removed in Django 1.4 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.4/#features-removed-in-1-4.",
                obj="TRANSACTIONS_MANAGED",
                id="removals.W014/transactions_managed",
            ),
            all_issues,
        )

    @override_settings(SILENCED_SYSTEM_CHECKS=("removals.W014/transactions_managed",))
    def test_ignoring_specific_warning_works(self):
        all_issues = checks.run_checks(tags=None)

        self.assertEqual(len(all_issues), 0)

    @override_settings(USE_L10N=True)
    @mock.patch.object(django, "VERSION", new=(4, 2, 0))
    def test_dont_check_newer_than_installed_django_versions(self, *args):
        all_issues = checks.run_checks(tags=None)

        self.assertEqual(len(all_issues), 0)