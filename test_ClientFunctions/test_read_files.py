import pytest
from ClientFunctions.read_files import *


@pytest.mark.parametrize("file, shape", [
    ('TestImages/Lenna.png', (220, 220, 3)),
    ('TestImages/coins.png', (246, 300, 3))
])
def test_load_image(file, shape):

    im = load_image(file)

    assert im.shape == shape


def test_get_zip_names():

    zipfile = 'TestImages/Ims.zip'

    get_zip_names(zipfile)