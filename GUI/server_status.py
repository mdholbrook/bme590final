from time import sleep
import requests
from PyQt5.QtCore import QThread, pyqtSignal


class SeverStatus(QThread):
    """
    Runs a separate thread which pings the server for status updates
    """
    def __init__(self):

        self.status = False
        self.ip = 'http://127.0.0.1:5000/status'  # UPDATE ADDRESS

    def run(self):

        requests.post(self.ip,
                      json='')
