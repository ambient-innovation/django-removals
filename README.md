[![PyPI release](https://img.shields.io/pypi/v/django-removals.svg)](https://pypi.org/project/django-removals/)
[![Downloads](https://static.pepy.tech/badge/django-removals)](https://pepy.tech/project/django-removals)
[![Coverage](https://img.shields.io/badge/Coverage-100.0%25-success)](https://github.com/ambient-innovation/django-removals/actions?workflow=CI)
[![Linting](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Coding Style](https://img.shields.io/badge/code%20style-Ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Documentation Status](https://readthedocs.org/projects/django-removals/badge/?version=latest)](https://django-removals.readthedocs.io/en/latest/?badge=latest)

Welcome to the **django-removals** - a maintainer's best friend for finding removed features in your Django project

[PyPI](https://pypi.org/project/django-removals/) • [GitHub](https://github.com/ambient-innovation/django-removals) • [Full documentation](https://django-removals.readthedocs.io/en/latest/index.html)

Creator & Maintainer: [Beyonder Deutschland](https://beyonder.de/)

## Features

This package will throw [Django system checks](https://docs.djangoproject.com/en/dev/topics/checks/)
warnings for all known removals from Django v1.0 to today.

Here's an example:

![Example system check](https://raw.githubusercontent.com/ambient-innovation/django-removals/963cdef1f04b9f3f8efbe6a4a893ef4abe911e07/docs/system_check_warning.png?raw=True)

The checks will either be triggered when using the Django development server

`python manage.py runserver`

or when you call the checks manually

`python manage.py check --deploy`

It focuses on Django settings but might also add more checks in the future.

## Sources

You can read up on Django deprecations in
[the official docs](https://docs.djangoproject.com/en/dev/internals/deprecation/).

## Installation

- Install the package via pip:

  `pip install django-removals`

  or via pipenv:

  `pipenv install django-removals`

- Add module to `INSTALLED_APPS` within the main django `settings.py`:

    ```python
    INSTALLED_APPS = (
        # ...
        "django_removals",
    )
    ```

Since this package adds only Django system checks, which don't run on production, you could add it only when being in
(local) debug mode.

```python
if DEBUG_MODE:
    INSTALLED_APPS += ("django_removals",)
```

## Releasing a new version

Releases are fully automated. Push a version tag and the pipeline will build, sign with
[Sigstore](https://www.sigstore.dev/), publish to PyPI via
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/), and create a GitHub Release —
no API tokens needed.

```bash
git tag v<version>          # e.g. git tag v1.2.3
git push origin v<version>
```

Tags **must** start with `v`. Tags without the prefix won't trigger the pipeline.

### First-time setup

Before the pipeline can run for the first time, an admin must:

1. **Create GitHub Environment `pypi`**
   - Go to *Settings → Environments → New environment*, name it exactly `pypi`
   - Under *Deployment branches and tags*, add a tag rule with pattern `v*`
   - Optionally add required reviewers for a manual approval gate

2. **Configure PyPI Trusted Publisher**
   - Go to *PyPI → Project settings → Publishing → Add a new publisher*
   - Fill in: Owner `ambient-innovation`, Repository `django-removals`,
     Workflow `release.yml`, Environment `pypi`

### Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD) if the GitHub webhook is not yet set
  up.

### Maintenance

Please note that this package supports the [ambient-package-update](https://pypi.org/project/ambient-package-update/).
So you don't have to worry about the maintenance of this package. This updater is rendering all important
configuration and setup files. It works similar to well-known updaters like `pyupgrade` or `django-upgrade`.

To run an update, refer to the [documentation page](https://pypi.org/project/ambient-package-update/)
of the "ambient-package-update".
