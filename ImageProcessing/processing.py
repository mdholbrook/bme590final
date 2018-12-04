import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float
from skimage import exposure
from skimage import util


def histogram_eq(image):
    img_eq = exposure.equalize_hist(image)
    return img_eq


def contrast_stretching(img):
    p2, p98 = np.percentile(img, (2, 98))
    img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))
    return img_rescale


def log_compression(image):
    logarithmic_corrected = exposure.adjust_log(image, 1)
    return logarithmic_corrected


def reverse_video(image):
    inverted_img = util.invert(image)
    return inverted_img


def gamma_correction(img):
    gamma_corrected = exposure.adjust_gamma(img, 2)
    return gamma_corrected
