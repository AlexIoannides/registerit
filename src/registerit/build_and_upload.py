"""
Functions for assembling a minimal Python package in a temporary
directory and upload it to PyPI, so that the package name can be
registered as belonging to the author (while they develope the
codebase).
"""
from pathlib import Path
from shutil import rmtree
from subprocess import CalledProcessError, run
from tempfile import mkdtemp


def _render_minimal_module_py() -> str:
    """Render the contents for an arbitraty Python module.

    :return: Module contents as text.
    """
    return 'print("Hello Production!")'


def _render_minimal_setup_py(
    package_name: str,
    author: str,
    email: str,
    url: str
) -> str:
    """Render the contents for an arbitraty Python module.

    :param package_name: The name of the package to be registered.
    :param author: Name of package author.
    :param email: E-mail address of package author.
    :param url: URL for package (website or repo).
    :return:  Module contents as text.
    """
    setup = (f'from setuptools import setup\n'
             f'setup(name="{package_name}", version="0.0.1", py_modules=["module"],'
             f'author="{author}", author_email="{email}",'
             f'url="{url}")')
    return setup


def build_minimal_python_distribution(
    package_name: str,
    author: str,
    email: str,
    url: str
) -> Path:
    """Build a source distribution for a minimal Python package.

    Create a minimal Python package structure in a temporary directory
    and build a source distribution from it.

    :param package_name: The name of the package to be registered.
    :param author: Name of package author.
    :param email: E-mail address of package author.
    :param url: URL for package (website or repo).
    :return: Path to the source distribution.
    """
    temp_dir = mkdtemp(dir=Path().cwd())
    temp_dir_path = Path(temp_dir)

    setup_py_path = temp_dir_path / 'setup.py'
    setup_py_path.write_text(_render_minimal_setup_py(package_name, author, email, url))

    module_py_path = temp_dir_path / 'module.py'
    module_py_path.write_text(_render_minimal_module_py())

    try:
        run(['python3', setup_py_path.absolute(), 'sdist'], check=True)
    except CalledProcessError:
        print('ERROR: cannot create skeleton Python package for uploading to PyPI.')
    finally:
        metadata_dir = Path().cwd() / f'{package_name}.egg-info'
        rmtree(metadata_dir)
        rmtree(temp_dir_path)

    dist_dir = Path().cwd() / 'dist'
    dist = list(dist_dir.glob('*.tar.gz'))
    return dist[0]


def upload_distribution_to_pypi(distribution: Path, username: str, password: str) -> None:
    """Upload a source distribution to PyPI.

    :param distribution: Path to source distribution.
    :param username: PyPI username.
    :param password: PyPI passwork.
    """
    try:
        run(
            ['twine', 'upload', distribution.absolute(), '-u', username, '-p', password],
            check=True
        )
    except CalledProcessError:
        print('ERROR: cannot upload skeleton Python distribution to PyPI.')
    finally:
        rmtree(distribution.parent)
