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


def write_zip(filename, files, ims, fileformat):
    """
    This function makes an in-memory zip file of image files and writes them
    to disk.

    Args:
        filename (str): name of the zip file which will be saved to disk
        files (list of str): list of filenames generated for saving, one for
            each image to be saved
        ims (list of numpy array): a list of image data to be saved
        fileformat (str): file encoding method to be used. Valid values are
        "JPEG", "PNG", and "TIFF".

    Returns:

    """

    # Set up in-memory file
    memory_file = BytesIO()

    # Make a zip file inside of the in-memory file
    zf = ZipFile(memory_file, mode='w')

    # For each image
    for i in range(len(files)):

        # Get a single image and create a PIL object
        im = Image.fromarray(ims[i])

        # Set up a temporary image buffer
        tmp = BytesIO()

        # Save image to a temporary buffer using an encoding defined by
        # fileformat
        im.save(tmp, fileformat)

        # Save image into the in-memory zip file
        zf.write(files[i], tmp.getvalue())

    # Close the in-memory zip file
    zf.close()

    # Write zip file to disk as bytes encoding
    with open(filename, 'wb') as f:
        f.write(memory_file.getvalue())


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


def save_images(df):
    """
    This function serves as the parent function for writing processed images
    to disk

    Args:
        df (dict): dictionary containing the processed images 'proc_im',
            original image filenames 'loaded_filenames'], the save file name
            'save_filename' and file extension information.

    Returns:

    """

    # Determine if we save an image or zip file
    if len(df['loaded_filenames']) == 1:

        # Save a single image
        write_image(df['save_filename'], df['proc_im'])

    else:

        # Get save file extension and encoding
        fileformat, file_ext = gen_file_extension(df)

        # Save a zip file of images
        write_zip(df['save_filename'], df['load_filenames'],
                  df['proc_im'], file_ext)


if __name__ == "__main__":

    filename = '../ProcessedImages/zipfile.png'

    files = ['../TestImages/foosball.jpg', '../TestImages/coins.png']

    from ClientFunctions.read_files import load_image_series

    ims = load_image_series(files)

    files = ['foosball.jpg', 'coins.png']

    write_image(filename, ims[0])

    filename = '../ProcessedImages/zipfile.zip'

    write_zip(filename, files, ims)
