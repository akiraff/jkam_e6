# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageview_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageViewEditor(object):
    def setupUi(self, ImageViewEditor):
        ImageViewEditor.setObjectName("ImageViewEditor")
        ImageViewEditor.resize(565, 422)
        self.gridLayout = QtWidgets.QGridLayout(ImageViewEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.settings_verticalLayout = QtWidgets.QVBoxLayout()
        self.settings_verticalLayout.setObjectName("settings_verticalLayout")
        self.autoscale_pushButton = QtWidgets.QPushButton(ImageViewEditor)
        self.autoscale_pushButton.setObjectName("autoscale_pushButton")
        self.settings_verticalLayout.addWidget(self.autoscale_pushButton)
        self.fullscale_pushButton = QtWidgets.QPushButton(ImageViewEditor)
        self.fullscale_pushButton.setObjectName("fullscale_pushButton")
        self.settings_verticalLayout.addWidget(self.fullscale_pushButton)
        self.customscale_pushButton = QtWidgets.QPushButton(ImageViewEditor)
        self.customscale_pushButton.setObjectName("customscale_pushButton")
        self.settings_verticalLayout.addWidget(self.customscale_pushButton)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.max_label = QtWidgets.QLabel(ImageViewEditor)
        self.max_label.setObjectName("max_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.max_label)
        self.min_label = QtWidgets.QLabel(ImageViewEditor)
        self.min_label.setObjectName("min_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.min_label)
        self.colormap_label = QtWidgets.QLabel(ImageViewEditor)
        self.colormap_label.setObjectName("colormap_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.colormap_label)
        self.max_lineEdit = QtWidgets.QLineEdit(ImageViewEditor)
        self.max_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.max_lineEdit.setObjectName("max_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.max_lineEdit)
        self.min_lineEdit = QtWidgets.QLineEdit(ImageViewEditor)
        self.min_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.min_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.min_lineEdit.setObjectName("min_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.min_lineEdit)
        self.cmap_comboBox = QtWidgets.QComboBox(ImageViewEditor)
        self.cmap_comboBox.setObjectName("cmap_comboBox")
        self.cmap_comboBox.addItem("")
        self.cmap_comboBox.addItem("")
        self.cmap_comboBox.addItem("")
        self.cmap_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmap_comboBox)
        self.settings_verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings_verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.settings_verticalLayout, 0, 1, 1, 1)
        self.imageview = ImageView(ImageViewEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imageview.sizePolicy().hasHeightForWidth())
        self.imageview.setSizePolicy(sizePolicy)
        self.imageview.setMinimumSize(QtCore.QSize(400, 400))
        self.imageview.setObjectName("imageview")
        self.gridLayout.addWidget(self.imageview, 0, 0, 1, 1)

        self.retranslateUi(ImageViewEditor)
        QtCore.QMetaObject.connectSlotsByName(ImageViewEditor)

    def retranslateUi(self, ImageViewEditor):
        _translate = QtCore.QCoreApplication.translate
        ImageViewEditor.setWindowTitle(_translate("ImageViewEditor", "Form"))
        self.autoscale_pushButton.setText(_translate("ImageViewEditor", "Auto Scale"))
        self.fullscale_pushButton.setText(_translate("ImageViewEditor", "Full Scale"))
        self.customscale_pushButton.setText(_translate("ImageViewEditor", "Custom Scale"))
        self.max_label.setText(_translate("ImageViewEditor", "Max"))
        self.min_label.setText(_translate("ImageViewEditor", "Min"))
        self.colormap_label.setText(_translate("ImageViewEditor", "Color Map:"))
        self.max_lineEdit.setText(_translate("ImageViewEditor", "255"))
        self.min_lineEdit.setText(_translate("ImageViewEditor", "0"))
        self.cmap_comboBox.setItemText(0, _translate("ImageViewEditor", "jet"))
        self.cmap_comboBox.setItemText(1, _translate("ImageViewEditor", "gray"))
        self.cmap_comboBox.setItemText(2, _translate("ImageViewEditor", "viridis"))
        self.cmap_comboBox.setItemText(3, _translate("ImageViewEditor", "false2"))
from pyqtgraph import ImageView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageViewEditor = QtWidgets.QWidget()
    ui = Ui_ImageViewEditor()
    ui.setupUi(ImageViewEditor)
    ImageViewEditor.show()
    sys.exit(app.exec_())