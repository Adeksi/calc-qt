from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from mainui import Ui_MainWindow

import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.actionQuit.triggered.connect(self.quit_app)
        self.btn

    """
    Logic
    """
    # def

    """
    """

    """
    Other things
    """

    def quit_app(self):
        app.quit()


if __name__ == "__main__":
    print("Okk")
    app = QApplication([])
    app.setApplicationName("Calc")
    # app.setStyle("Fusion")

    # # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, Qt.white)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, Qt.black)
    # app.setPalette(palette)
    # app.setStyleSheet(
    #     "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = MainWindow()
    # sys.argv(app.exec_())
    app.exec_()
