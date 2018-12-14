import pytest
from ImageProcessing.ImgFunctions import *
from skimage import io


@pytest.mark.parametrize("filename,expected", [
    ("TestImages/Lenna.png", 2),
    ("TestImages/circlesBrightDark.png", 2),
    ("TestImages/yellowlily.jpg", 2),
    ("TestImages/tire.tif", 2),
    ("TestImages/coins.png", 2),
    ("TestImages/foosball.jpg", 2),
])
def test_histogram_eq(filename, expected):
    img = io.imread(filename)
    test = histogram_eq(img)
    assert test.shape[0] == img.shape[0]
    assert test.shape[1] == img.shape[1]


@pytest.mark.parametrize("filename,expected", [
    ("TestImages/Lenna.png", 2),
    ("TestImages/circlesBrightDark.png", 2),
    ("TestImages/yellowlily.jpg", 2),
    ("TestImages/tire.tif", 2),
    ("TestImages/coins.png", 2),
])
def test_contrast_stretching(filename, expected):
    img = io.imread(filename)
    test = contrast_stretching(img)
    assert test.shape[0] == img.shape[0]
    assert test.shape[1] == img.shape[1]


@pytest.mark.parametrize("filename,expected", [
    ("TestImages/Lenna.png", 2),
    ("TestImages/circlesBrightDark.png", 2),
    ("TestImages/yellowlily.jpg", 2),
    ("TestImages/tire.tif", 2),
    ("TestImages/coins.png", 2),
])
def test_log_compression(filename, expected):
    img = io.imread(filename)
    test = log_compression(img)
    assert test.shape[0] == img.shape[0]
    assert test.shape[1] == img.shape[1]


@pytest.mark.parametrize("filename,expected", [
    ("TestImages/Lenna.png", 2),
    ("TestImages/circlesBrightDark.png", 2),
    ("TestImages/yellowlily.jpg", 2),
    ("TestImages/tire.tif", 2),
    ("TestImages/coins.png", 2),
    ("TestImages/foosball.jpg", 2),
])
def test_reverse_video(filename, expected):

    img = io.imread(filename)
    test = reverse_video(img)
    assert test.shape[0] == img.shape[0]
    assert test.shape[1] == img.shape[1]


@pytest.mark.parametrize("filename,expected", [
    ("TestImages/Lenna.png", 2),
    ("TestImages/circlesBrightDark.png", 2),
    ("TestImages/yellowlily.jpg", 2),
    ("TestImages/tire.tif", 2),
    ("TestImages/coins.png", 2),
    ("TestImages/foosball.jpg", 2),
])
def test_gamma_correction(filename, expected):
    img = io.imread(filename)
    test = gamma_correction(img)
    assert test.shape[0] == img.shape[0]
    assert test.shape[1] == img.shape[1]
