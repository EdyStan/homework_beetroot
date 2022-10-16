import pytest
from task_1_class import MyOpen


@pytest.fixture
def replace_file_obj():
    return "pytest_input.txt"


@pytest.fixture
def data_to_check(replace_file_obj):
    with MyOpen(replace_file_obj, 'r') as io_file:
        data = io_file.read(9)
        return data


def test_data(data_to_check):
    assert data_to_check == 'Some text'
