import pytest
from skimage import io
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
    assert aa.size == 5992704
