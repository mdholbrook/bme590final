import cv2
import numpy as np
from PIL import Image
from zipfile import ZipFile


def load_image(imfile):
    """This function reads an input image from file

    Args:
        imfile (str): path to an image

    Returns:
        2D or
    """

    im = cv2.imread(imfile)

    return im


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

    # Read each image and append in a list
    img = []
    with ZipFile(zipfilename) as archive:
        for entry in archive.infolist():
            with archive.open(entry) as file:
                print(file)
                tmp = Image.open(file)
                img.append(np.array(tmp))

    # Return the read images
    return img
