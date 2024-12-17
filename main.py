import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Агаш Пазл")
        self.resize(650, 550)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
