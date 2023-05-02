#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:43:41 2023

@author: DK

refer: https://pythonspot.com/pyqt5-treeview/
"""

import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
QTime, QDir)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
QWidget, QFileSystemModel)

class App(QWidget):
    
    # setup the variables for the infomodel
    Name, Code, Update, POC, Stat, LAT, LON = range(7)
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Tutorial by DK'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 500
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        # station info viewer
        self.dataGroupBox = QGroupBox("Station Viewer")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
        
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
        
        
        # creating infomodel that can save info before display
        infomodel = self.createInfoModel(self)
        self.dataView.setModel(infomodel)
        # add data to the table
        # in the future, this process will be automized using the input value from the compensator program
        self.addInfo(infomodel, 'Inlet A', 'ILA','03/25/2023','DK','Working','4799958','438889')
        self.addInfo(infomodel, 'Inlet B', 'ILB','02/02/2023','DK','Suspended','4799957','438883')
        self.addInfo(infomodel, 'Outlet', 'OUT','01/01/2023','Dr.Cherkauer','Working','4799955','438889')

        
        
        # file directory viewer
        self.dirGroupBox = QGroupBox("DIR Viewer")
        self.model = QFileSystemModel()
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        
        self.tree.setIndentation(10)
        self.tree.setSortingEnabled(True)
        
        
        dirLayout = QHBoxLayout()
        dirLayout.addWidget(self.tree)
        self.dirGroupBox.setLayout(dirLayout)
        

        # add widgets to the layout vertically using QVBOXLayout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        mainLayout.addWidget(self.dirGroupBox)
        
        
        self.setLayout(mainLayout)
        
        
        # show the window
        self.show()

    def createInfoModel(self,parent):
        model = QStandardItemModel(0, 7, parent)
        model.setHeaderData(self.Name, Qt.Horizontal, "Name")
        model.setHeaderData(self.Code, Qt.Horizontal, "Code")
        model.setHeaderData(self.Update, Qt.Horizontal, "Last Update")
        model.setHeaderData(self.POC, Qt.Horizontal, "POC")
        model.setHeaderData(self.Stat, Qt.Horizontal, "Status")
        model.setHeaderData(self.LAT, Qt.Horizontal, "Lat")
        model.setHeaderData(self.LON, Qt.Horizontal, "Lon")

        return model
    
    def addInfo(self,model, Name, Code, Update, POC, Stat, Lat, Lon):
        model.insertRow(0)
        model.setData(model.index(0, self.Name), Name)
        model.setData(model.index(0, self.Code), Code)
        model.setData(model.index(0, self.Update), Update)
        model.setData(model.index(0, self.POC), POC)
        model.setData(model.index(0, self.Stat), Stat)
        model.setData(model.index(0, self.LAT), Lat)
        model.setData(model.index(0, self.LON), Lon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
