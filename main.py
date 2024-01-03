import sys
import random
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Circles(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.circles = [[QLabel(self), random.randint(10, 300), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))] for _ in range(3)]
        [self.circles[i][0].move(30 + 620 * i, 300) for i in range(len(self.circles))]
        [self.circles[i][0].resize(self.circles[i][1] * 2, self.circles[i][1] * 2) for i in range(len(self.circles))]

    def run(self):
        [self.circles[i][0].setStyleSheet(f'background: rgb({self.circles[i][-1][0]}, {self.circles[i][-1][1]}, {self.circles[i][-1][2]}); border-radius:{self.circles[i][1]}px') for i in range(len(self.circles))]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
