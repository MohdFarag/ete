# #START_LICENSE###########################################################
#
# Copyright (C) 2009 by Jaime Huerta Cepas. All rights reserved.  
# email: jhcepas@gmail.com
#
# This file is part of the Environment for Tree Exploration program (ETE). 
# http://ete.cgenomics.org
#  
# ETE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# ETE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with ETE.  If not, see <http://www.gnu.org/licenses/>.
#
# #END_LICENSE#############################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jaime/pygenomics/pygenomics/treeview/ete_qt4app.ui'
#
# Created: Sun Jun  7 22:17:55 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionPaste_newick = QtGui.QAction(MainWindow)
        self.actionPaste_newick.setObjectName("actionPaste_newick")
        self.actionSave_image = QtGui.QAction(MainWindow)
        self.actionSave_image.setObjectName("actionSave_image")
        self.actionSave_region = QtGui.QAction(MainWindow)
        self.actionSave_region.setObjectName("actionSave_region")
        self.actionBranchLength = QtGui.QAction(MainWindow)
        self.actionBranchLength.setCheckable(True)
        self.actionBranchLength.setObjectName("actionBranchLength")
        self.actionZoomIn = QtGui.QAction(MainWindow)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtGui.QAction(MainWindow)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionETE = QtGui.QAction(MainWindow)
        self.actionETE.setObjectName("actionETE")
        self.actionForceTopology = QtGui.QAction(MainWindow)
        self.actionForceTopology.setCheckable(True)
        self.actionForceTopology.setObjectName("actionForceTopology")
        self.actionSave_newick = QtGui.QAction(MainWindow)
        self.actionSave_newick.setObjectName("actionSave_newick")
        self.actionBranchSupport = QtGui.QAction(MainWindow)
        self.actionBranchSupport.setObjectName("actionBranchSupport")
        self.actionZoomInX = QtGui.QAction(MainWindow)
        self.actionZoomInX.setObjectName("actionZoomInX")
        self.actionZoomOutX = QtGui.QAction(MainWindow)
        self.actionZoomOutX.setObjectName("actionZoomOutX")
        self.actionZoomInY = QtGui.QAction(MainWindow)
        self.actionZoomInY.setObjectName("actionZoomInY")
        self.actionZoomOutY = QtGui.QAction(MainWindow)
        self.actionZoomOutY.setObjectName("actionZoomOutY")
        self.actionFit2tree = QtGui.QAction(MainWindow)
        self.actionFit2tree.setObjectName("actionFit2tree")
        self.actionFit2region = QtGui.QAction(MainWindow)
        self.actionFit2region.setObjectName("actionFit2region")
        self.actionRenderPDF = QtGui.QAction(MainWindow)
        self.actionRenderPDF.setObjectName("actionRenderPDF")
        self.actionSearchNode = QtGui.QAction(MainWindow)
        self.actionSearchNode.setObjectName("actionSearchNode")
        self.actionClearSearch = QtGui.QAction(MainWindow)
        self.actionClearSearch.setObjectName("actionClearSearch")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionPaste_newick)
        self.menuFile.addAction(self.actionSave_newick)
        self.menuFile.addAction(self.actionSave_image)
        self.menuFile.addAction(self.actionSave_region)
        self.menuAbout.addAction(self.actionETE)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionZoomInX)
        self.toolBar.addAction(self.actionZoomOutX)
        self.toolBar.addAction(self.actionZoomInY)
        self.toolBar.addAction(self.actionZoomOutY)
        self.toolBar.addAction(self.actionFit2tree)
        self.toolBar.addAction(self.actionFit2region)
        self.toolBar.addAction(self.actionForceTopology)
        self.toolBar.addAction(self.actionBranchLength)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionRenderPDF)
        self.toolBar.addAction(self.actionSearchNode)
        self.toolBar.addAction(self.actionClearSearch)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste_newick.setText(QtGui.QApplication.translate("MainWindow", "Paste newick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste_newick.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_image.setText(QtGui.QApplication.translate("MainWindow", "Save Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_region.setText(QtGui.QApplication.translate("MainWindow", "Save region", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_region.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBranchLength.setText(QtGui.QApplication.translate("MainWindow", "Show branch lenghts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBranchLength.setShortcut(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionETE.setText(QtGui.QApplication.translate("MainWindow", "ETE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForceTopology.setText(QtGui.QApplication.translate("MainWindow", "Force showing topology", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForceTopology.setToolTip(QtGui.QApplication.translate("MainWindow", "Allows to see topology by setting assuming all branch lenghts are 1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForceTopology.setShortcut(QtGui.QApplication.translate("MainWindow", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_newick.setText(QtGui.QApplication.translate("MainWindow", "Save newick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBranchSupport.setText(QtGui.QApplication.translate("MainWindow", "Show branch support", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomInX.setText(QtGui.QApplication.translate("MainWindow", "Increase X scale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOutX.setText(QtGui.QApplication.translate("MainWindow", "decrease X scale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomInY.setText(QtGui.QApplication.translate("MainWindow", "increase Y scale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOutY.setText(QtGui.QApplication.translate("MainWindow", "decrease Y scale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFit2tree.setText(QtGui.QApplication.translate("MainWindow", "Fit to tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFit2tree.setShortcut(QtGui.QApplication.translate("MainWindow", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFit2region.setText(QtGui.QApplication.translate("MainWindow", "Fit to selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFit2region.setShortcut(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenderPDF.setText(QtGui.QApplication.translate("MainWindow", "renderPDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearchNode.setText(QtGui.QApplication.translate("MainWindow", "searchNode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearchNode.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearSearch.setText(QtGui.QApplication.translate("MainWindow", "clearSearch", None, QtGui.QApplication.UnicodeUTF8))
