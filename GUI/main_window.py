import sys
import os
from time import sleep
from GUI.validation_functions import valid_email, validate_file_exists
from PyQt5 import QtWidgets
from GUI.main_window_design import Ui_MainWindow
from GUI.files_dialog import LoadDialog, SaveDialog
from GUI.view_images import run_image_viewer
from ClientFunctions.read_files import load_image_series_bytes
from ClientFunctions.read_files import load_image_series
from ClientFunctions.write_files import save_images
from ClientFunctions.communication import send_to_server
from GUI.utils import save_email, load_email


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        # Set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up self fields
        self.save_dialog = ''
        self.load_dialog = ''
        self.filenames = ''

        # Callback for changing image selection via the ComboBox
        self.ui.comboBox.activated.connect(self.pullcombotext)

        # Callback for changing image view buttons
        self.ui.radioButtonShowBoth.toggled.connect(self.pullcombotext)
        self.ui.radioButtonShowOriginal.toggled.connect(self.pullcombotext)
        self.ui.radioButtonShowProcessed.toggled.connect(self.pullcombotext)

        # Callbacks for button presses
        self.ui.pushButtonApply.clicked.connect(self.apply_clicked)
        self.ui.pushButtonDonwload.clicked.connect(self.download_clicked)
        self.ui.toolButtonLoad.clicked.connect(self.load_image_dialog)
        self.ui.pushButtonEmail.clicked.connect(self.validate_email)
        self.ui.pushButtonImageViewer.clicked.connect(self.image_viewer)

        # Gray out options before loading a file
        self.process_flag = False       # Allow processing
        self.viewer_flag = False        # Allower viewer
        self.view_pros_flag = False     # Allow viewer to show processed ims
        self.save_flag = False          # Allow saving images
        self.load_flag = False          # Allow loading images
        self.disable_options()

        # Initialize dictionary for saving user inputs
        self.df = {}
        self.df['show1'] = False
        self.df['show2'] = False

        # Load previous data
        self.preload_email()

    def preload_email(self):
        """If a previous email has been used, upload it to the GUI and allow
        the user to access more options.

        Returns:

        """

        email = load_email()
        if email:
            # Update dictionary
            self.df['email'] = email

            # Update GUI field
            self.ui.lineEditEmail.setText(email)

            # Allow the user to access other options
            self.load_flag = True

            self.disable_options()

    def validate_email(self):
        """Determines that the input email address is valid (eg. is of the
        format '*@*.*')

        Returns:

        """

        # Get input email address from image path
        email = self.ui.lineEditEmail.text()

        # Validate the email address
        if valid_email(email):

            # Add email to the dictionary
            self.df['email'] = self.ui.lineEditEmail.text()

            # Update disabled options
            self.load_flag = True

            # Save valid email for future use
            save_email(self.df['email'])

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

        # Disable viewing image if images are not loaded, do not exist
        self.ui.pushButtonImageViewer.setEnabled(self.viewer_flag)

        # Disable showing histograms or processed image if not processed
        self.ui.checkBoxShowHist.setEnabled(self.view_pros_flag)
        self.ui.radioButtonShowProcessed.setEnabled(self.view_pros_flag)
        self.ui.radioButtonShowBoth.setEnabled(self.view_pros_flag)

        # Disable Download push button if no image is loaded
        self.ui.pushButtonDonwload.setEnabled(self.save_flag)

    def load_image_dialog(self):
        """Calls files_dialog to create a window explorer in which a single
        or multiple files may be selected.

        Returns:

        """
        # Define a default position for the image selected
        self.df['imageInd'] = 0

        # Launch the load image dialog
        self.load_dialog = LoadDialog(self)
        self.df['load_filenames'] = self.load_dialog.files

        # Close dialog box
        self.load_dialog.close()

        # Update image path shown in GUI
        self.ui.lineEditLoad.setText(self.df['load_filenames'][0])

        # Check that the images exist
        if validate_file_exists(self.df['load_filenames']):

            # Load the images
            self.df['orig_im'], self.df['orig_im_names'] = \
                load_image_series_bytes(self.df['load_filenames'])

            # Add images to combobox to allow for viewing
            self.filenames = [os.path.basename(i) for i in self.df[
                'orig_im_names']]
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(self.filenames)
            self.ui.comboBox.setCurrentIndex(0)

            # Enable process flag
            self.process_flag = True
            self.viewer_flag = True

        else:
            # Show error message
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage("Please enter valid image files")

            self.process_flag = False
            self.viewer_flag = False

        self.disable_options()

    def apply_clicked(self):
        """The "Apply Processing" button was clicked

        Returns:

        """

        # Get processing settings
        self.df['hist'] = self.ui.radioButtonHist.isChecked()
        self.df['cont'] = self.ui.radioButtonContrast.isChecked()
        self.df['log'] = self.ui.radioButtonLog.isChecked()
        self.df['rev'] = self.ui.radioButtonReverse.isChecked()
        self.df['gamma'] = self.ui.radioButtonGamma.isChecked()

        # Allow image saving
        self.save_flag = True
        self.disable_options()

        # Send data to server
        json_dict = send_to_server(self.df)

        # Error handling
        if type(json_dict) == str:
            # self.ui.listWidgetStatus.clear()
            self.ui.listWidgetStatus.addItems([json_dict])

        else:
            self.df['proc_im'] = json_dict["proc_im"]
            self.df['histDataOrig'] = json_dict["histDataOrig"]
            self.df['histDataProc'] = json_dict["histDataProc"]
            self.df['im_dims'] = json_dict["image_sizes"]
            self.df["processing_time"] = json_dict["latency"]
            self.df["timestamp"] = json_dict["upload_timestamp"]

            # TODO: Add a check to see if the processing is complete
            self.view_pros_flag = True

            # Update status
            self.ui.listWidgetStatus.addItem('Done!')

        self.disable_options()

    def image_viewer(self):

        # Load original images
        self.df['orig_im_array'], _ = load_image_series(self.df[
                                                           'load_filenames'])

        # Get viewer options
        if self.ui.radioButtonShowBoth.isChecked():

            # Show both images
            self.df['show1'] = True
            self.df['show2'] = True

        else:
            # Show only one image
            self.df['show1'] = self.ui.radioButtonShowOriginal.isChecked()
            self.df['show2'] = self.ui.radioButtonShowProcessed.isChecked()

        # Get histomgram request
        self.df['showHist'] = self.ui.checkBoxShowHist.isChecked()

        # TODO: update status box with image info

        # Call image viewer
        run_image_viewer(self.df)

    def download_clicked(self):
        """The "Download" button was clicked

        This function grabs the selected GUI options and calls a function to
        save the processed images.

        Returns:

        """

        # Get save settings
        self.df['JPEG'] = self.ui.radioButtonJPEG.isChecked()
        self.df['PNG'] = self.ui.radioButtonPNG.isChecked()
        self.df['TIFF'] = self.ui.radioButtonTIFF.isChecked()

        # Launch the save image dialog box
        self.save_dialog = SaveDialog(self, df=self.df)
        self.df['save_filename'] = self.save_dialog.filename

        # Close dialog box
        self.save_dialog.close()

        # Write images
        save_images(self.df)

    def pullcombotext(self, ind):

        # Get droptext index
        if type(ind) == bool:
            ind = 0

        self.df['imageInd'] = ind

        # Get radiobutton selection for which image to view
        self.df['show1'] = self.ui.radioButtonShowOriginal.isChecked()
        self.df['show2'] = self.ui.radioButtonShowProcessed.isChecked()

        if self.ui.radioButtonShowBoth.isChecked():
            self.df['show1'] = True
            self.df['show2'] = True

        # Update image metadata
        if self.df['show2']:

            data = ['Image name: ' + self.filenames[ind],
                    'Started processing: %s' % self.df['timestamp'],
                    'Batch processing time: ' + self.df['processing_time'],
                    'Image dimensions: [%d, %d]'
                    % (self.df['im_dims'][ind][0],
                       self.df['im_dims'][ind][1]),
                    '']

            # Update list box
            self.ui.listWidgetStatus.addItems(data)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
