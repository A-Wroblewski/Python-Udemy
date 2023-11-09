from PySide6.QtWidgets import QPushButton, QGridLayout

from utils.check_number_or_dot import is_number_or_dot
from utils.check_valid_float import is_valid_float


class Button(QPushButton):
    def __init__(self):
        super().__init__()

        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 24px;')
        self.setMinimumSize(70, 70)


class ButtonsGrid(QGridLayout):
    def __init__(self, calculation_label, display):
        super().__init__()

        self._grid_symbols = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]

        self.calculation_label = calculation_label
        self.display = display
        self._calculation = ''
        self._make_grid()

    def _make_grid(self):
        for row_index, list in enumerate(self._grid_symbols):
            for column_index, text in enumerate(list):
                if text:
                    button = Button()
                    button.setText(text)

                    if not is_number_or_dot(text):
                        button.setProperty('cssClass', 'specialButton')
                        self._config_special_button(button)

                    if text == '0':
                        self.addWidget(button, row_index, column_index, 1, 2)
                    else:
                        self.addWidget(button, row_index, column_index)

                    button.clicked.connect(self._insert_button_text_to_display)

    def _insert_button_text_to_display(self):
        button = self.sender()  # sender retorna o objeto que emitiu o sinal
        button_text = button.text()

        future_display_value = self.display.text() + button_text

        if not is_valid_float(future_display_value):
            return

        self.display.insert(button_text)

    def _config_special_button(self, button):
        button_text = button.text()

        if button_text == 'C':
            button.clicked.connect(self.display.clear)

    @property
    def calculation(self):
        return self._calculation

    @calculation.setter
    def calculation(self, value):
        self._calculation = value
        self.calculation_label.setText(self.calculation)
