<<<<<<< HEAD
import sys
import os
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot


class Main_Widget(QWidget):

    def __init__(self, window_width, window_height):
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width
        self.initUI()

    def initUI(self):

        self.resize(self.window_width, self.window_height)
        self.center()

        self.setWindowTitle('VK Social Graph')

        self.tb_start_id = QLineEdit(self)
        self.tb_start_id.move(self.window_width / 2 - self.tb_start_id.width() /
                              2 - self.window_width / 35, self.window_height / 7)
        self.tb_start_id.setPlaceholderText("Enter your id")

        self.tb_finish_id = QLineEdit(self)
        self.tb_finish_id.move(self.window_width / 2 - self.tb_finish_id.width() / 2 - self.window_width / 35, 2 *
                               self.window_height / 7)
        self.tb_finish_id.setPlaceholderText("Enter another id")

        self.tb_depth = QLineEdit(self)
        self.tb_depth.move(self.window_width / 2 - self.tb_depth.width() / 2 - self.window_width / 35, 3 *
                           self.window_height / 7)
        self.tb_depth.setPlaceholderText("Enter depth")

        self.btn = QPushButton("OK", self)
        self.btn.move(self.window_width / 2 - self.btn.width() /
                      2 + self.window_width / 13, 5 * self.window_height / 7)
        self.btn.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        os.system("python3 ../script.py " + str(self.tb_depth.text()) + " " +
                  str(self.tb_start_id.text()) + " " + str(self.tb_finish_id.text()))
        os.system("python3 ../code.py")

        # return

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = Main_Widget(300, 200)
    sys.exit(app.exec_())
=======
import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot
from qtpy import QtGui


class Main_Widget(QWidget):

    def __init__(self, window_width, window_height):
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width
        self.initUI()


    def initUI(self):

        self.resize(self.window_width, self.window_height)
        self.center()

        self.setWindowTitle('VK Social Graph')

        self.tb_start_id = QLineEdit(self)
        self.tb_start_id.move(self.window_width / 2 - self.tb_start_id.width() / 2 - self.window_width / 35, self.window_height / 7)
        self.tb_start_id.setPlaceholderText("Enter your id")

        self.tb_finish_id = QLineEdit(self)
        self.tb_finish_id.move(self.window_width / 2 - self.tb_finish_id.width() / 2 - self.window_width / 35, 2 *
                               self.window_height / 7)
        self.tb_finish_id.setPlaceholderText("Enter another id")

        self.tb_depth = QLineEdit(self)
        self.tb_depth.move(self.window_width / 2 - self.tb_depth.width() / 2 - self.window_width / 35, 3 *
                           self.window_height / 7)
        self.tb_depth.setPlaceholderText("Enter depth")

        self.btn = QPushButton("OK", self)
        self.btn.move(self.window_width / 2 - self.btn.width() / 2 + self.window_width/13, 5 * self.window_height / 7)
        self.btn.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        os.system("python ../script.py " + str(self.tb_depth.text()) + " " +
                  str(self.tb_start_id.text()) + " " + str(self.tb_finish_id.text()))

        os.system("python ../code.py")

        self.tb_finish_id.deleteLater()
        self.tb_start_id.deleteLater()
        self.tb_btn_id.deleteLater()
        self.label = QLabel(self)
        self.pixmap = QPixmap('graph.jpg')
        self.label.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.show()
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = Main_Widget(300, 200)
    sys.exit(app.exec_())


>>>>>>> 4d12a4672e64acddc029aa6ff4053e70e16cded7
