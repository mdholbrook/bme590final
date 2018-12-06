from processing import *
from skimage.color import rgb2gray
from skimage import util, io, exposure
from matplotlib import pyplot as plt

filename = "Lenna.png"
img = io.imread(filename)
img = rgb2gray(img)

def test_histogram_eq(img):



def test_contrast_stretching(img):


def test_log_compression(img):


def test_reverse_video(img):


def gamma_correction(img):