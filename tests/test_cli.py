"""
Basic tests for the CLI.
"""
import re
from subprocess import CalledProcessError, run


def test_cli_exists():
    try:
        cli_output = run(
            ['registerit', '--help'],
            check=True,
            capture_output=True,
            encoding='utf-8'
        )
    except CalledProcessError:
        assert False
    assert re.findall('Usage: registerit', cli_output.stdout)
