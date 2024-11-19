from django.core import checks
from django.test import SimpleTestCase, override_settings

from django_removals.checks.settings import check_removed_settings


class SettingsCheckTest(SimpleTestCase):
    def test_check_removed_settings_no_warnings(self):
        warnings = check_removed_settings()

        self.assertEqual(len(warnings), 0)

    @override_settings(TRANSACTIONS_MANAGED=True)
    def test_check_removed_settings_with_deprecated_settings(self):
        warnings = check_removed_settings()

        self.assertEqual(len(warnings), 1)
        self.assertIn(
            checks.Warning(
                "The 'TRANSACTIONS_MANAGED' setting was removed in Django 1.4 and its use is not recommended.",
                hint="Please refer to the documentation: https://docs.djangoproject.com/en/stable/releases/"
                "1.4/#features-removed-in-1-4.",
                obj="TRANSACTIONS_MANAGED",
                id="removals.W014/transactions_managed",
            ),
            warnings,
        )
