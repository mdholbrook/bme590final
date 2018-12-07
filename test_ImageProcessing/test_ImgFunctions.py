import pytest
from ImageProcessing.ImgFunctions import *
from skimage import io
from skimage.color import rgb2gray


def test_histogram_eq():
    filename = "test_ImageProcessing/Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = histogram_eq(img)
    assert test.size == img.size


def test_contrast_stretching():
    filename = "test_ImageProcessing/Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = contrast_stretching(img)
    assert test.size == img.size


def test_log_compression():
    filename = "test_ImageProcessing/Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = log_compression(img)
    assert test.size == img.size


def test_reverse_video():
    filename = "test_ImageProcessing/Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = reverse_video(img)
    assert test.size == img.size


def test_gamma_correction():
    filename = "test_ImageProcessing/Lenna.png"
    img = io.imread(filename)
    img = rgb2gray(img)
    test = gamma_correction(img)
    assert test.size == img.size
