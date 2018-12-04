import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float
from skimage import exposure

def histogram_eq(image):
    img_eq = exposure.equalize_hist(img)

def contrast_streching(img):
    p2, p98 = np.percentile(img, (2, 98))
    img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))

def log_compression():


def reverse_video():


def gamma_correction(img):
    gamma_corrected = exposure.adjust_gamma(img, 2)
    return gamma_corrected
