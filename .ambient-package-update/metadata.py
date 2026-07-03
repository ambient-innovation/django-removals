from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import (
    DEV_DEPENDENCIES,
    LICENSE_MIT,
    SUPPORTED_DJANGO_VERSIONS,
    SUPPORTED_PYTHON_VERSIONS,
)
from ambient_package_update.metadata.maintainer import PackageMaintainer
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent

METADATA = PackageMetadata(
    package_name="django-removals",
    github_package_group="ambient-innovation",
    authors=[
        PackageAuthor(
            name="Beyonder Deutschland",
            email="hello@beyonder.de",
        ),
    ],
    maintainer=PackageMaintainer(name="Beyonder Deutschland", url="https://beyonder.de/", email="hello@beyonder.de"),
    licenser="Beyonder Deutschland GmbH",
    claim="Tool for finding removed features in your Django project",
    license=LICENSE_MIT,
    license_year=2024,
    development_status="5 - Production/Stable",
    has_migrations=False,
    readme_content=ReadmeContent(uses_internationalisation=False),
    main_branch="main",
    dependencies=[
        f"Django>={SUPPORTED_DJANGO_VERSIONS[0]}",
    ],
    supported_django_versions=SUPPORTED_DJANGO_VERSIONS,
    supported_python_versions=SUPPORTED_PYTHON_VERSIONS,
    optional_dependencies={
        "dev": [
            *DEV_DEPENDENCIES,
        ],
    },
    ruff_ignore_list=[],
)
