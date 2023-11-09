from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit


class Display(QLineEdit):
    def __init__(self):
        super().__init__()

        self._config_style()

    def _config_style(self):
        self.setStyleSheet('font-size: 50px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(3, 3, 3, 3)
