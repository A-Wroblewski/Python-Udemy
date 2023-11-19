import sys
import app_style

from PySide6.QtWidgets import QApplication

from buttons import ButtonsGrid
from display import Display
from calculation_label import CalculationLabel
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()

    app_style.config_style()

    # textinho com as contas já feitas
    calculation_label = CalculationLabel()
    window.vertical_layout.addWidget(calculation_label)

    # campo das contas
    display = Display()
    window.vertical_layout.addWidget(display)

    # nova grid pra comportar os botões
    buttons_grid = ButtonsGrid(window, calculation_label, display)
    window.vertical_layout.addLayout(buttons_grid)

    window.adjust_size()
    window.show()
    sys.exit(app.exec())
