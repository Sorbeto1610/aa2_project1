# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:22:22 2022

@author: Gabriel
"""

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QCoreApplication

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.myPalette = self.palette()
        self.myPalette.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.myPalette)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Grid Layouts")
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(Color('black'),0,0)
        self.layout.addWidget(Color('black'),0,1)
        self.layout.addWidget(Color('black'),0,2)
        self.layout.addWidget(Color('red'),1,0)
        self.layout.addWidget(Color('red'),1,1)
        self.layout.addWidget(Color('red'),1,2)
        self.layout.addWidget(Color('yellow'),2,0)
        self.layout.addWidget(Color('yellow'),2,1)
        self.layout.addWidget(Color('yellow'),2,2)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()