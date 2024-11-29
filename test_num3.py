import pytest
from unittest.mock import Mock, patch
from numerology_calculator import get_life_path_number

# Test to check if 'life_path_number' is a dictionary and contains the required keys
@patch("numerology_calculator.requests.get")
def test_life_path_number_has_required_keys(mock_get):
    # Mock the API response
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": "ok",
        "data": {
            "life_path_number": {
                "name": "Life Path Number",
                "number": 11,
                "description": "The number 11 is a unique number that represents insight and enlightenment..."
            }
        }
    }
    mock_get.return_value = mock_response

    # Define test inputs
    access_token = "test_access_token"
    birth_date_time = "1987-02-20T15:55:00Z"

    # Call the function to get the result
    result = get_life_path_number(access_token, birth_date_time)

    # Check if 'life_path_number' is a dictionary and contains the required keys
    life_path_data = result['data']['life_path_number']
    assert isinstance(life_path_data, dict), "'life_path_number' should be a dictionary"
    assert "name" in life_path_data, "'life_path_number' should have the key 'name'"
    assert "number" in life_path_data, "'life_path_number' should have the key 'number'"
    assert "description" in life_path_data, "'life_path_number' should have the key 'description'"

# Test to check if the 'description' is a string
@patch("numerology_calculator.requests.get")
def test_description_is_string(mock_get):
    # Mock the API response
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": "ok",
        "data": {
            "life_path_number": {
                "name": "Life Path Number",
                "number": 11,
                "description": "The number 11 is a unique number that represents insight and enlightenment..."
            }
        }
    }
    mock_get.return_value = mock_response

    # Define test inputs
    access_token = "test_access_token"
    birth_date_time = "1987-02-20T15:55:00Z"

    # Call the function to get the result
    result = get_life_path_number(access_token, birth_date_time)

    # Check if 'description' is a string
    life_path_data = result['data']['life_path_number']
    assert isinstance(life_path_data['description'], str), "The 'description' should be a string"
