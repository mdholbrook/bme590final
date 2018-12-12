import base64


def check_user_data(user_data):
    """
    Checks to see that the input for the /new_user endpoint is
    valid, i.e. a dictionary with the correct key-value pairs and types.

    Args:
        user_data: JSON of data from a server request (from the GUI)

    Returns: The input, if no exceptions are thrown.
    """

    # Ensures that all expected keys are in the dictionary
    if "hist" not in user_data or \
            "cont" not in user_data or \
            "log" not in user_data or \
            "rev" not in user_data or \
            "median" not in user_data or \
            "images" not in user_data or \
            "extension" not in user_data:
        # app.logger.error("A key is missing from the user data dictionary.")
        raise KeyError

    # Ensures that there are no empty values in the dictionary
    if None in user_data.values():
        # app.logger.error("One of the fields is empty.")
        raise ValueError

    # # Ensures that the filenames are of type String
    # if type(user_data["load_filenames"]) == list:
    #     for filename in user_data["load_filenames"]:
    #         if type(filename) != str:
    #            # app.logger.error("Filepath of one of the files not String.")
    #             raise TypeError
    # elif type(user_data["load_filenames"]) != str:
    #     # app.logger.error("Filepath of single file not String.")
    #     raise TypeError

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

    # Ensures that the images are of type String (i.e. a ByteString)
    if type(user_data["images"]) == list:
        for image in user_data["images"]:
            if type(image) != str:
                # app.logger.error("One of the images was not encoded.")
                raise TypeError
    elif type(user_data["images"]) != str:
        # app.logger.error("The image was not properly encoded.")
        raise TypeError

    # Ensures that the extension type is a String, and one that makes sense
    if type(user_data["extension"]) != str:
        raise TypeError
    if user_data["extension"] != "JPEG" or \
            user_data["extension"] != "PNG" or \
            user_data["extension"] != "TIFF":
        raise ValueError

    return user_data


def decode_images(images):
    """
    Decodes the uploaded image(s).

    Args:
        images: A list of image(s) encoded in base64 format

    Returns: A list of decoded image(s), i.e. as float array(s)
    """
    ret = []
    for image in images:
        ret.append(base64.b64decode(image))
    return ret


def encode_images(images):
    """
    Encodes the processed image(s).

    Args:
        images: A list of raw image(s), i.e. as float array(s)

    Returns: A list of encoded image(s) as ByteStrings
    """
    ret = []
    for image in images:
        ret.append(base64.b64encode(image))
    return ret
