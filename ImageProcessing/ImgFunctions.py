import numpy as np
from skimage import util, exposure, io

from matplotlib import pyplot as plt


def view_histogram_bw(image):
    """
    Args: View the histogram of a black and white image
        image: Float array of the image
    Returns: Hist and its bin array
    """
    hist, bins = np.histogram(image.ravel(), 256, [0, 256])
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()
    return hist, bins


def view_color_histogram(image):
    """
    Args: View the histogram of a color image
        image: Float array of the image
    Returns: Hist and its bin array
    """
    hist_all = []
    for i in range(image.shape[2]):
        hist, bins = np.histogram(image[:, :, i].ravel(), 256, [0, 256])
        hist_all.append(hist)
        # plt.hist(image.ravel(), 256, [0, 256])
        # plt.show()
    return hist_all, bins


def contrast_stretching(image):
    """
    Args: Contrast stretching (often called normalization) is a simple image
    enhancement technique that attempts to improve the contrast in an image
    by `stretching' the range of intensity values it contains to span a
    desired range of values
        image:float array for the image
    Returns: Contrast adjusted version of the image
    """
    p2, p98 = np.percentile(image, (2, 98))
    img_rescale = exposure.rescale_intensity(image, in_range=(p2, p98))
    return img_rescale


def log_compression(image):
    """
    Args:The logarithmic operator is a simple point processor where the mapping
    function is a logarithmic curve.In other words, each pixel value is
    replaced with its logarithm. Most implementations take either the natural
    logarithm or the base 10 logarithm. However, the basis does not influence
    the shape of the logarithmic curve, only the scale of the output values
    which are scaled for display on an 8-bit system. Hence, the basis does not
    influence the degree of compression of the dynamic range.
        image: float array for the image
    Returns: Log compressed version of the image
    """
    logarithmic_corrected = exposure.adjust_log(image, 1)
    return logarithmic_corrected


def reverse_video(image):
    """
    Args: Invert the image, Minimum to Maximum intensity on each pixel of the
    image
        image: float array for the image
    Returns: reverse/invert version of the image
    """
    inverted_img = util.invert(image)
    return inverted_img


def gamma_correction(image):
    """
    Args:Gamma correction, or often simply gamma, is a nonlinear operation used
     to encode and decode luminance or tristimulus values in video or still
     image systems. Gamma correction is, in the simplest cases, defined by the
     power-law expression.
        image: float array for the image
    Returns: gamma corrected version of the image
    """
    gamma_corrected = exposure.adjust_gamma(image, 2)
    return gamma_corrected


if __name__ == '__main__':
    filename = "../TestImages/Lenna.png"
    img = io.imread(filename)
    his = view_histogram_bw(img)
    his2 = view_color_histogram(img)
    img2 = reverse_video(img)
    plt.imshow(img2)
    plt.show()
