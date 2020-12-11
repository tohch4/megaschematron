import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from config.constants import APP_NAME, APP_VERSION

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        label = QLabel("Main window")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
