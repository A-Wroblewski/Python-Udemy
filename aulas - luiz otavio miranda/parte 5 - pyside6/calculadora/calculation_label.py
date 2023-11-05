from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class CalculationLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 16px;')
        self.setText('2.0 ^ 10.0 = 1024')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
