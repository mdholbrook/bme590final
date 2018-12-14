from skimage import data
from skimage.viewer import ImageViewer
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import seaborn as sns

sns.set_style('whitegrid')


def run_image_viewer(df):
    """This functions calls the functions in this script to dispaly images
    and histograms.

    Args:
        df (dict): dictionary passed from the GUI

    Returns:

    """
    # Get images to show
    im = separate_ims(df)

    # Plot image histograms
    if df['showHist']:
        show_hist(df)

    # Show images
    show_ims(im)

    plt.show()


def show_ims(im):
    """Function which uses skimage viewer to display the desired image(s).
    The window cretaed by this function needs be closed before the GUI can
    continue.

    Args:
        im (PIL object): a PIL image object

    Returns:

    """

    # Get an array to plot
    im_array = np.array(im)

    # Set up the figure
    fig, ax = plt.subplots()

    # Show the image
    if len(im_array.shape) == 2:
        plt.imshow(im_array, cmap='gray')

    else:
        plt.imshow(im_array)

    # Set the plot properties
    ax.grid(False)
    ax.axis('off')


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
    ind = df['imageInd']

    # Loop over image channels
    for c in range(len(colors)):

        # If both images are shown
        if df['show1'] and df['show2']:

            if c == 0:
                fig, ax = plt.subplots(len(colors), 2)

            # Allow BW images to be indexed
            if len(colors) == 1:
                ax = [ax]

            # Plot original image
            bins = [(i + j)/2 for i, j in zip(df['histDataOrig'][ind][0][1:],
                                              df['histDataOrig'][ind][0][
                                              :-1])]
            ax[c][0].plot(bins, df['histDataOrig'][ind][1][c], color=colors[c],
                          linewidth=2.0)

            ax[c][0].set_xlabel('Image Values')
            ax[c][0].set_ylabel('Counts')
            ttl = 'Original Image - ' + color_names[c]
            ax[c][0].set_title(ttl)

            # Plot processed image
            bins = [(i + j)/2 for i, j in zip(df['histDataProc'][ind][0][1:],
                                              df['histDataProc'][ind][0][
                                              :-1])]
            ax[c][1].plot(bins, df['histDataProc'][ind][1][c], color=colors[c],
                          linewidth=2.0)

            ax[c][1].set_xlabel('Image Values')
            ax[c][1].set_ylabel('Counts')
            ttl = 'Processed Image - ' + color_names[c]
            ax[c][1].set_title(ttl)

        # If we only want the original image
        elif df['show1']:

            if c == 0:
                fig, ax = plt.subplots(1, len(colors))

            # Allow BW images to be indexed
            if len(colors) == 1:
                ax = [ax]

            # Plot original image
            bins = [(i + j)/2 for i, j in zip(df['histDataOrig'][ind][0][1:],
                                              df['histDataOrig'][ind][0][
                                              :-1])]
            ax[c].plot(bins, df['histDataOrig'][ind][1][c], color=colors[c],
                       linewidth=2.0)

            ax[c].set_xlabel('Image Values')
            ax[c].set_ylabel('Counts')
            ttl = 'Processed Image - ' + color_names[c]
            ax[c].set_title(ttl)

        # If we only want the processed image
        elif df['show2']:

            if c == 0:
                fig, ax = plt.subplots(1, len(colors))

            # Allow BW images to be indexed
            if len(colors) == 1:
                ax = [ax]

            # Plot processed image
            bins = [(i + j)/2 for i, j in zip(df['histDataProc'][ind][0][1:],
                                              df['histDataProc'][ind][0][
                                              :-1])]
            ax[c].plot(bins, df['histDataProc'][ind][1][c], color=colors[c],
                       linewidth=2.0)

            ax[c].set_xlabel('Image Values')
            ax[c].set_ylabel('Counts')
            ax[c].set_title('Processed Image')


def get_num_channels(df):
    """Get the number of image channels of the input image.

    We make the assumption that the number of channels will not be different
    for the processed image

    Args:
        df (dict): dictionary containing original images

    Returns:
        int: the number of channels in the image
    """
    ind = df['imageInd']
    im_bands = df['orig_im_array'][ind].getbands()

    # Assigne the number of channels based on image type
    num_chans = len(im_bands)

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

    # Use image selected in the GUI
    ind = df['imageInd']

    if df['show1'] and df['show2']:
        im = concatenate_ims([df['orig_im_array'][ind], df['proc_im'][ind]])

    elif df['show1']:
        im = df['orig_im_array'][ind]
    elif df['show2']:
        im = df['proc_im'][ind]

    return im


def concatenate_ims(ims):
    """Concatenates PIL original and processed images to a single image

    Args:
        ims (list): list of PIL image objects, [original, processed]

    Returns:
        PIL obj: a single, concatenated image
    """

    num_ims = len(ims)

    # Get image dimensions
    widths, heights = zip(*(i.size for i in ims))

    total_width = sum(widths)
    total_height = max(heights)

    # Make new concatenated image
    new_im = Image.new(mode=ims[0].mode, size=(total_width, total_height))

    x_offset = 0
    for im in ims:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    return new_im


if __name__ == "__main__":

    # Load sample image
    im1 = Image.fromarray(data.coffee())
    im2 = im1.copy()

    # Set up sample dict
    df = dict()
    df['orig_im_array'] = [im1]
    df['proc_im'] = [im2]

    df['show1'] = True
    df['show2'] = True

    df['imageInd'] = 0
    df['showHist'] = True

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
    run_image_viewer(df)
