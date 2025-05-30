[![PyPI release](https://img.shields.io/pypi/v/django-removals.svg)](https://pypi.org/project/django-removals/)
[![Downloads](https://static.pepy.tech/badge/django-removals)](https://pepy.tech/project/django-removals)
[![Coverage](https://img.shields.io/badge/Coverage-100.0%25-success)](https://github.com/ambient-innovation/django-removals/actions?workflow=CI)
[![Linting](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Coding Style](https://img.shields.io/badge/code%20style-Ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Documentation Status](https://readthedocs.org/projects/django-removals/badge/?version=latest)](https://django-removals.readthedocs.io/en/latest/?badge=latest)

Welcome to the **django-removals** - a maintainer's best friend for finding removed features in your Django project

* [PyPI](https://pypi.org/project/django-removals/)
* [GitHub](https://github.com/ambient-innovation/django-removals)
* [Full documentation](https://django-removals.readthedocs.io/en/latest/index.html)
* Creator & Maintainer: [Ambient Digital](https://ambient.digital/)


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



### Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD) if the GitHub webhook is not yet set
  up.

### Publish to PyPi

- Update documentation about new/changed functionality

- Update the `Changelog`

- Increment version in main `__init__.py`

- Create pull request / merge to main

- This project uses the flit package to publish to PyPI. Thus, publishing should be as easy as running:
  ```
  flit publish
  ```

  To publish to TestPyPI use the following to ensure that you have set up your .pypirc as
  shown [here](https://flit.readthedocs.io/en/latest/upload.html#using-pypirc) and use the following command:

  ```
  flit publish --repository testpypi
  ```

### Maintenance

Please note that this package supports the [ambient-package-update](https://pypi.org/project/ambient-package-update/).
So you don't have to worry about the maintenance of this package. This updater is rendering all important
configuration and setup files. It works similar to well-known updaters like `pyupgrade` or `django-upgrade`.

To run an update, refer to the [documentation page](https://pypi.org/project/ambient-package-update/)
of the "ambient-package-update".
