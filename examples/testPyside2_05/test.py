#!/usr/bin/env python
# -'''- coding: utf-8 -'''-

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets  import *
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import *

# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
viem = QQuickView()
# Create an URL to the QML file
# url = QUrl('./main.qml')
# Set the QML file and show
url = QUrl('./helloworld/tutorial3.qml')
viem.setSource(url)
viem.show()

# engine.show()
# Enter Qt main loop
sys.exit(app.exec_())