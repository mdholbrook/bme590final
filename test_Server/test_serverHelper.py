import pytest
from PIL import Image
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
    a = encode_images_from_file(["TestImages/Lenna.png"])
    de = decode_images(a)
    aa = de[0]
    im = Image.open("TestImages/Lenna.png")
    assert aa.size == im.size
