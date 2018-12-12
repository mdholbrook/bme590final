import os
import base64
import numpy as np
from PIL import Image
from zipfile import ZipFile


def load_file_bytes(imfile):
    """This function takes the name of a file and returns an base 64 encoded
    in-memory file

    Args:
        imfile (str): path to string object

    Returns:
        bytes: an in-memory base64 encoding of the input file
    """

    with open(imfile, "rb") as image_file:
        return base64.b64encode(image_file.read())


def load_image(imfile):
    """This function reads an input image from file

    Args:
        imfile (str): path to an image

    Returns:
        2D or 3D numpy array of image values
    """

    im = Image.open(imfile)

    return [im]


def get_zip_names(zipfilename):
    """This function pulls the names of files found in a zip file

    Args:
        zipfilename (str): path to the selected zip file

    Returns:
        list of str: a list of files found in the zip file
    """

    # Get names from the zip file
    zipfiles = []
    with ZipFile(zipfilename) as archive:
        for file in archive.infolist():
            zipfiles.append(file.filename)

    return zipfiles


def load_zipped_image(zipfilename):
    """Loads image files contained in a zip file

    Args:
        zipfilename (str): path to the selected zip file

    Returns:
        list of numpy arrays: a list image image data found in the zip file
    """

    # Read each image and append in a list
    img = []
    filenames = []
    with ZipFile(zipfilename) as archive:
        for entry in archive.infolist():
            with archive.open(entry) as file:
                tmp = Image.open(file)
                img.append(np.array(tmp))
                filenames.append(file.name)

    # Return the read images
    return img, filenames


def flatten(filenames):
    """Takes a list which may contain other lists and returns a single,
    flattened list

    Args:
        filenames (list): list of filenames

    Returns:
        flattened list of filenames
    """

    flat_filenames = [file for i in filenames for file in i]

    return flat_filenames


def load_image_series(filenames):
    """This function takes a list of filenames and returns a list of numpy
    arrays containing image data.

    Args:
        filenames (list of str): a list of filenames selected in the GUI

    Returns:
        list numpy arrays containing image data
    """

    # Cycle through each file
    ims = []
    all_filenames = []
    for file in filenames:

        # Get file extension
        _, ext = os.path.splitext(file)

        # If file is a zip file read with load_zipped_image
        if ext == '.zip':
            filename = get_zip_names(file)
            all_filenames.append(filename)

        else:
            all_filenames.append(file)

        im = load_file_bytes(file)
        ims.append(im)

    # Convert lists of lists into lists
    ims = flatten(ims)
    all_filenames = flatten([all_filenames])

    return ims, all_filenames
