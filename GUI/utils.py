def save_email(email):
    """Save the latest user's email so that future sessions can auto-populate
    the GUI with this information

    Args:
        email (str): an email address which has been validated

    Returns:

    """

    f = open('GUI/LastEmail.log', 'w')

    f.write(email)

    f.close()


def load_email():
    """Loads a previously validated email. Only the last-saved email address
    can be recovered.

    If the file is not found a False value is returned and the user must
    enter a valid email.

    Returns:
        str or bool: an email is returned if an email address has been saved,
        otherwise the function return False
    """

    try:
        # Try to open a previously saved file
        f = open('GUI/LastEmail.log', 'r')

        email = f.read()

        f.close()

        return email

    except FileNotFoundError:

        return False
