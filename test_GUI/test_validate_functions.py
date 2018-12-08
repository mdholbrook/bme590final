import pytest
from GUI.validation_functions import valid_email, validate_file_exists


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


@pytest.mark.parametrize("candidate, expected", [
    (["TestImages/TestImages.zip", "TestImages/circles.png"], True),
    (["TestImages/Lenna.bmp", "TestImages/tire.tif"], False),
])
def test_validate_file_exists(candidate, expected):

    assert validate_file_exists(candidate) == expected
