import pytest

from eva_data_analysis import calculate_crew_size, text_to_duration

def test_text_to_duration_integer():
    """Test function returns expected true value  for durations with no minutes."""
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float():
    """Test function returns expected true value  for durations with non-zero minutes."""
    input_value = "10:20"
    assert text_to_duration(input_value) == pytest.approx(10.3333, rel=1e-4) # defines the tolerance for the approximation, in this case 0.0001

@pytest.mark.parametrize(
    "input_value, expected_result",
    [
        ("John Doe; Jane Smith; Bob Johnson;", 3),
        ("Alice;", 1),
        ("", None),
        ("John Doe; Jane Smith;", 2),
        ("John Doe; Jane Smith; Bob Johnson; Alice;", 4),
    ],
)
def test_calculate_crew_size(input_value, expected_result):
    """Test function for 2 or 3 crew members."""
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result