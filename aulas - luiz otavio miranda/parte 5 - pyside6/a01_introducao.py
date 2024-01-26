import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

def create_buttons():
    button1 = QPushButton('texto1')
    button1.setStyleSheet('font-size: 20px; font-weight: bold;')

    button2 = QPushButton('texto2')
    button2.setStyleSheet('font-size: 40px; color: red;')

    button3 = QPushButton('texto3')
    button3.setStyleSheet('font-size: 60px; color: pink;')

    return button1, button2, button3

@Slot()
def slot_change_status_text(status_bar):
    status_bar.showMessage('mensagem depois da função')

@Slot()
def slot_toggle_action(is_checked):
    print('marcado?', is_checked)

app = QApplication(sys.argv)
window = QMainWindow()

central_widget = QWidget()  # cria um widget genérico que vai servir pra comportar todos os widgets

window.setCentralWidget(central_widget)
window.setWindowTitle('Janelinha')

layout = QGridLayout()
central_widget.setLayout(layout)

button1, button2, button3 = create_buttons()

layout.addWidget(button1, 1, 1, 1, 2)
layout.addWidget(button2, 2, 1)
layout.addWidget(button3, 2, 2)

# seção na parte de baixo da janela
status_bar = window.statusBar()
status_bar.showMessage('mensagem antes da função')

# seção na parte de cima da janela
menu_bar = window.menuBar()
menu = menu_bar.addMenu('Menu')

menu_action1 = menu.addAction('Primeira ação')
menu_action1.triggered.connect(lambda: slot_change_status_text(status_bar))

menu_action2 = menu.addAction('Segunda ação')
menu_action2.setCheckable(True)
menu_action2.toggled.connect(slot_toggle_action)

window.show()
app.exec()
