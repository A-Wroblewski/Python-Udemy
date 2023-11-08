from PySide6.QtWidgets import QPushButton, QGridLayout


class Button(QPushButton):
    def __init__(self):
        super().__init__()

        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 24px;')
        self.setMinimumSize(70, 70)


class ButtonsGrid(QGridLayout):
    def __init__(self, display):
        super().__init__()

        self._grid_symbols = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]

        self.display = display
        self._make_grid()

    def _make_grid(self):
        for row_index, list in enumerate(self._grid_symbols):
            for column_index, text in enumerate(list):
                if text:
                    button = Button()
                    button.setText(text)

                    if text not in '0123456789.':
                        button.setProperty('cssClass', 'specialButton')

                    if text == '0':
                        self.addWidget(button, row_index, column_index, 1, 2)
                    else:
                        self.addWidget(button, row_index, column_index)

                    button.clicked.connect(self._insert_button_text_to_display)

    def _insert_button_text_to_display(self):
        button = self.sender()  # sender retorna o objeto que emitiu o sinal
        button_text = button.text()

        self.display.insert(button_text)
