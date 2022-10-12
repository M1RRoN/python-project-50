import pytest

from gendiff.file_processor.gendiff import generate_diff
from gendiff.file_processor.file_handler import read_file
from gendiff.file_processor.file_handler import FILEREAD_ERR
from gendiff.file_processor.data_loader import load_json, load_yaml
from gendiff.file_processor.data_loader import UNSUPPORTED_TYPE, INVALID_FILE
from gendiff.formatters.tree_render import (
    FORMAT_STYLISH, FORMAT_PLAIN, FORMAT_JSON, UNSUPPORTED_FORMAT
)


FLAT_JSON1 = 'tests/fixtures/diff_requests/file1.json'
FLAT_JSON2 = 'tests/fixtures/diff_requests/file2.json'
FLAT_YAML1 = 'tests/fixtures/diff_requests/file1.yaml'
FLAT_YAML2 = 'tests/fixtures/diff_requests/file2.yaml'
FLAT_YML1 = 'tests/fixtures/diff_requests/file1.yml'
FLAT_YML2 = 'tests/fixtures/diff_requests/file2.yml'
NESTED_JSON1 = 'tests/fixtures/diff_requests/file3.json'
NESTED_JSON2 = 'tests/fixtures/diff_requests/file4.json'
NESTED_YAML1 = 'tests/fixtures/diff_requests/file3.yaml'
NESTED_YAML2 = 'tests/fixtures/diff_requests/file4.yaml'
NESTED_YML1 = 'tests/fixtures/diff_requests/file3.yml'
NESTED_YML2 = 'tests/fixtures/diff_requests/file4.yml'

RESPONSE_STYLISH_FLAT = 'tests/fixtures/diff_responses/stylish_flat.txt'
RESPONSE_STYLISH_NESTED = 'tests/fixtures/diff_responses/stylish_nested.txt'
RESPONSE_PLAIN_FLAT = 'tests/fixtures/diff_responses/plain_flat.txt'
RESPONSE_PLAIN_NESTED = 'tests/fixtures/diff_responses/plain_nested.txt'
RESPONSE_JSON_FLAT = 'tests/fixtures/diff_responses/json_flat.txt'
RESPONSE_JSON_NESTED = 'tests/fixtures/diff_responses/json_nested.txt'


@pytest.mark.parametrize('file1, file2, format, response_file_path', [
    (FLAT_JSON1, FLAT_JSON2, FORMAT_STYLISH, RESPONSE_STYLISH_FLAT),
    (FLAT_YAML1, FLAT_YAML2, FORMAT_STYLISH, RESPONSE_STYLISH_FLAT),
    (FLAT_YML1, FLAT_YML2, FORMAT_STYLISH, RESPONSE_STYLISH_FLAT),
    (NESTED_JSON1, NESTED_JSON2, FORMAT_STYLISH, RESPONSE_STYLISH_NESTED),
    (NESTED_YAML1, NESTED_YAML2, FORMAT_STYLISH, RESPONSE_STYLISH_NESTED),
    (NESTED_YML1, NESTED_YML2, FORMAT_STYLISH, RESPONSE_STYLISH_NESTED),
    (FLAT_JSON1, FLAT_JSON2, FORMAT_PLAIN, RESPONSE_PLAIN_FLAT),
    (FLAT_YAML1, FLAT_YAML2, FORMAT_PLAIN, RESPONSE_PLAIN_FLAT),
    (FLAT_YML1, FLAT_YML2, FORMAT_PLAIN, RESPONSE_PLAIN_FLAT),
    (NESTED_JSON1, NESTED_JSON2, FORMAT_PLAIN, RESPONSE_PLAIN_NESTED),
    (NESTED_YAML1, NESTED_YAML2, FORMAT_PLAIN, RESPONSE_PLAIN_NESTED),
    (NESTED_YML1, NESTED_YML2, FORMAT_PLAIN, RESPONSE_PLAIN_NESTED),
    (FLAT_JSON1, FLAT_JSON2, FORMAT_JSON, RESPONSE_JSON_FLAT),
    (FLAT_YAML1, FLAT_YAML2, FORMAT_JSON, RESPONSE_JSON_FLAT),
    (FLAT_YML1, FLAT_YML2, FORMAT_JSON, RESPONSE_JSON_FLAT),
    (NESTED_JSON1, NESTED_JSON2, FORMAT_JSON, RESPONSE_JSON_NESTED),
    (NESTED_YAML1, NESTED_YAML2, FORMAT_JSON, RESPONSE_JSON_NESTED),
    (NESTED_YML1, NESTED_YML2, FORMAT_JSON, RESPONSE_JSON_NESTED)
])
def test_generate_diff(file1, file2, format, response_file_path):
    with open(response_file_path) as file:
        expected_result = file.read()
    assert expected_result == generate_diff(file1, file2, format)


def test_open_file_fail():
    with pytest.raises(RuntimeError) as pytest_error:
        read_file('wrong file path')
    assert pytest_error.type == RuntimeError
    assert str(pytest_error.value) == FILEREAD_ERR.format('wrong file path')


def test_unsupported_file_format():
    with pytest.raises(ValueError) as pytest_error:
        generate_diff(RESPONSE_STYLISH_FLAT, RESPONSE_STYLISH_NESTED)
    assert pytest_error.type == ValueError
    assert str(pytest_error.value) == UNSUPPORTED_TYPE.format('.txt')


def test_load_json_err():
    with pytest.raises(RuntimeError) as pytest_error:
        load_json('{"host": "hexlet.io",""}')
    assert pytest_error.type == RuntimeError
    assert str(pytest_error.value) == INVALID_FILE


def test_load_yaml_err():
    with pytest.raises(RuntimeError) as pytest_error:
        load_yaml('host: "hexlet.io":')
    assert pytest_error.type == RuntimeError
    assert str(pytest_error.value) == INVALID_FILE


def test_unsupported_render_format():
    with pytest.raises(ValueError) as pytest_error:
        generate_diff(FLAT_JSON1, FLAT_JSON2, 'wrong format')
    assert pytest_error.type == ValueError
    assert str(pytest_error.value) == UNSUPPORTED_FORMAT
