# coding:utf-8

import sys
from PySide2.QtCore import QDateTime, QTimer, SIGNAL
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber

class MyTimer(QWidget):
    """计时器的主窗口类"""

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("My Digital Clock")
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.updtTime)
        self.myTimeDisplay = QLCDNumber(self)
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.myTimeDisplay.setDigitCount(8)
        self.myTimeDisplay.resize(500, 150)
        timer.start(1000)

    def updtTime(self):
        """更新当前时间"""
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.myTimeDisplay.display(currentTime)


if __name__ == "__main__":
    try:
        myApp = QApplication(sys.argv)
        myWindow = MyTimer()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error", sys.exe_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exe_info()[1])