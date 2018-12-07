import sys
from PyQt5 import QtWidgets
from GUI.main_window import MainWindow


if __name__ == "__main__":
    # Execute local front end client
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
