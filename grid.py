# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:35:47 2022

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
    def __init__(self,columns,row):
        super().__init__()
        self.setWindowTitle("Grid Layouts")
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        for i in range(0,columns,1):
            if i%2 == 0:
                for j in range(0,row,2):
                    self.layout.addWidget(Color('black'),i,j)
                    self.layout.addWidget(Color('white'),i,j+1)
            else:
                for j in range(1,row,2):
                    self.layout.addWidget(Color('black'),i,j)
                    self.layout.addWidget(Color('white'),i,j-1)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Window(10,10)
window.show()
app.exec_()