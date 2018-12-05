import pytest
from GUI.validation_functions import valid_email


@pytest.mark.parametrize("candidate, expected", [
    (12, False),
    ('jim@jim.edu', True),
    ('jim.jim.edu', False),
    ("o'hare@gmail.com", True),
    ('9.2', False)
    ])
def test_valid_email(candidate, expected):

    # Run the test
    assert valid_email(candidate) == expected
