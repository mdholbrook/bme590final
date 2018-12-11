import pytest
import os
from ClientFunctions.write_files import *
from ClientFunctions.read_files import *


def clean_up(files):

    for file in files:
        os.remove(file)


def test_write_image():

    # Load test data
    infile = ['TestImages/circles.png']
    im, filenames = load_image_series(infile)

    # Set up image writing data
    outfile = 'ProcessedImages/circles_test.png'
    fileformat = 'PNG'
    write_image(outfile, im, fileformat)

    assert os.path.exists(outfile)

    clean_up([outfile])


def test_gen_save_filename():

    # Set up test case
    files = ['a.p', 'b.p', 'b.j', 'c.j', 'a.j']
    file_ext = '.m'

    # Set up answer
    expected = ['a.m', 'b.m', 'b_1.m', 'c.m', 'a_1.m']

    # Test function
    new_files = gen_save_filename(files, file_ext)

    assert new_files == expected


@pytest.mark.parametrize("candidate, fileformat, file_ext", [
    ({'PNG': True, 'JPEG': False, 'TIFF': False}, 'PNG', '.png'),
    ({'PNG': False, 'JPEG': True, 'TIFF': False}, 'JPEG', '.jpg'),
    ({'PNG': False, 'JPEG': False, 'TIFF': True}, 'TIFF', '.tif'),
])
def test_gen_file_extension(candidate, fileformat, file_ext):

    # Test the function
    fileform, file_ex = gen_file_extension(candidate)

    assert fileformat == fileform

    assert file_ext == file_ex


def tset_write_zip():

    # Load data
    infiles = ['TestImages/coins.png', 'TestImages/Lenna.png']
    ims, all_filenames = load_image_series(infiles)

    # Set up inputs
    outfile = 'ProcessedImages/zip_test.zip'
    files = ['coins.tif', 'Lenna.tif']
    fileformat = 'TIFF'
    write_zip(outfile, files, ims, fileformat)

    # Test output file
    assert os.path.exists(outfile)

    # Read image names
    zipnames = get_zip_names(outfile)

    assert zipnames == files

    clean_up(outfile)
