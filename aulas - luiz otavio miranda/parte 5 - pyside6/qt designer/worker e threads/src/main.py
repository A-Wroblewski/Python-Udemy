import sys
import time

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QWidget, QApplication

from window import Ui_central_widget


# workers são usados no caso de algum processo pesado
# que pode atrapalhar a execução de outras tarefas,
# assim causando o travamento da janela até ser completado
class Worker(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)

        for i in range(1, 6):
            value = str(i)
            time.sleep(1)
            self.progressed.emit(value)

        self.finished.emit(value)


class MainWindow(QWidget, Ui_central_widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.push_button_1.clicked.connect(self.worker_1_process)
        self.push_button_2.clicked.connect(self.worker_2_process)

    def worker_1_process(self):
        # são criadas referências às classes para evitar
        # que o garbage collector do python os destrua
        # antes do fim da execução do processo
        self._worker1 = Worker()
        self._thread1 = QThread()

        worker = self._worker1
        thread = self._thread1

        # move o worker pra thread escolhida, fazendo assim com que
        # todos os métodos do worker sejam executados na thread
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        # após finalizar o processo, ao pedir a exclusão
        # dos objetos garante com que a memória seja liberada
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker_1_started)
        worker.progressed.connect(self.worker_1_progressed)
        worker.finished.connect(self.worker_1_finished)

        thread.start()

    def worker_1_started(self, value):
        self.push_button_1.setDisabled(True)
        self.label_1.setText(value)
        print('worker 1 iniciado', value)

    def worker_1_progressed(self, value):
        self.label_1.setText(value)
        print('worker 1 progrediu', value)

    def worker_1_finished(self, value):
        self.push_button_1.setDisabled(False)
        self.label_1.setText(value)
        print('worker 1 finalizado', value)

    def worker_2_process(self):
        self._worker2 = Worker()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker_2_started)
        worker.progressed.connect(self.worker_2_progressed)
        worker.finished.connect(self.worker_2_finished)

        thread.start()

    def worker_2_started(self, value):
        self.push_button_2.setDisabled(True)
        self.label_2.setText(value)
        print('worker 2 iniciado', value)

    def worker_2_progressed(self, value):
        self.label_2.setText(value)
        print('worker 2 progrediu', value)

    def worker_2_finished(self, value):
        self.push_button_2.setDisabled(False)
        self.label_2.setText(value)
        print('worker 2 finalizado', value)


app = QApplication([])
window = MainWindow()

window.show()
sys.exit(app.exec())
