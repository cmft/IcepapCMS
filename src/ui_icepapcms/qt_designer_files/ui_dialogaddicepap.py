# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogaddicepap.ui'
#
# Created: Mon Sep  3 10:01:32 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogAddIcepap(object):
    def setupUi(self, DialogAddIcepap):
        DialogAddIcepap.setObjectName("DialogAddIcepap")
        DialogAddIcepap.resize(QtCore.QSize(QtCore.QRect(0,0,426,153).size()).expandedTo(DialogAddIcepap.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAddIcepap.sizePolicy().hasHeightForWidth())
        DialogAddIcepap.setSizePolicy(sizePolicy)
        DialogAddIcepap.setWindowIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/ipapsys.png"))

        self.gridlayout = QtGui.QGridLayout(DialogAddIcepap)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(131,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.okButton = QtGui.QPushButton(DialogAddIcepap)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(DialogAddIcepap)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        self.gridlayout.addLayout(self.hboxlayout,2,0,1,8)

        self.label_4 = QtGui.QLabel(DialogAddIcepap)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,1,0,1,1)

        self.txtDescription = QtGui.QTextEdit(DialogAddIcepap)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(0),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(6),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(8),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(12),QtGui.QColor(84,123,196))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        self.txtDescription.setPalette(palette)
        self.txtDescription.setObjectName("txtDescription")
        self.gridlayout.addWidget(self.txtDescription,1,2,1,6)

        self.txtPort = QtGui.QLineEdit(DialogAddIcepap)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(0),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(6),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(8),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(12),QtGui.QColor(84,123,196))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        self.txtPort.setPalette(palette)
        self.txtPort.setMaxLength(6)
        self.txtPort.setObjectName("txtPort")
        self.gridlayout.addWidget(self.txtPort,0,6,1,1)

        self.txtHost = QtGui.QLineEdit(DialogAddIcepap)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(0),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(6),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(8),QtGui.QColor(16,16,16))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(12),QtGui.QColor(101,148,235))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(0),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(1),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(2),QtGui.QColor(237,237,237))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(3),QtGui.QColor(247,245,243))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(4),QtGui.QColor(119,117,115))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(5),QtGui.QColor(159,157,154))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(6),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(8),QtGui.QColor(127,125,123))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,235,231))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(12),QtGui.QColor(84,123,196))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(15),QtGui.QColor(255,0,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(16),QtGui.QColor(247,245,243))
        self.txtHost.setPalette(palette)
        self.txtHost.setObjectName("txtHost")
        self.gridlayout.addWidget(self.txtHost,0,2,1,1)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1,0,7,1,1)

        self.label_2 = QtGui.QLabel(DialogAddIcepap)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,0,1,1)

        self.label_5 = QtGui.QLabel(DialogAddIcepap)
        self.label_5.setPixmap(QtGui.QPixmap(":/small_icons/IcepapCfg Icons/redpixel.png"))
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,0,1,1,1)

        self.label_6 = QtGui.QLabel(DialogAddIcepap)
        self.label_6.setPixmap(QtGui.QPixmap(":/small_icons/IcepapCfg Icons/redpixel.png"))
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,0,5,1,1)

        self.label_1 = QtGui.QLabel(DialogAddIcepap)
        self.label_1.setObjectName("label_1")
        self.gridlayout.addWidget(self.label_1,0,4,1,1)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2,0,3,1,1)

        self.retranslateUi(DialogAddIcepap)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),DialogAddIcepap.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),DialogAddIcepap.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAddIcepap)
        DialogAddIcepap.setTabOrder(self.txtHost,self.txtPort)
        DialogAddIcepap.setTabOrder(self.txtPort,self.txtDescription)
        DialogAddIcepap.setTabOrder(self.txtDescription,self.okButton)
        DialogAddIcepap.setTabOrder(self.okButton,self.cancelButton)

    def retranslateUi(self, DialogAddIcepap):
        DialogAddIcepap.setWindowTitle(QtGui.QApplication.translate("DialogAddIcepap", "Add Icepap System", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("DialogAddIcepap", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DialogAddIcepap", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogAddIcepap", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogAddIcepap", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("DialogAddIcepap", "Port", None, QtGui.QApplication.UnicodeUTF8))

import icepapcms_rc
