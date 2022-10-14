from gendiff import generate_diff
import pytest

from tests import get_path


@pytest.mark.parametrize(
    "test_input1,test_input2, formater,  expected",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
            'correct_result.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'stylish',
            'correct_result.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.json',
            'stylish',
            'correct_result.txt',
            id="flat_mix_file"
        ),
        pytest.param(
            'empty_file.json',
            'empty_file.json',
            'stylish',
            'correct_result_empty.txt',
            id="empty_file"
        ),
        pytest.param(
            'file1_tree.json',
            'file2_tree.json',
            'stylish',
            'correct_result_tree.txt',
            id="tree_json_file"
        ),
        pytest.param(
            'file1_tree.yaml',
            'file2_tree.yaml',
            'stylish',
            'correct_result_tree.txt',
            id="tree_yaml_file"
        ),
        pytest.param(
            'file1_tree.yaml',
            'file2_tree.yaml',
            'plain',
            'correct_result_tree_plain.txt',
            id="tree_plain"
        ),
        pytest.param(
            'file1_tree.json',
            'file2_tree.json',
            'json',
            'correct_result_tree_json.txt',
            id="tree_json"
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, formater, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(test_input1)
        test_path2 = get_path(test_input2)
        assert generate_diff(test_path1, test_path2, formater) == result_data
