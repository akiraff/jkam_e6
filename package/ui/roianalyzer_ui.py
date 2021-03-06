# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_resources\roianalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoiAnalyzer(object):
    def setupUi(self, RoiAnalyzer):
        RoiAnalyzer.setObjectName("RoiAnalyzer")
        RoiAnalyzer.resize(228, 134)
        self.gridLayout_2 = QtWidgets.QGridLayout(RoiAnalyzer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(RoiAnalyzer)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.enable_checkBox = QtWidgets.QCheckBox(self.frame)
        self.enable_checkBox.setObjectName("enable_checkBox")
        self.gridLayout.addWidget(self.enable_checkBox, 1, 0, 1, 1)
        self.bg_subtract_checkBox = QtWidgets.QCheckBox(self.frame)
        self.bg_subtract_checkBox.setObjectName("bg_subtract_checkBox")
        self.gridLayout.addWidget(self.bg_subtract_checkBox, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)

        self.retranslateUi(RoiAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(RoiAnalyzer)

    def retranslateUi(self, RoiAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        RoiAnalyzer.setWindowTitle(_translate("RoiAnalyzer", "Form"))
        self.label.setText(_translate("RoiAnalyzer", "ROI Analyzer"))
        self.enable_checkBox.setText(_translate("RoiAnalyzer", "Enable"))
        self.bg_subtract_checkBox.setText(_translate("RoiAnalyzer", "Background Subtract"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoiAnalyzer = QtWidgets.QWidget()
    ui = Ui_RoiAnalyzer()
    ui.setupUi(RoiAnalyzer)
    RoiAnalyzer.show()
    sys.exit(app.exec_())
