def check_user_data(user_data):
    """
    Checks to see that the input for the /new_user endpoint is
    valid, i.e. a dictionary with the correct key-value pairs and types.

    Args:
        user_data: JSON of data from a server request (from the GUI)

    Returns: The input, if no exceptions are thrown.
    """

    # Ensures that all expected keys are in the dictionary
    if "load_filenames" not in user_data or \
            "hist" not in user_data or \
            "cont" not in user_data or \
            "log" not in user_data or \
            "rev" not in user_data or \
            "median" not in user_data:
        # app.logger.error("A key is missing from the user data dictionary.")
        raise KeyError

    # Ensures that there are no empty values in the dictionary
    if None in user_data.values():
        # app.logger.error("One of the fields is empty.")
        raise ValueError

    # Ensures that the filenames are of type String
    if type(user_data["load_filenames"]) == list:
        for filename in user_data["load_filenames"]:
            if type(filename) != str:
                # app.logger.error("Filepath of one of the files not String.")
                raise TypeError
    elif type(user_data["load_filenames"]) != str:
        # app.logger.error("Filepath of single file not String.")
        raise TypeError

    # Ensures that the postprocessing flags are of type bool
    if type(user_data["hist"]) != bool or \
            type(user_data["cont"]) != bool or \
            type(user_data["log"]) != bool or \
            type(user_data["rev"]) != bool or \
            type(user_data["median"]) != bool:
        # app.logger.error("Post-processing method flag not of type bool.")
        raise TypeError

    # Ensures that only one postprocessing method was chosen
    if (user_data["hist"] + user_data["cont"] + user_data["log"] +
       user_data["rev"] + user_data["median"]) != 1:
        # app.logger.error("Too many post-processing methods chosen.")
        raise RuntimeError

    # if "@" not in user_data["email"] or \
    #         "." not in user_data["email"]:
    #     # app.logger.error("Email address missing a special character "
    #     # "('@' or '.')")
    #     raise ValueError

    return user_data