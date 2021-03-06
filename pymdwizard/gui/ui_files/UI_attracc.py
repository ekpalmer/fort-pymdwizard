# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attracc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 133)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_attracc = QtWidgets.QGroupBox(Form)
        self.fgdc_attracc.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_attracc.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fgdc_attracc.setObjectName("fgdc_attracc")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fgdc_attracc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.fgdc_attracc)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.fgdc_attraccr = GrowingTextEdit(self.fgdc_attracc)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_attraccr.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_attraccr.setSizePolicy(sizePolicy)
        self.fgdc_attraccr.setMinimumSize(QtCore.QSize(0, 45))
        self.fgdc_attraccr.setMaximumSize(QtCore.QSize(16777215, 45))
        self.fgdc_attraccr.setObjectName("fgdc_attraccr")
        self.verticalLayout_2.addWidget(self.fgdc_attraccr)
        self.verticalLayout.addWidget(self.fgdc_attracc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_attracc.setTitle(_translate("Form", "Attribute Accuracy Report"))
        self.label.setText(
            _translate(
                "Form",
                'How accurate are the values in the dataset relative to "true" values?   Were any tests performed to assess the accuracy of values?   Please describe any methods used to ensure quality / accuracy in the data.  See help for more info.',
            )
        )
        self.fgdc_attraccr.setPlainText(
            _translate("Form", "No formal attribute accuracy tests were conducted.")
        )


from growingtextedit import GrowingTextEdit
