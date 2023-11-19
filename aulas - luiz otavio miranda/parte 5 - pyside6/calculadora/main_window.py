from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

from utils.pyinstaller_media import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        central_widget.setLayout(self.vertical_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Calculadora')

        icon_path = resource_path('calculator.ico')
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

    def adjust_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def make_message_box(self):
        return QMessageBox(self)
