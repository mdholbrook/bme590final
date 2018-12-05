from skimage import data
from skimage.viewer import ImageViewer
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


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


def show_hist(df):
    """Plot histograms of the shown images.

    Histogram values were calculated on the server. They are only plotted here.

    Args:
        df (dict): dictionary containing calculated histograms and display
            metadata

    Returns:

    """
    # Get colors to use for grayscale or RGB images
    num_chans = get_num_channels(df)
    colors, color_names = hist_colors(num_chans)

    # Get image index
    ind = 0

    # Loop over image channels
    for c in range(len(colors)):

        # If both images are shown
        if df['show1'] and df['show2']:

            if c == 0:
                fig, ax = plt.subplots(len(colors), 2)

            # Plot original image
            ax[c][0].bar(df['histDataOrig'][ind][0],
                         df['histDataOrig'][ind][1][c], color=colors[c])

            ax[c][0].set_xlabel('Image Values')
            ax[c][0].set_ylabel('Counts')
            ttl = 'Original Image - ' + color_names[c]
            ax[c][0].set_title(ttl)

            # Plot processed image
            ax[c][1].bar(df['histDataProc'][ind][0],
                         df['histDataProc'][ind][1][c], color=colors[c])

            ax[c][1].set_xlabel('Image Values')
            ax[c][1].set_ylabel('Counts')
            ttl = 'Processed Image - ' + color_names[c]
            ax[c][1].set_title(ttl)

        # If we only want the original image
        elif df['show1']:

            if c == 0:
                fig, ax = plt.subplots(1, len(colors))

            # Allow BW images to be indexed
            if len(ax) == 1:
                ax = [ax]

            # Plot original image
            ax[c].bar(df['histDataOrig'][ind][0],
                   df['histDataOrig'][ind][1][c], color=colors[c])

            ax[c].set_xlabel('Image Values')
            ax[c].set_ylabel('Counts')
            ttl = 'Processed Image - ' + color_names[c]
            ax[c].set_title(ttl)

        # If we only want the processed image
        elif df['show2']:

            if c == 0:
                fig, ax = plt.subplots(1, len(colors))

            # Allow BW images to be indexed
            if len(ax) == 1:
                ax = [ax]

            # Plot processed image
            ax[c].bar(df['histDataProc'][ind][0],
                   df['histDataProc'][ind][1][c], color=colors[c])

            ax[c].set_xlabel('Image Values')
            ax.set_ylabel('Counts')
            ax.set_title('Processed Image')

    plt.show()


def get_num_channels(df):
    """Get the number of image channels of the input image.

    We make the assumption that the number of channels will not be different
    for the processed image

    Args:
        df (dict): dictionary containing original images

    Returns:
        int: the number of channels in the image
    """

    im = df['orig_im'][0].shape
    num_chans = im[2]

    return num_chans


def hist_colors(num_chans):
    """This function returns a list of colors to be used for histogram
    plotting based on whether the image is grayscale or RGB.

    Args:
        num_chans (int): the number of channels contained

    Returns:
        list: colors, a list of colors of len=1 or len=3
        list: color_names, names of the colors, will be used for labeling
    """
    if num_chans == 1:
        colors = ['k']
        color_names = ['BW']

    if num_chans == 3:
        colors = ['r', 'g', 'b']
        color_names = ['Red', 'Green', 'Blue']

    return colors, color_names


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

    # Set up histograms
    df['histDataOrig'] = [[[0, 1, 2, 3, 4, 5, 6],
                          [[1, 1, 4, 9, 8, 4, 3],
                           [1, 0, 3, 10, 7, 5, 2],
                           [1, 2, 5, 2, 3, 4, 5]]]]
    df['histDataProc'] = [[[0, 1, 2, 3, 4, 5, 6],
                          [[1, 1, 4, 9, 8, 4, 3],
                          [1, 0, 3, 10, 7, 5, 2],
                          [1, 2, 5, 2, 3, 4, 5]]]]

    # Show images
    im = separate_ims(df)
    show_hist(df)
    show_ims(im)
