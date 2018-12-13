import pytest
from PIL import Image
from GUI.view_images import *


def setup():

    from skimage import data

    # test_im = data.camera()
    test_im = Image.fromarray(np.ones((64, 64), dtype='int8'), mode='1')
    df1 = {'imageInd': 0,
           'orig_im_array': [test_im],
           'proc_im': [test_im],
           'show1': True,
           'show2': True,
           'imdims': [test_im.size]
           }

    # test_im = data.coffee()
    test_im = Image.fromarray(np.ones((128, 128, 3), dtype='int8'), mode='RGB')
    df2 = {'imageInd': 0,
           'orig_im_array': [test_im],
           'proc_im': [test_im],
           'show1': False,
           'show2': True,
           'imdims': [test_im.size]
           }

    return df1, df2


def test_get_num_channels():
    """Test the get_num_channels function

    Returns:

    """

    # Set up sample dictionaries
    df1, df2 = setup()

    # Run the test
    assert get_num_channels(df1) == 1
    assert get_num_channels(df2) == 3


@pytest.mark.parametrize("candidate, expected1, expected2", [
    (1, ['k'], ['BW']),
    (3, ['r', 'g', 'b'], ['Red', 'Green', 'Blue'])
])
def test_hist_colors(candidate, expected1, expected2):
    """Test the hist_colors function

    Args:
        candidate:
        expected1:
        expected2:

    Returns:

    """

    assert hist_colors(candidate) == (expected1, expected2)


def test_separate_ims():
    """Test the separate_ims function.

    Returns:

    """

    df1, df2 = setup()

    # Test 1
    im = separate_ims(df1)
    size = df1['imdims'][0]
    assert im.size == (size[0]*2, size[1])

    # Test 2
    im = separate_ims(df2)
    size = df2['imdims'][0]
    assert im.size == (size[0], size[1])
