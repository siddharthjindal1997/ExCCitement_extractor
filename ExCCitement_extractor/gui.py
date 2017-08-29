# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 651)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textandstuff = QtGui.QTextEdit(self.centralwidget)
        self.textandstuff.setGeometry(QtCore.QRect(10, 460, 581, 101))
        self.textandstuff.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textandstuff.setObjectName(_fromUtf8("textandstuff"))
        self.butCancel = QtGui.QPushButton(self.centralwidget)
        self.butCancel.setGeometry(QtCore.QRect(380, 570, 97, 27))
        self.butCancel.setObjectName(_fromUtf8("butCancel"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 581, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.butGenGraph = QtGui.QPushButton(self.verticalLayoutWidget)
        self.butGenGraph.setObjectName(_fromUtf8("butGenGraph"))
        self.verticalLayout_2.addWidget(self.butGenGraph)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.butLoadFile = QtGui.QPushButton(self.centralwidget)
        self.butLoadFile.setGeometry(QtCore.QRect(160, 10, 241, 27))
        self.butLoadFile.setObjectName(_fromUtf8("butLoadFile"))
        self.buExit = QtGui.QPushButton(self.centralwidget)
        self.buExit.setGeometry(QtCore.QRect(490, 570, 97, 27))
        self.buExit.setObjectName(_fromUtf8("buExit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ExCCitement Extractor", None))
        self.butCancel.setText(_translate("MainWindow", "Cancel", None))
        self.butGenGraph.setText(_translate("MainWindow", "Generate excitement graph and Extract highlights", None))
        self.butLoadFile.setText(_translate("MainWindow", "Load File", None))
        self.buExit.setText(_translate("MainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

