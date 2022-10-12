import os
import pytest


from gendiff import cli


def test_help_command():
    exit_status = os.system('gendiff -h')
    assert exit_status == 0


def test_cli_without_arg():
    with pytest.raises(SystemExit) as pytest_error:
        cli.parse_arguments()()
    assert pytest_error.type == SystemExit
    assert pytest_error.value.code == 2
