import pytest


@pytest.fixture
def sample_data():
    return {"name":"Adam","age":30}



def test_pass_data_to_method(sample_data):
    actual_name="Adam"
    expected_name=sample_data["name"]

    actual_age=30
    expected_age=sample_data["age"]
    assert expected_name in actual_name

    assert  actual_age==expected_age