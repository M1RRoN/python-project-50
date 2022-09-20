from gendiff.engine import generate_diff, run_gendiff
import pytest


def test_generate_diff():
    answer = open(r'C:\Users\M1rr0n\python-project-50\tests\fixtures\result.txt')
    assert run_gendiff(r'C:\Users\M1rr0n\python-project-50\tests\fixtures\file1.json', r'C:\Users\M1rr0n\python-project-50\tests\fixtures\file2.json') == print(answer)


def test_generate_diff_wrong_format():
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.wrong')
