import pytest
import os
import numpy as np
from ClientFunctions.read_files import load_image_series, get_zip_names
from ClientFunctions.write_files import write_zip
from Server.serverHelper import *


# @pytest.mark.parametrize("img", [
#     "TestImages/circlesBrightDark.png",
#     "TestImages/circles.png",
#     "TestImages/tire.tif",
#     "TestImages/yellowlily.jpg",
#     "TestImages/foosballraw.tiff"
# ])
def test_base64():
    """
    test_add_parametrize is called with all of the input & expected output
    combinations specified in the decorator above.
    """
    imglist = ["TestImages/circlesBrightDark.png",
               "TestImages/circles.png",
               "TestImages/yellowlily.jpg"]
    a = encode_images_from_file(imglist)
    de = decode_images(a)
    aa = de[-1]

    assert aa.size == (1224, 1632)


def test_unpack_zip_files():

    # Load data
    out_path = 'ProcessedImages/'
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    infiles = ['TestImages/coins.png', 'TestImages/Lenna.png']
    ims, all_filenames = load_image_series(infiles)

    # Set up inputs
    files = ['coins.tif', 'Lenna.tif']
    fileformat = 'TIFF'
    zip_file = write_zip(files, ims, fileformat)

    # Unpack the images
    unpacked_ims = unpack_zip_files(zip_file)

    # Verify that the input and output images are identical
    for im, pim in zip(ims, unpacked_ims):
        assert (np.array(im) == np.array(pim)).all()
