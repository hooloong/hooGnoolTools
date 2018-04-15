# coding:utf-8
import sys

from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])

    label = QLabel("Hello World")
    label.setWindowTitle("My First Application")
    label.setGeometry(300, 300, 250, 175)
    label.show()

    sys.exit(app.exec_())


