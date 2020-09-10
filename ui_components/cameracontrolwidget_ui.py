# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameracontrolwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraControlWidget(object):
    def setupUi(self, CameraControlWidget):
        CameraControlWidget.setObjectName("CameraControlWidget")
        self.gridLayout = QtWidgets.QGridLayout(CameraControlWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.exposure_pushButton = QtWidgets.QPushButton(CameraControlWidget)
        self.exposure_pushButton.setEnabled(False)
        self.exposure_pushButton.setObjectName("exposure_pushButton")
        self.gridLayout.addWidget(self.exposure_pushButton, 8, 0, 1, 2)
        self.serial_label = QtWidgets.QLabel(CameraControlWidget)
        self.serial_label.setObjectName("serial_label")
        self.gridLayout.addWidget(self.serial_label, 5, 0, 1, 2)
        self.trigger_source_label = QtWidgets.QLabel(CameraControlWidget)
        self.trigger_source_label.setObjectName("trigger_source_label")
        self.gridLayout.addWidget(self.trigger_source_label, 13, 0, 1, 1)
        self.hardware_trigger_radioButton = QtWidgets.QRadioButton(CameraControlWidget)
        self.hardware_trigger_radioButton.setEnabled(False)
        self.hardware_trigger_radioButton.setChecked(True)
        self.hardware_trigger_radioButton.setObjectName("hardware_trigger_radioButton")
        self.trigger_buttonGroup = QtWidgets.QButtonGroup(CameraControlWidget)
        self.trigger_buttonGroup.setObjectName("trigger_buttonGroup")
        self.trigger_buttonGroup.addButton(self.hardware_trigger_radioButton)
        self.gridLayout.addWidget(self.hardware_trigger_radioButton, 14, 0, 1, 1)
        self.trigger_mode_label = QtWidgets.QLabel(CameraControlWidget)
        self.trigger_mode_label.setObjectName("trigger_mode_label")
        self.gridLayout.addWidget(self.trigger_mode_label, 10, 0, 1, 1)
        self.exposure_formLayout = QtWidgets.QFormLayout()
        self.exposure_formLayout.setObjectName("exposure_formLayout")
        self.exposure_label = QtWidgets.QLabel(CameraControlWidget)
        self.exposure_label.setMinimumSize(QtCore.QSize(150, 0))
        self.exposure_label.setObjectName("exposure_label")
        self.exposure_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.exposure_label)
        self.exposure_lineEdit = QtWidgets.QLineEdit(CameraControlWidget)
        self.exposure_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.exposure_lineEdit.setObjectName("exposure_lineEdit")
        self.exposure_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.exposure_lineEdit)
        self.gridLayout.addLayout(self.exposure_formLayout, 4, 0, 1, 2)
        self.start_pushButton = QtWidgets.QPushButton(CameraControlWidget)
        self.start_pushButton.setEnabled(False)
        self.start_pushButton.setObjectName("start_pushButton")
        self.gridLayout.addWidget(self.start_pushButton, 1, 0, 1, 2)
        self.software_trigger_radioButton = QtWidgets.QRadioButton(CameraControlWidget)
        self.software_trigger_radioButton.setEnabled(False)
        self.software_trigger_radioButton.setObjectName("software_trigger_radioButton")
        self.trigger_buttonGroup.addButton(self.software_trigger_radioButton)
        self.gridLayout.addWidget(self.software_trigger_radioButton, 14, 1, 1, 1)
        self.arm_pushButton = QtWidgets.QPushButton(CameraControlWidget)
        self.arm_pushButton.setObjectName("arm_pushButton")
        self.gridLayout.addWidget(self.arm_pushButton, 0, 0, 1, 2)
        self.software_trigger_pushButton = QtWidgets.QPushButton(CameraControlWidget)
        self.software_trigger_pushButton.setEnabled(False)
        self.software_trigger_pushButton.setObjectName("software_trigger_pushButton")
        self.gridLayout.addWidget(self.software_trigger_pushButton, 15, 0, 1, 2)
        self.triggered_radioButton = QtWidgets.QRadioButton(CameraControlWidget)
        self.triggered_radioButton.setEnabled(False)
        self.triggered_radioButton.setObjectName("triggered_radioButton")
        self.mode_buttonGroup = QtWidgets.QButtonGroup(CameraControlWidget)
        self.mode_buttonGroup.setObjectName("mode_buttonGroup")
        self.mode_buttonGroup.addButton(self.triggered_radioButton)
        self.gridLayout.addWidget(self.triggered_radioButton, 11, 0, 1, 1)
        self.continuous_radioButton = QtWidgets.QRadioButton(CameraControlWidget)
        self.continuous_radioButton.setEnabled(False)
        self.continuous_radioButton.setChecked(True)
        self.continuous_radioButton.setObjectName("continuous_radioButton")
        self.mode_buttonGroup.addButton(self.continuous_radioButton)
        self.gridLayout.addWidget(self.continuous_radioButton, 11, 1, 1, 1)

        self.retranslateUi(CameraControlWidget)
        QtCore.QMetaObject.connectSlotsByName(CameraControlWidget)

    def retranslateUi(self, CameraControlWidget):
        _translate = QtCore.QCoreApplication.translate
        self.exposure_pushButton.setText(_translate("CameraControlWidget", "Update Exposure Time"))
        self.serial_label.setText(_translate("CameraControlWidget", "Serial Number: xxxxxxxx"))
        self.trigger_source_label.setText(_translate("CameraControlWidget", "Trigger Source:"))
        self.hardware_trigger_radioButton.setText(_translate("CameraControlWidget", "Hardware"))
        self.trigger_mode_label.setText(_translate("CameraControlWidget", "Trigger Mode"))
        self.exposure_label.setText(_translate("CameraControlWidget", "Exposure Time (ms)"))
        self.exposure_lineEdit.setText(_translate("CameraControlWidget", "10"))
        self.start_pushButton.setText(_translate("CameraControlWidget", "Start Camera"))
        self.software_trigger_radioButton.setText(_translate("CameraControlWidget", "Software"))
        self.arm_pushButton.setText(_translate("CameraControlWidget", "Arm Camera"))
        self.software_trigger_pushButton.setText(_translate("CameraControlWidget", "Software Trigger"))
        self.triggered_radioButton.setText(_translate("CameraControlWidget", "Triggered"))
        self.continuous_radioButton.setText(_translate("CameraControlWidget", "Continuous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraControlWidget = QtWidgets.QWidget()
    ui = Ui_CameraControlWidget()
    ui.setupUi(CameraControlWidget)
    CameraControlWidget.show()
    sys.exit(app.exec_())
