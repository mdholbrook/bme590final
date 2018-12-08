import pytest
from ClientFunctions.read_files import *


@pytest.mark.parametrize("file, shape", [
    ('TestImages/Lenna.png', (220, 220, 3)),
    ('TestImages/coins.png', (246, 300, 3))
])
def test_load_image(file, shape):

    im = load_image(file)

    assert im[0].shape == shape


def test_get_zip_names():

    zipfile = 'TestImages/TestImages.zip'
    names = ['circles.png',
             'circlesBrightDark.png',
             'coins.png', 'foosball.jpg',
             'foosballraw.tiff',
             'football.jpg',
             'Lenna.png',
             'tire.tif',
             'yellowlily.jpg'
             ]

    zipnames = get_zip_names(zipfile)

    assert zipnames == names


def test_load_zipped_image():

    # Set up test case
    filename = 'TestImages/TestImages.zip'
    file_sizes = [(256, 256),
                  (512, 512),
                  (246, 300),
                  (2336, 3504, 3),
                  (2348, 3522),
                  (256, 320, 3),
                  (220, 220, 3),
                  (205, 232),
                  (1632, 1224, 3)]

    # Test function
    ims = load_zipped_image(filename)

    # Assert that the correct number of images were found
    assert len(ims) == len(file_sizes)

    # Assert that the images shapes are correct
    for i in range(len(ims)):
        assert ims[i].shape == file_sizes[i]


@pytest.mark.parametrize("lists, answer", [
    ([[1], [2, 3], [3, 4, 5]], [1, 2, 3, 3, 4, 5]),
    ([['png'], ['jpg', 'tif']], ['png', 'jpg', 'tif'])
])
def test_flatten(lists, answer):

    files = flatten(lists)

    assert files == answer


def test_load_image_series():

    # Set up test cases using TestImages
    filenames = ['TestImages\\circles.png',
                 'TestImages\\circlesBrightDark.png',
                 'TestImages\\coins.png',
                 'TestImages\\foosball.jpg',
                 'TestImages\\foosballraw.tiff',
                 'TestImages\\football.jpg',
                 'TestImages\\Lenna.png',
                 # 'TestImages\\TestImages.zip',
                 'TestImages\\tire.tif',
                 'TestImages\\yellowlily.jpg']
    shapes = [(256, 256, 3),
              (512, 512, 3),
              (246, 300, 3),
              (2336, 3504, 3),
              (2348, 3522, 3),
              (256, 320, 3),
              (220, 220, 3),
              # (256, 256),
              # (512, 512),
              # (246, 300),
              # (2336, 3504, 3),
              # (2348, 3522),
              # (256, 320, 3),
              # (220, 220, 3),
              # (205, 232),
              # (1632, 1224, 3),
              (205, 232, 3),
              (1632, 1224, 3)]

    # Load test images
    ims = load_image_series(filenames)

    # Check the length of the ims list
    assert len(ims) == len(shapes)

    # Check the images sizes
    for z in range(len(ims)):

        assert ims[z].shape == shapes[z]
