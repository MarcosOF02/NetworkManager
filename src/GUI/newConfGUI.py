# Form implementation generated from reading ui file 'newConfGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_newConfGUI(object):
    def setupUi(self, newConfGUI):
        newConfGUI.setObjectName("newConfGUI")
        newConfGUI.resize(824, 819)
        self.gridLayout_3 = QtWidgets.QGridLayout(newConfGUI)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=newConfGUI)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=newConfGUI)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_3.addWidget(self.lineEdit_name)
        self.label_4 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_4.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_5.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.pushButton_pat = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_pat.setObjectName("pushButton_pat")
        self.verticalLayout_3.addWidget(self.pushButton_pat)
        self.label_PatDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_PatDir_2.setObjectName("label_PatDir_2")
        self.verticalLayout_3.addWidget(self.label_PatDir_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_RefDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_RefDir_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_RefDir_2.setObjectName("label_RefDir_2")
        self.verticalLayout_3.addWidget(self.label_RefDir_2)
        self.pushButton_ref = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_ref.setObjectName("pushButton_ref")
        self.verticalLayout_3.addWidget(self.pushButton_ref)
        self.label_16 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_RoiDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_RoiDir_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_RoiDir_2.setObjectName("label_RoiDir_2")
        self.verticalLayout_3.addWidget(self.label_RoiDir_2)
        self.pushButton_roi = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_roi.setObjectName("pushButton_roi")
        self.verticalLayout_3.addWidget(self.pushButton_roi)
        self.label_17 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_InputDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_InputDir_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_InputDir_2.setObjectName("label_InputDir_2")
        self.verticalLayout_3.addWidget(self.label_InputDir_2)
        self.pushButton_input = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_input.setObjectName("pushButton_input")
        self.verticalLayout_3.addWidget(self.pushButton_input)
        self.label_18 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_outputDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_outputDir_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_outputDir_2.setObjectName("label_outputDir_2")
        self.verticalLayout_3.addWidget(self.label_outputDir_2)
        self.pushButton_output = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_output.setObjectName("pushButton_output")
        self.verticalLayout_3.addWidget(self.pushButton_output)
        self.label_19 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_valDir_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_valDir_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_valDir_2.setObjectName("label_valDir_2")
        self.verticalLayout_3.addWidget(self.label_valDir_2)
        self.pushButton_val = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_val.setObjectName("pushButton_val")
        self.verticalLayout_3.addWidget(self.pushButton_val)
        self.label_20 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.label_2 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton_selectModelDir = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_selectModelDir.setObjectName("pushButton_selectModelDir")
        self.verticalLayout_3.addWidget(self.pushButton_selectModelDir)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(parent=newConfGUI)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.pushButton_saveNew = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_saveNew.setObjectName("pushButton_saveNew")
        self.verticalLayout_3.addWidget(self.pushButton_saveNew)
        self.pushButton_endNew = QtWidgets.QPushButton(parent=newConfGUI)
        self.pushButton_endNew.setObjectName("pushButton_endNew")
        self.verticalLayout_3.addWidget(self.pushButton_endNew)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(newConfGUI)
        QtCore.QMetaObject.connectSlotsByName(newConfGUI)

    def retranslateUi(self, newConfGUI):
        _translate = QtCore.QCoreApplication.translate
        newConfGUI.setWindowTitle(_translate("newConfGUI", "Form"))
        self.label.setText(_translate("newConfGUI", "Name:"))
        self.label_4.setText(_translate("newConfGUI", "Rutas:"))
        self.label_5.setText(_translate("newConfGUI", "Patterns:"))
        self.pushButton_pat.setText(_translate("newConfGUI", "Select Dir"))
        self.label_PatDir_2.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_RefDir_2.setText(_translate("newConfGUI", "Reference:"))
        self.pushButton_ref.setText(_translate("newConfGUI", "Select Dir"))
        self.label_16.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_RoiDir_2.setText(_translate("newConfGUI", "Rois"))
        self.pushButton_roi.setText(_translate("newConfGUI", "Select Dir"))
        self.label_17.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_InputDir_2.setText(_translate("newConfGUI", "Input Dir:"))
        self.pushButton_input.setText(_translate("newConfGUI", "Select Dir"))
        self.label_18.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_outputDir_2.setText(_translate("newConfGUI", "Output Dir:"))
        self.pushButton_output.setText(_translate("newConfGUI", "Select Dir"))
        self.label_19.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_valDir_2.setText(_translate("newConfGUI", "Validation Dir:"))
        self.pushButton_val.setText(_translate("newConfGUI", "Select Dir"))
        self.label_20.setText(_translate("newConfGUI", "Actual dir:"))
        self.label_2.setText(_translate("newConfGUI", "Models Dir:"))
        self.pushButton_selectModelDir.setText(_translate("newConfGUI", "Select Dir"))
        self.label_3.setText(_translate("newConfGUI", "Actual dir:"))
        self.pushButton_saveNew.setText(_translate("newConfGUI", "Guardar Configuracion"))
        self.pushButton_endNew.setText(_translate("newConfGUI", "Acabar"))
