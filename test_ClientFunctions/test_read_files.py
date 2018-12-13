import pytest
from ClientFunctions.read_files import *


@pytest.mark.parametrize("file, shape", [
    ('TestImages/Lenna.png', (220, 220)),
    ('TestImages/coins.png', (246, 300))
])
def test_load_image(file, shape):

    im = load_image(file)

    assert im[0].size == (shape[1], shape[0])


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
                  (2336, 3504),
                  (2348, 3522),
                  (256, 320),
                  (220, 220),
                  (205, 232),
                  (1632, 1224)]
    names = ['circles.png',
             'circlesBrightDark.png',
             'coins.png', 'foosball.jpg',
             'foosballraw.tiff',
             'football.jpg',
             'Lenna.png',
             'tire.tif',
             'yellowlily.jpg'
             ]

    # Test function
    ims, all_filenames = load_zipped_image(filename)

    # Assert that the correct number of images were found
    assert len(ims) == len(file_sizes)

    # Assert that the images shapes are correct
    for i in range(len(ims)):
        assert ims[i].size == (file_sizes[i][1], file_sizes[i][0])

    for i in range(len(all_filenames)):

        assert all_filenames[i] == names[i]


@pytest.mark.parametrize("lists, answer", [
    ([[1], [2, 3], [3, 4, 5]], [1, 2, 3, 3, 4, 5]),
    ([['png'], ['jpg', 'tif']], ['png', 'jpg', 'tif'])
])
def test_flatten(lists, answer):

    files = flatten(lists)

    assert files == answer


def test_load_image_series():

    # Set up test cases using TestImages
    filenames = ['TestImages/circles.png',
                 'TestImages/circlesBrightDark.png',
                 'TestImages/coins.png',
                 'TestImages/foosball.jpg',
                 'TestImages/foosballraw.tiff',
                 'TestImages/football.jpg',
                 'TestImages/Lenna.png',
                 'TestImages/TestImages.zip',
                 'TestImages/tire.tif',
                 'TestImages/yellowlily.jpg']
    shapes = [(256, 256),
              (512, 512),
              (246, 300),
              (2336, 3504),
              (2348, 3522),
              (256, 320),
              (220, 220),
              (256, 256),
              (512, 512),
              (246, 300),
              (2336, 3504),
              (2348, 3522),
              (256, 320),
              (220, 220),
              (205, 232),
              (1632, 1224),
              (205, 232),
              (1632, 1224)]

    # Load test images
    ims, all_filenames = load_image_series(filenames)

    # Check the length of the ims list
    assert len(ims) == len(shapes)

    # Check the images sizes
    for z in range(len(ims)):

        assert ims[z].size == (shapes[z][1], shapes[z][0])
