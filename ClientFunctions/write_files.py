import os
import cv2
import numpy as np
from PIL import Image
from zipfile import ZipFile, ZipInfo
import io


def write_image(filename, im):
    """Writes a single images to file

    Args:
        filename (str): name and path of the file to be written
        im (numpy array): image data to be written

    Returns:

    """

    cv2.imwrite(filename, im)


def write_zip(filename, files, ims):

    for z in range(len(files)):
        memory_file = io.BytesIO()

        zf = ZipFile(filename, mode='w')

        im = Image.fromarray(ims[z])

        im.save(memory_file, 'JPEG')

    zf.write(filename, memory_file.getvalue())


if __name__ == "__main__":

    filename = '../ProcessedImages/zipfile.png'

    files = ['../TestImages/foosball.jpg', '../TestImages/coins.png']

    from ClientFunctions.read_files import load_image_series

    ims = load_image_series(files)

    files = ['foosball.jpg', 'coins.png']

    write_image(filename, ims[0])

    filename = '../ProcessedImages/zipfile.zip'

    write_zip(filename, files, ims)
