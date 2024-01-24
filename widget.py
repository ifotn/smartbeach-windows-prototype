# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton

from ui_form import *

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
