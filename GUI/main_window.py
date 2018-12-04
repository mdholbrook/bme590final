import sys
from PyQt5 import QtWidgets
from GUI.main_window_design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        # Set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Callbacks for putton presses
        self.ui.pushButtonApply.clicked.connect(self.apply_clicked)
        self.ui.pushButtonDonwload.clicked.connect(self.download_clicked)

        # Set up program dictionary
        self.df = {}

    def apply_clicked(self):
        """The "Apply Processing" button was clicked

        Returns:

        """

        # Load files and process

        # Get processing settings
        self.df['hist'] = self.ui.radioButtonHist.isChecked()
        self.df['cont'] = self.ui.radioButtonContrast.isChecked()
        self.df['log'] = self.ui.radioButtonLog.isChecked()
        self.df['rev'] = self.ui.radioButtonReverse.isChecked()
        self.df['median'] = self.ui.radioButtonMedian.isChecked()

        print(self.df)

        # TODO: Add call to communictation function

    def download_clicked(self):
        """The "Download" button was clicked

        Returns:

        """

        # Get save settings
        self.df['JPEG'] = self.ui.radioButtonJPEG.isChecked()
        self.df['PNG'] = self.ui.radioButtonPNG.isChecked()
        self.df['TIFF'] = self.ui.radioButtonTIFF.isChecked()

        print(self.df)

        # TODO: Add call to communictation function


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())