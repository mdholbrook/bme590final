import os
from PIL import Image
from zipfile import ZipFile, ZipInfo
from io import BytesIO


def write_image(filename, im, fileformat):
    """Writes a single images to file

    Args:
        filename (str): name and path of the file to be written
        im (numpy array): image data to be written

    Returns:

    """

    img = im[0]
    img.save(filename, fileformat)


def write_zip(files, ims, fileformat):
    """
    This function makes an in-memory zip file of image files.

    Args:
        filename (str): name of the zip file which will be saved to disk
        files (list of str): list of filenames generated for saving, one for
            each image to be saved
        ims (list of numpy array): a list of image data to be saved
        fileformat (str): file encoding method to be used. Valid values are
        "JPEG", "PNG", and "TIFF".

    Returns:
        BytesIO: an in-memory file containing zipped images.
    """

    # Set up in-memory file
    memory_file = BytesIO()

    # Make a zip file inside of the in-memory file
    zf = ZipFile(memory_file, mode='w')

    # For each image
    for i in range(len(files)):

        # Get a single image and create a PIL object
        im = ims[i]

        # Set up a temporary image buffer
        tmp = BytesIO()

        # Save image to a temporary buffer using an encoding defined by
        # fileformat
        im.save(tmp, fileformat)

        # Save image into the in-memory zip file
        zf.writestr(files[i], tmp.getvalue())

    # Close the in-memory zip file
    zf.close()

    return memory_file


def write_zip_disk(zip_file, filename):
    """
    Writes the contents of a zipfile to disk.
    Args:
        zip_file (BytesIO): an in-memory file containing a zip file as
            created by write_zip.

    Returns:

    """

    # Write zip file to disk as bytes encoding
    with open(filename, 'wb') as f:
        f.write(zip_file.getvalue())


def gen_save_filename(files, file_ext):
    """
    Generates a new filename for saving zipfile images based on the name
    naming convention as the original file
    Args:
        file (str): original image filename
        file_ext (str): extension to be used for saving the processed image

    Returns:
        str: a new filename which will be used in the saved zip file
    """

    new_names = []
    for file in files:

        # Split path to original filename with a new extension
        base = os.path.basename(file)
        new_name, _ = os.path.splitext(base)

        # Rename if filename already exists
        if new_name in new_names:
            new_name = new_name + '_1'

        # Append to list of new names
        new_names.append(new_name)

    # Append extension
    new_names = [i + file_ext for i in new_names]

    # Return filename with appended extension
    return new_names


def gen_file_extension(df):
    """Generates file extensions from the data structure

    Args:
        df (dict): dictionary which contains file format information

    Returns:
        tuple: save file format for PIL, and file extension
    """

    if df['JPEG']:
        fileformat = 'JPEG'
        file_ext = '.jpg'

    elif df['PNG']:
        fileformat = 'PNG'
        file_ext = '.png'

    elif df['TIFF']:
        fileformat = 'TIFF'
        file_ext = '.tif'

    return fileformat, file_ext


def save_images(df):
    """
    This function serves as the parent function for writing processed images
    to disk

    Args:
        df (dict): dictionary containing the processed images 'proc_im',
            original image filenames 'loaded_filenames'], the save file name
            'save_filename' and file extension information.

    Returns:

    """
    # Get save file extension and encoding
    fileformat, file_ext = gen_file_extension(df)

    # Determine if we save an image or zip file
    if len(df['loaded_filenames']) == 1:

        # Save a single image
        write_image(df['save_filename'], df['proc_im'], fileformat)

    else:

        # Generate image save names
        gen_save_filename(df['orig_im_names'], file_ext)

        # Save a zip file of images
        zip_file = write_zip(df['load_filenames'],
                             df['proc_im'], file_ext)
        write_zip_disk(zip_file, df['save_filename'])


if __name__ == "__main__":

    filename = '../ProcessedImages/zipfile.png'

    files = ['../TestImages/foosball.jpg', '../TestImages/coins.png']

    from ClientFunctions.read_files import load_image_series_bytes

    ims = load_image_series_bytes(files)

    files = ['foosball.jpg', 'coins.png']

    write_image(filename, ims[0])

    filename = '../ProcessedImages/zipfile.zip'

    write_zip(filename, files, ims)
