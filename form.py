import os
import shutdownHost
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 294)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 72, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 124, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)

        Form.setAutoFillBackground(True)

        self.ShutdownAll = QtWidgets.QPushButton(Form)
        self.ShutdownAll.setGeometry(QtCore.QRect(20, 70, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.ShutdownAll.setPalette(palette)
        self.ShutdownAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShutdownAll.setObjectName("ShutdownAll")
        self.ShutdownAll.clicked.connect(self.shutAll)

        self.RestartAll = QtWidgets.QPushButton(Form)
        self.RestartAll.setGeometry(QtCore.QRect(160, 70, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.RestartAll.setPalette(palette)
        self.RestartAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RestartAll.setObjectName("RestartAll")
        self.RestartAll.clicked.connect(self.resttAll)

        self.restartHost = QtWidgets.QPushButton(Form)
        self.restartHost.setGeometry(QtCore.QRect(160, 220, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.restartHost.setPalette(palette)
        self.restartHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restartHost.setObjectName("restartHost")
        self.restartHost.clicked.connect(self.restHost)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 140, 261, 31))
        self.label.setObjectName("label")

        self.shutdownHost = QtWidgets.QPushButton(Form)
        self.shutdownHost.setGeometry(QtCore.QRect(20, 220, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.shutdownHost.setPalette(palette)
        self.shutdownHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shutdownHost.setObjectName("shutdownHost")
        self.shutdownHost.clicked.connect(self.shutHost)

        self.viewAliveHost = QtWidgets.QPushButton(Form)
        self.viewAliveHost.setGeometry(QtCore.QRect(160, 10, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.viewAliveHost.setPalette(palette)
        self.viewAliveHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewAliveHost.setObjectName("viewAliveHost")
        self.viewAliveHost.clicked.connect(self.showHost)

        self.scanHost = QtWidgets.QPushButton(Form)
        self.scanHost.setGeometry(QtCore.QRect(20, 10, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.scanHost.setPalette(palette)
        self.scanHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scanHost.setObjectName("scanHost")
        self.scanHost.clicked.connect(self.scan)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 231, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 130, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Network Host Shutdown"))
        self.ShutdownAll.setText(_translate("Form", "Shutdown All Hosts"))
        self.RestartAll.setText(_translate("Form", "Restart All Hosts"))
        self.restartHost.setText(_translate("Form", "Restart Host"))
        self.label.setText(_translate("Form", "  For specific host write down host name or IP address"))
        self.shutdownHost.setText(_translate("Form", "Shutdown Host"))
        self.viewAliveHost.setText(_translate("Form", "View Alive Hosts"))
        self.scanHost.setText(_translate("Form", "Scan Alive Hosts"))

    def shutAll(self):
        shutdownHost.shutAll()

    def resttAll(self):
        shutdownHost.restartAll()

    def shutHost(self):
        hostName = self.lineEdit.text()
        if hostName == "":
            QtWidgets.QMessageBox.information(self, "Empty Field", "Please enter a Host name or Host address")
        else:
            shutdownHost.shutUser(hostName)

    def restHost(self):
        hostName = self.lineEdit.text()
        if hostName == "":
            QtWidgets.QMessageBox.information(self, "Empty Field", "Please enter a Host name or Host address")
        else:
            shutdownHost.restartUser(hostName)

    def scan(self):
        import log_IP_with_host
        log_IP_with_host.log_ip_with_hostname()

    def showHost(self):
        direct = os.getcwd() + "\\aliveHostList.txt"
        os.system("notepad " + direct)
