from skimage import data
from skimage.viewer import ImageViewer
import numpy as np


def show_ims(im):

    viewer = ImageViewer(im)
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

    ind = 0

    if df['show1'] and df['show2']:
        im = np.concatenate((df['orig_im'][ind], df['proc_im'][ind]), axis=1)

    elif df['show1']:
        im = df['orig_im'][ind]
    elif df['show2']:
        im = df['proc_im'][ind]

    return im


if __name__ == "__main__":

    from PIL import Image
    import numpy as np

    im1 = Image.open('../peppers.jpg')
    im1.load()
    im1 = np.asarray(im1, dtype="int32")
    im2 = im1.copy()

    df = {}
    df['orig_im'] = [im1]
    df['proc_im'] = [im2]

    df['show1'] = True
    df['show2'] = True

    im = separate_ims(df)
    show_ims(im)
