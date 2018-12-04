import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon


class LoadDialog(QWidget):

    def __init__(self, parent=None):
        super(LoadDialog, self).__init__(parent)
        self.title = 'Select images to load'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
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
                self, "QFileDialog.getOpenFileNames()", "",
                "Image Files (*.jpg, *.png, *.tif, *.zip);;JPEG (*.jpg);;"
                "PNG (*.png);;TIFF (*.tif);;Zip files (*.zip);;All Files (*)",
                options=options)
        if files:
            print(files)

        self.files = files


class SaveDialog(QWidget):

    def __init__(self, parent=None, df={}):
        super(SaveDialog, self).__init__(parent)
        self.df = df

        # Make default filename
        self.default_saveformat()
        self.default_savefile()

        self.title = 'Select file to save'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def default_saveformat(self):
        """Creates a default save format
        Zip files are the default for multiple images. Otherwise the user's
        input filetype is selected.

        Returns:

        """
        if len(self.df['load_filenames']) > 1:
            self.fileformat = 'Zip (*.zip)'

        elif self.df['JPEG']:
            self.fileformat = 'JPEG (*.jpg)'

        elif self.df['PNG']:
            self.fileformat = 'PNG (*.png)'

        elif self.df['TIFF']:
            self.fileformat = 'TIFF (*.tif)'

    def default_savefile(self):

        [file, _] = os.path.splitext(self.df['load_filenames'][0])
        self.new_file = file + '_processed' + self.fileformat[-5:-1]

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
                self, "QFileDialog.getSaveFileName()", self.new_file,
                self.fileformat,
                options=options)
        if fileName:
            print(fileName)

        self.filename = fileName


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadDialog()
    sys.exit(app.exec_())
