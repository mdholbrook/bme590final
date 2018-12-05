from skimage import data
from skimage.viewer import ImageViewer
import numpy as np


def view_images(df):
    """Call image display functions to show original, processed, or both images

    Args:
        df (dict): dictionary containing images and display instructions

    Returns:

    """

    # Get image to show
    im = separate_ims(df)

    # Display images
    show_ims(im)


def show_ims(im):
    """Function which uses skimage viewer to display the desired image(s).
    The window cretaed by this function needs be closed before the GUI can
    continue.

    Args:
        im (numpy array): a 2D numpy array (or 3D with channels)

    Returns:

    """

    # Generate image viewer
    viewer = ImageViewer(im, useblit=False)

    # Show image
    viewer.show()


def separate_ims(df):
    """Creates an image which is to be send to a viewer function. For
    cases in which both the original and processed images are to be
    shwon this function creates a horizontally concatenated image.

    Args:
        df (dict): dictionary containing images and display instructions

    Returns:
        numpy array: a 2D or 3D numpy array (includes channels) containing
        the image to be shown
    """

    # TODO: upate image index based on which index is selected
    ind = 0

    if df['show1'] and df['show2']:
        im = np.concatenate((df['orig_im'][ind], df['proc_im'][ind]), axis=1)

    elif df['show1']:
        im = df['orig_im'][ind]
    elif df['show2']:
        im = df['proc_im'][ind]

    return im


if __name__ == "__main__":

    # Load sample image
    im1 = data.coffee()
    im1 = np.asarray(im1, dtype="int32")
    im2 = im1.copy()

    # Set up sample dict
    df = {}
    df['orig_im'] = [im1]
    df['proc_im'] = [im2]

    df['show1'] = True
    df['show2'] = True

    # Show images
    im = separate_ims(df)
    show_ims(im)
