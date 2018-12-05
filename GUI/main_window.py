import sys
from GUI.validation_functions import valid_email
from PyQt5 import QtWidgets
from GUI.main_window_design import Ui_MainWindow
from GUI.files_dialog import LoadDialog, SaveDialog


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        # Set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up self fields
        self.save_dialog = ''
        self.load_dialog = ''

        # Set up email field
        # self.ui.lineEditEmail.text()

        # Callbacks for button presses
        self.ui.pushButtonApply.clicked.connect(self.apply_clicked)
        self.ui.pushButtonDonwload.clicked.connect(self.download_clicked)
        self.ui.toolButtonLoad.clicked.connect(self.load_image_dialog)
        self.ui.pushButtonEmail.clicked.connect(self.validate_email)

        # Gray out options before loading a file
        self.process_flag = False
        self.save_flag = False
        self.load_flag = False
        self.disable_options()

        # Initialize dictionary for saving user inputs
        self.df = {}

    def validate_email(self):
        """Determines that the input email address is valid (eg. is of the
        format '*@*.*')

        Returns:

        """

        # Get input email address from image path
        email = self.ui.lineEditEmail.text()

        # Validate the emaail address
        if valid_email(email):

            # Add email to the dictionary
            self.df['email'] = self.ui.lineEditEmail.text()
            print(self.df)

            # Update disabled options
            self.load_flag = True

        else:

            # Show error message
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage("Please enter a valid email address")

            self.load_flag = False

        self.disable_options()

    def disable_options(self):
        """This function prohibits a user from trying to access GUI commands
        before they are ready. For example, an image cannot be processed
        before a valid email has been entered or a file has been loaded.

        Returns:

        """

        # Disable loading images if there is not valid email address
        self.ui.toolButtonLoad.setEnabled(self.load_flag)

        # Disable Apply push button if no image is loaded
        self.ui.pushButtonApply.setEnabled(self.process_flag)

        # Disable Download push button if no image is loaded
        self.ui.pushButtonDonwload.setEnabled(self.save_flag)

    def load_image_dialog(self):
        """Calls files_dialog to create a window explorer in which a single
        or multiple files may be selected.

        Returns:

        """

        # Launch the load image dialog
        self.load_dialog = LoadDialog(self)
        self.df['load_filenames'] = self.load_dialog.files
        print(self.df)

        # Close dialog box
        self.load_dialog.close()

        # Update image path shown in GUI
        self.ui.lineEditLoad.setText(self.df['load_filenames'][0])

        # Allow the loaded image to be processed
        # TODO: add a check that the image exists
        self.process_flag = True
        self.disable_options()

    def apply_clicked(self):
        """The "Apply Processing" button was clicked

        Returns:

        """

        # Load files
        # TODO: add a function to read images

        # Get processing settings
        self.df['hist'] = self.ui.radioButtonHist.isChecked()
        self.df['cont'] = self.ui.radioButtonContrast.isChecked()
        self.df['log'] = self.ui.radioButtonLog.isChecked()
        self.df['rev'] = self.ui.radioButtonReverse.isChecked()
        self.df['median'] = self.ui.radioButtonMedian.isChecked()

        print(self.df)

        # Allow image saving
        self.save_flag = True
        self.disable_options()

        # TODO: Add call to communictation function

    def download_clicked(self):
        """The "Download" button was clicked

        This function grabs the selected GUI options and calls a function to
        save the processed images.

        Returns:

        """
        # TODO: add a check that the images have been processed
        # TODO: get processed image(s)

        # Get save settings
        self.df['JPEG'] = self.ui.radioButtonJPEG.isChecked()
        self.df['PNG'] = self.ui.radioButtonPNG.isChecked()
        self.df['TIFF'] = self.ui.radioButtonTIFF.isChecked()

        print(self.df)

        # Launch the save image dialog box
        self.save_dialog = SaveDialog(self, df=self.df)
        self.df['save_filename'] = self.save_dialog.filename
        print(self.df)

        # Close dialog box
        self.save_dialog.close()

        # TODO: Add call to to write the images 


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
