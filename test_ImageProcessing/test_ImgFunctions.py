import pytest
from ImageProcessing.ImgFunctions import *
from skimage import io
from skimage.color import rgb2gray


def test_histogram_eq():
    filename = "Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = histogram_eq(img)
    assert test.size == img.size


def test_contrast_stretching():
    filename = "Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = histogram_eq(img)
    assert test.size == img.size

