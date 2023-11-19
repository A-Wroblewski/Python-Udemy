from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit

from utils.check_number_or_dot import is_number_or_dot


class Display(QLineEdit):
    # enter_pressed = Signal()
    # delete_pressed = Signal()
    # esc_pressed = Signal()
    # input_pressed = Signal(str)
    # operator_pressed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self._config_style()

    def _config_style(self):
        self.setStyleSheet('font-size: 50px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(3, 3, 3, 3)

    # def keyPressEvent(self, event):
    #     key = event.key()
    #     text = event.text()  # string da tecla pressionada

    #     is_confirm = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal]
    #     is_delete = key in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete]
    #     is_clear = key in [Qt.Key.Key_Escape, Qt.Key.Key_C]
    #     is_operator = key in [Qt.Key.Key_Plus, Qt.Key.Key_Minus, Qt.Key.Key_Slash, Qt.Key.Key_Asterisk, Qt.Key.Key_AsciiCircum]

    #     if is_confirm:
    #         self.enter_pressed.emit()
    #         return event.ignore()

    #     if is_delete:
    #         self.delete_pressed.emit()
    #         return event.ignore()

    #     if is_clear:
    #         self.esc_pressed.emit()
    #         return event.ignore()

    #     if is_operator:
    #         self.operator_pressed.emit(text)
    #         return event.ignore()

    #     if len(text) == 0:
    #         return event.ignore()

    #     if is_number_or_dot(text):
    #         self.input_pressed.emit(text)
    #         return event.ignore()
