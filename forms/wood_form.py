# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wood_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 550)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 198, 391, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sheet_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.sheet_name_label.setObjectName("sheet_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sheet_name_label)
        self.sheet_name = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sheet_name.setObjectName("sheet_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sheet_name)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.wood_type_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.wood_type_label.setObjectName("wood_type_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wood_type_label)
        self.wood_type = QtWidgets.QComboBox(self.formLayoutWidget)
        self.wood_type.setObjectName("wood_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wood_type)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.thickness_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.thickness_label.setObjectName("thickness_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.thickness_label)
        self.thickness = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.thickness.setObjectName("thickness")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.thickness)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sheet_name_label.setText(_translate("Form", "Название листа"))
        self.sheet_name.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.wood_type_label.setText(_translate("Form", "Вид древесины"))
        self.thickness_label.setText(_translate("Form", "Толщина, мм"))
