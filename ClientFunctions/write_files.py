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


def write_zip(filename, files, ims, fileformat, file_ext):

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
        im.save(memory_file, fileformat)

        # Generate new filename using filename and extension
        base = os.path.basename(files[z])
        file, _ = os.path.splitext(base)
        file = file + file_ext


    zf.write(filename, memory_file.getvalue())


def gen_save_filename(file, file_ext):
    """
    Generates a new filename for saving zipfile images based on the name
    naming convention as the original file
    Args:
        file (str): original image filename
        file_ext (str): extension to be used for saving the processed image

    Returns:
        str: a new filename which will be used in the saved zip file
    """

    # Split path to original filename to get only the name with a new extension
    base = os.path.basename(file)
    file, _ = os.path.splitext(base)

    # Return filename with appended extension
    return file + file_ext


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
