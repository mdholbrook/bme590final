import base64
from io import BytesIO
from PIL import Image
from zipfile import ZipFile
import numpy as np
import logging
from PIL import Image
from ImageProcessing.ImgFunctions import *


def check_user_data(user_data):
    """
    Checks to see that the input for the /new_user endpoint is
    valid, i.e. a dictionary with the correct key-value pairs and types.

    Args:
        user_data: JSON of data from a server request (from the GUI)

    Returns: The input, if no exceptions are thrown.
    """

    # Ensures that all expected keys are in the dictionary
    # print(user_data)
    if "email" not in user_data or \
            "hist" not in user_data or \
            "cont" not in user_data or \
            "log" not in user_data or \
            "rev" not in user_data or \
            "gamma" not in user_data or \
            "images" not in user_data:
        logging.error("A key is missing from the user data dictionary.")
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
            type(user_data["gamma"]) != bool:
        # app.logger.error("Post-processing method flag not of type bool.")
        raise TypeError

    # Ensures that only one postprocessing method was chosen
    if (user_data["hist"] + user_data["cont"] + user_data["log"] +
       user_data["rev"] + user_data["gamma"]) != 1:
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
    # if type(user_data["extension"]) != str:
    #     raise TypeError
    # if user_data["extension"] != "JPEG" or \
    #         user_data["extension"] != "PNG" or \
    #         user_data["extension"] != "TIFF":
    #     raise ValueError

    return user_data


def decode_images(base64_string):
    """
    Decodes the uploaded image(s).

    Args:
        base64_string: A list of image(s) encoded in base64 format

    Returns: A list of decoded image(s), i.e. as numpy array(s) of floats
    """
    ret = []
    for bytestring in base64_string:
        image_bytes = base64.b64decode(bytestring)
        image_buf = BytesIO(image_bytes)

        try:
            i = Image.open(image_buf)
            ret.append(i)

        except OSError:
            ims = unpack_zip_files(image_buf)

            for i in ims:
                ret.append(np.array(i))
    return ret


def encode_images_from_file(image_paths):
    """
    Encodes the processed image(s).

    Args:
        image_paths: List of input image filepath Strings ex).jpg , .png, .tiff

    Returns: A list of encoded image(s) as ByteStrings
    """
    ret = []
    for path in image_paths:
        with open(path, "rb") as image_file:
            ret.append((base64.b64encode(image_file.read())).decode('utf-8'))
    return ret


def encode_images(images):
    """
    Encodes the processed image(s).

    Args:
        images: A list of input images (nparrays)

    Returns: A list of encoded image(s) as ByteStrings
    """
    ret = []
    for image in images:
        ret.append((base64.b64encode(image)).decode('utf-8'))
    return ret


def unpack_zip_files(zip_file):
    """
    Unzips in-memory zip files to return a list of PIL Image objects
    Args:
        zip_file (BytesIO): an in-memory zip file, containing images to process

    Returns:
        list of PIL image objects: a list of the unpacked images
    """

    # Open the zip file
    zip_file.seek(0)
    file = ZipFile(BytesIO(zip_file.read()))

    # Get the list of file contents
    names = file.infolist()

    # Read from zip file
    ims = []
    for name in names:

        # Read from zip file
        tmp = file.open(name)

        # Convert data to Image
        tmp = Image.open(tmp)

        # Append PIL Image objects
        ims.append(tmp)

    return ims


def compute_histograms(raw_images):
    """
    This function takes a list of images and computes the histograms of each
    Args:
        raw_images (list of numpy arrays): a list of numpy array images

    Returns:
        list: bins and histogram information formatted as following [image
        #][bins or counts][channel]
    """

    # Calculates histogram data for all original images and packages it
    # to return to GUI client
    histogram_data = []
    image_sizes = []
    for image in raw_images:
        image_sizes.append([image.shape[0], image.shape[1]])
        data_per_image = []

        # If the images has one channel or is BW
        if len(image.shape) == 2:
            hist, bins = view_histogram_bw(image)

        else:
            hist, bins = view_color_histogram(image)

        # Concatenate histogram data
        data_per_image.append(bins)
        data_per_image.append(hist)
        histogram_data.append(data_per_image)

    return histogram_data, image_sizes


def save_ims_to_memory(user):
    """
    This function takes images and numpy arrays and encodes them as PNG files
    in an in-memory buffer
    Args:
        user (class): a class containing the image arrays to be processed

    Returns:
        list: a list of BytesIO objects containing image files
    """

    # Encodes the processed images to prepare to return them to the client
    memory_file = []
    for image in user.processedImages:
        # import matplotlib.pyplot as plt
        # plt.imshow(image), plt.show()

        memory_file.append(BytesIO())
        if len(image.shape) == 2:
            if image.dtype == bool:
                image = image.astype(np.uint8)

            file_format = "L"
            image *= 255
            image = image.astype(np.uint8)
        else:
            file_format = "RGB"
        im = Image.fromarray(image, mode=file_format)
        im.save(memory_file[-1], "PNG")

    file_paths = []
    for file in memory_file:
        file_paths.append(file.getvalue())

    logging.debug(type(memory_file[0]))

    return file_paths
