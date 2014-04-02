# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_radialband.ui'
#
# Created: Tue Apr  1 16:09:11 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RadialBand(object):
    def setupUi(self, RadialBand):
        RadialBand.setObjectName(_fromUtf8("RadialBand"))
        RadialBand.resize(374, 325)
        self.buttonBox = QtGui.QDialogButtonBox(RadialBand)
        self.buttonBox.setGeometry(QtCore.QRect(20, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.BandLine = QtGui.QLineEdit(RadialBand)
        self.BandLine.setGeometry(QtCore.QRect(10, 50, 131, 21))
        self.BandLine.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.BandLine.setText(_fromUtf8(""))
        self.BandLine.setObjectName(_fromUtf8("BandLine"))
        self.AddBand = QtGui.QPushButton(RadialBand)
        self.AddBand.setGeometry(QtCore.QRect(10, 80, 131, 23))
        self.AddBand.setObjectName(_fromUtf8("AddBand"))
        self.listWidget = QtGui.QListWidget(RadialBand)
        self.listWidget.setGeometry(QtCore.QRect(155, 50, 211, 192))
        self.listWidget.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.DeleteBand = QtGui.QPushButton(RadialBand)
        self.DeleteBand.setGeometry(QtCore.QRect(10, 110, 131, 21))
        self.DeleteBand.setObjectName(_fromUtf8("DeleteBand"))
        self.ClearBand = QtGui.QPushButton(RadialBand)
        self.ClearBand.setGeometry(QtCore.QRect(10, 140, 131, 21))
        self.ClearBand.setObjectName(_fromUtf8("ClearBand"))
        self.label = QtGui.QLabel(RadialBand)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(RadialBand)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 201, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(RadialBand)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 121, 61))
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))


        self.retranslateUi(RadialBand)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RadialBand.reject)
        QtCore.QObject.connect(self.AddBand, QtCore.SIGNAL(_fromUtf8("clicked()")), RadialBand.AddData)
        QtCore.QObject.connect(self.DeleteBand, QtCore.SIGNAL(_fromUtf8("clicked()")), RadialBand.DeleteData)
        QtCore.QObject.connect(self.ClearBand, QtCore.SIGNAL(_fromUtf8("clicked()")), RadialBand.ClearBands)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RadialBand.accept)
        QtCore.QMetaObject.connectSlotsByName(RadialBand)

    def AddData(self):
        bandradius=self.BandLine.text()
        test=1
        try:
            bandradius = int(bandradius)
        except Exception:
            test=0
            pass
        
        test2=0
        
        if test<>0:
            bandradius=self.BandLine.text()
            
            if self.listWidget.count()<>0:
                for i in range(self.listWidget.count()):
                    if bandradius<>self.listWidget.item(i).text() and test2<>1:
                        test2=0
                    else:
                        test2=1

                if test2==0:
                    self.listWidget.addItem(bandradius)
                    self.BandLine.clear()
                    bandradius=None
                else:
                    QtGui.QMessageBox.about(self, 'Error','Radius is allready listed!')
                    
            else:    
                self.listWidget.addItem(bandradius)
                self.BandLine.clear()
                bandradius=None
        else:
            self.BandLine.clear()
            bandradius=None
            QtGui.QMessageBox.about(self, 'Error','Radius can only be a number')

    def DeleteData(self):
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        item = None

    def ClearBands(self):
        self.listWidget.clear()

    def CalculateRings(self):
        print('accepted')

    def retranslateUi(self, RadialBand):
        RadialBand.setWindowTitle(QtGui.QApplication.translate("RadialBand", "RadialBand", None, QtGui.QApplication.UnicodeUTF8))
        self.AddBand.setText(QtGui.QApplication.translate("RadialBand", "Add Band", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteBand.setText(QtGui.QApplication.translate("RadialBand", "Delete Band", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearBand.setText(QtGui.QApplication.translate("RadialBand", "Clear Bands", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RadialBand", "Insert Radius (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RadialBand", "Added Rings:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RadialBand", "Rings will be calculated for the selected points", None, QtGui.QApplication.UnicodeUTF8))

