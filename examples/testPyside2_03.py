#coding:utf-8
import sys
import time
from PySide2.QtWidgets import QApplication,  QWidget
from PySide2.QtGui import QIcon

class SampleWindow(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         self.setWindowTitle("Sample Window")

         self.setGeometry(300, 300, 400, 350)

     def setIcon(self):
         #设置icon
         appIcon = QIcon("222.ico")
         self.setWindowIcon(appIcon)

if __name__ == "__main__":
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("NameError:", sys.exc_info()[1])
    except SystemExit:\
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])