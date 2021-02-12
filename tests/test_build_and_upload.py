"""
Tests for building distributions for a minimal Python package.
"""
import re
from pathlib import Path
from random import randint
from shutil import rmtree
from subprocess import run
from typing import Iterable

import pytest

from registerit.build_and_upload import build_minimal_python_distribution


@pytest.fixture()
def setup_and_cleanup() -> Iterable[None]:
    yield None
    dist_dir = Path().cwd() / 'dist'
    if dist_dir.exists() and dist_dir.is_dir():
        rmtree(dist_dir)


def test_build_minimal_python_distribution(setup_and_cleanup: Iterable[None]):
    pkg_name = f'this-is-only-a-test-{randint(1, 100)}'

    path_to_dist = build_minimal_python_distribution(
        pkg_name,
        'me',
        'me@me.com',
        'www.me.co'
    )
    assert path_to_dist.is_file()
    assert re.findall('tar.gz$', str(path_to_dist))
    try:
        run(['pip', 'install', str(path_to_dist)], check=True)
    except Exception:
        assert False
    cli_output = run(['pip', 'freeze'], encoding='utf-8', capture_output=True)
    assert re.findall(f'{pkg_name}', cli_output.stdout)
