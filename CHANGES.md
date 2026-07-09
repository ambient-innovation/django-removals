# Changelog

**1.4.0** (2026-07-09)
  * Added `SIGNED_COOKIE_LEGACY_SALT_FALLBACK` to the settings removed in Django 7.0 (#18)

**1.3.1** (2026-07-03)
  * Updated company and maintainer information to "Beyonder Deutschland"

**1.3.0** (2026-07-03)
  * **Breaking change:** Dropped support for Python 3.10 (nearing end-of-life in October 2026)
  * Added support for Python 3.14
  * Added native uv support to the rendered Read the Docs configuration
  * Replaced the unmaintained "m2r2" documentation dependency with "sphinx-mdinclude"
  * Added a Code of Conduct, issue templates and a pull request template to rendered packages
  * Made the single-version CI and Read the Docs jobs track the newest supported Python version
  * Bumped rendered single-version jobs to Python 3.14
  * Added a cache suffix to the uv setup step to avoid CI cache namespace conflicts
  * Excluded unsupported Python/Django combinations (Python 3.14 with Django 4.2 and 5.2) from the rendered CI matrix
  * Fixed the rendered ruff target-version to track the minimum supported Python (matching requires-python) instead of the newest
  * Removed the stale .md source suffix from the rendered Sphinx config, since sphinx-mdinclude provides only the mdinclude directive (not a Markdown source parser)

**1.2.1** (2026-05-27)
  * Fixed incorrect removal versions for several settings: `DATABASE_*` / `TEST_DATABASE_*` (1.2 → 1.4),
    `TRANSACTIONS_MANAGED` (1.4 → 1.8), `AUTH_PROFILE_MODULE` (1.5 → 1.7), the legacy `TEST_*` database
    settings (1.7 → 1.8) and `PASSWORD_RESET_TIMEOUT_DAYS` (3.0 → 4.0)
  * Fixed version comparison so double-digit minor versions (e.g. Django 1.10) are evaluated correctly

**1.2.0** (2026-05-27)
  * Added known settings deprecations from Django 6.1: the `EMAIL_*` settings (replaced by `MAILERS`) and `USE_BLANK_CHOICE_DASH`

**1.1.8** (2026-03-30)
  * Maintenance updates via ambient-package-update

**1.1.7** (2026-03-30)
  * Maintenance updates via ambient-package-update

**1.1.6** (2025-12-16)
  * Added official deprecation docs to readme

**1.1.5** (2025-12-11)
  * Maintenance updates via ambient-package-update

**1.1.4** (2025-10-15)
  * Maintenance updates via ambient-package-update

**1.1.3** (2025-10-10)
  * Maintenance updates via ambient-package-update

**1.1.2** (2025-10-09)
  * Maintenance updates via ambient-package-update

**1.1.1** (2025-10-09)
  * Maintenance updates via ambient-package-update

**1.1.0** (2025-10-08)
  * Added known deprecations for `FORMS_URLFIELD_ASSUME_HTTPS` and `URLIZE_ASSUME_HTTPS`

**1.0.9** (2025-06-05)
  * Fixed issue of wrong deprecation version for `SECURE_BROWSER_XSS_FILTER`

**1.0.8** (2025-05-29)
  * Maintenance updates via ambient-package-update

**1.0.7** (2025-04-03)
  * Maintenance updates via ambient-package-update

**1.0.6** (2025-02-15)
  * Maintenance updates via ambient-package-update

**1.0.5** (2024-11-28)
   * Fixed display bug with two-digit Django versions

**1.0.4** (2024-11-20)
   * Improved docs

**1.0.3** (2024-11-19)
   * Added screenshot to documentation for clarification

**1.0.2** (2024-11-19)
   * Moved `DEFAULT_FILE_STORAGE` removal from Django 3.1 to Django 5.1

**1.0.1** (2024-11-19)
   * Added docs at RTD

**1.0.0** (2024-11-19)
   * Added system checks for all known setting variable removals since Django v1.0
