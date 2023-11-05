from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self):
        super().__init__()

        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 50px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(3, 3, 3, 3)
