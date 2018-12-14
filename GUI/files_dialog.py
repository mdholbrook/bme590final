import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog


class LoadDialog(QWidget):

    def __init__(self, parent=None):
        super(LoadDialog, self).__init__(parent)
        self.title = 'Select images to load'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.files = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Load filenames
        self.open_file_names_dialog()

        self.show()

        return self.files

    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = \
            QFileDialog.getOpenFileNames(
                self, "Open Image Files", "TestImages/",
                "Image Files (*.jpg *.png *.tif *.zip);;JPEG (*.jpg);;"
                "PNG (*.png);;TIFF (*.tif);;Zip files (*.zip);;All Files (*)",
                options=options)
        # if files:
        #     print(files)

        self.files = files


class SaveDialog(QWidget):

    def __init__(self, parent=None, df={}):
        super(SaveDialog, self).__init__(parent)
        self.df = df

        # Initialize self
        self.default_path = ''
        self.filename = ''
        self.fileformat = ''
        self.new_file = ''

        # Make default filename
        self.default_savepath()
        self.default_saveformat()
        self.default_savefile()

        self.title = 'Select file to save'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.filename = ''
        self.initUI()

    def default_saveformat(self):
        """Creates a default save format
        Zip files are the default for multiple images. Otherwise the user's
        input filetype is selected.

        Returns:

        """
        if len(self.df['orig_im_names']) > 1:
            self.fileformat = 'Zip (*.zip)'

        elif self.df['JPEG']:
            self.fileformat = 'JPEG (*.jpg)'

        elif self.df['PNG']:
            self.fileformat = 'PNG (*.png)'

        elif self.df['TIFF']:
            self.fileformat = 'TIFF (*.tif)'

    def default_savefile(self):

        [_, file_ext] = os.path.split(self.df['load_filenames'][0])
        [file, _] = os.path.splitext(file_ext)
        self.new_file = self.default_path + file + self.fileformat[-5:-1]

    def default_savepath(self):
        """Creates a directory inside the project for saving processed images

        Returns:

        """
        # Set up default save directory
        self.default_path = 'ProcessedImages/'

        # The directory does not already exist, create it
        if not os.path.exists(self.default_path):
            os.mkdir(self.default_path)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Save filename
        self.open_file_dialog()

        self.show()

    def open_file_dialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = \
            QFileDialog.getSaveFileName(
                self, "Save Processed Image Files", self.new_file,
                self.fileformat,
                options=options)
        # if fileName:
        #     print(fileName)

        self.filename = fileName


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadDialog()
    sys.exit(app.exec_())
