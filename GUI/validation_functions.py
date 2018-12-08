import os
import logging
import re

logging.basicConfig(filename='server.log', level=logging.DEBUG)


def valid_email(email):
    """Check if entered email address is valid

    This checks if the email address contains a "@" followed by a "."

    Args:
        email (str): input email address

    Returns:
        bool: True if the input is a valid email and False otherwise
    """
    # Ensure email is a string
    if not type(email) == str:
        return False

    # Find @ and . in the email address
    if re.match("[^@]+@[^@]+.[^@]+", email):
        return True

    else:
        return False


def validate_file_exists(filenames):
    """Check if an input filename exists

    Args:
        filenames(list of str): a list of filenames to read

    Returns:
        bool: False if one of the names does not exist, True if all names exist

    """

    for file in filenames:
        if not os.path.exists(file):
            return False

    return True
