import os
import cv2
import numpy as np
from PIL import Image
from zipfile import ZipFile, ZipInfo
from io import BytesIO


def write_image(filename, im):
    """Writes a single images to file

    Args:
        filename (str): name and path of the file to be written
        im (numpy array): image data to be written

    Returns:

    """

    cv2.imwrite(filename, im)


def write_zip(filename, files, ims, file_format):

    # Set up in-memory file
    memory_file = BytesIO()

    # Make a zip file in memory_file
    zf = ZipFile(memory_file, mode='w')

    for z in range(len(files)):

        # Get image
        im = Image.fromarray(ims[z])

        # Set up a temporary image buffer
        tmp = BytesIO()

        # Save image to temporoary buffer
        im.save(memory_file, file_format)

        # Generate new filename using filename and extension
        new_file = files[z] + file_format





    zf.write(filename, memory_file.getvalue())


def gen_file_extension(df):
    """Generates file extensions from the data structure

    Args:
        df (dict): dictionary which contains file format information

    Returns:
        tuple: save file format for PIL, and file extension
    """

    if df['JPEG']:
        fileformat = 'JPEG'
        file_ext = '.jpg'

    elif df['PNG']:
        fileformat = 'PNG'
        file_ext = '.png'

    elif df['TIFF']:
        fileformat = 'TIFF'
        file_ext = '.tif'

    return fileformat, file_ext


if __name__ == "__main__":

    filename = '../ProcessedImages/zipfile.png'

    files = ['../TestImages/foosball.jpg', '../TestImages/coins.png']

    from ClientFunctions.read_files import load_image_series

    ims = load_image_series(files)

    files = ['foosball.jpg', 'coins.png']

    write_image(filename, ims[0])

    filename = '../ProcessedImages/zipfile.zip'

    write_zip(filename, files, ims)
