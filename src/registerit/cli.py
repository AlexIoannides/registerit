"""
Command Line Interface (CLI) for registerit.
"""
import click
from twine.utils import DEFAULT_REPOSITORY

from .build_and_upload import (
    build_minimal_python_distribution,
    upload_distribution_to_pypi
)


@click.command()
@click.argument('package_name', required=True, type=str)
@click.option('--username', '-u', required=True, type=str)
@click.option('--password', '-p', required=True, type=str)
@click.option('--author', required=False, type=str, default='me')
@click.option('--email', required=False, type=str, default='me@me.com')
@click.option('--url', required=False, type=str, default='http://www.github.com')
@click.option('--repository-url', required=False, type=str, default=DEFAULT_REPOSITORY)
def cli(
    package_name: str,
    username: str,
    password: str,
    author: str,
    email: str,
    url: str,
    repository_url: str
) -> None:
    """Register package names on PyPI."""
    try:
        minimal_dist = build_minimal_python_distribution(
            package_name,
            author,
            email,
            url
        )
        upload_distribution_to_pypi(minimal_dist, username, password, repository_url)
        print(f'{package_name} successfully registered on PyPI.')
    except RuntimeError as e:
        print(f'ERROR: {e}')
