from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog
import h5py
#import numpy as np
from pathlib import Path
#from PyQt5.QtCore import pyqtSignal


class OpenFileDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Open camera files:'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
     #   self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
       # self.openFileNameDialog()
        #self.show()


    def openFileNameDialog(self):
        self.initUI()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open camera files:", "D:\E6",
                                                   "Camera Files (*.h5)", options=options)
        if file_name:
            print(file_name)
        file_path = Path(file_name)
        h5 = h5py.File(file_path, 'r')

        return h5
        #self.open_inquiry_signal.emit()

