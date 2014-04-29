# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_layerlistcreator.ui'
#
# Created: Tue Apr 29 20:38:44 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_layerListCreator(object):
    def setupUi(self, layerListCreator):
        layerListCreator.setObjectName(_fromUtf8("layerListCreator"))
        layerListCreator.resize(449, 347)
        self.buttonBox = QtGui.QDialogButtonBox(layerListCreator)
        self.buttonBox.setGeometry(QtCore.QRect(90, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listWidget = QtGui.QListWidget(layerListCreator)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 411, 241))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(layerListCreator)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(layerListCreator)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(layerListCreator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), layerListCreator.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), layerListCreator.reject)
        QtCore.QMetaObject.connectSlotsByName(layerListCreator)

    def retranslateUi(self, layerListCreator):
        layerListCreator.setWindowTitle(QtGui.QApplication.translate("layerListCreator", "Skapa Lagerlista för Ladda Lager plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("layerListCreator", "Inkluderade lager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("layerListCreator", "Included layers", None, QtGui.QApplication.UnicodeUTF8))

