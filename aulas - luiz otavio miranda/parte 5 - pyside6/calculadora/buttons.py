from PySide6.QtWidgets import QPushButton, QGridLayout


class Button(QPushButton):
    def __init__(self):
        super().__init__()

        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 24px;')


class ButtonsGrid(QGridLayout):
    def __init__(self):
        super().__init__()

        self._grid_symbols = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]

        self._make_grid()

    def _make_grid(self):
        for row_index, list in enumerate(self._grid_symbols):
            for column_index, text in enumerate(list):
                if text:
                    button = Button()
                    button.setText(self._grid_symbols[row_index][column_index])

                    if text not in '0123456789.':
                        button.setProperty('cssClass', 'specialButton')

                    if text == '0':
                        self.addWidget(button, row_index, column_index, 1, 2)
                    else:
                        self.addWidget(button, row_index, column_index)
