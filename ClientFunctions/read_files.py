import cv2
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
