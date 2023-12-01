# comando pra compilar o arquivo .ui
# pyside6-uic caminho do arquivo ui -o caminho pra onde enviar o ui compilado
# exemplo: pyside6-uic .\ui\window.ui -o .\src\window.py

import sys

from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QMainWindow, QApplication

from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self._connect_button()
        self.name_input.installEventFilter(self)

    def _connect_button(self):
        self.name_button.clicked.connect(self._change_upper_label_text)

    def _get_name_input(self):
        return self.name_input.text()

    def _change_upper_label_text(self):
        text = self._get_name_input()
        self.upper_label.setText(text)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            text = self.name_input.text()
            self.upper_label.setText(text + event.text())

        return super().eventFilter(watched, event)


app = QApplication([])
window = MainWindow()

window.show()
sys.exit(app.exec())
