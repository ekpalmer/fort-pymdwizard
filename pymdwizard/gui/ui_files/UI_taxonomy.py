# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taxonomy2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Taxonomy(object):
    def setupUi(self, Taxonomy):
        Taxonomy.setObjectName("Taxonomy")
        Taxonomy.resize(523, 225)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Taxonomy.sizePolicy().hasHeightForWidth())
        Taxonomy.setSizePolicy(sizePolicy)
        Taxonomy.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Taxonomy)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_taxonomy = QtWidgets.QGroupBox(Taxonomy)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_taxonomy.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_taxonomy.setSizePolicy(sizePolicy)
        self.fgdc_taxonomy.setObjectName("fgdc_taxonomy")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_taxonomy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.fgdc_taxonomy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setStyleSheet("font: italic;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.rbtn_yes = QtWidgets.QRadioButton(self.fgdc_taxonomy)
        self.rbtn_yes.setAutoFillBackground(True)
        self.rbtn_yes.setChecked(False)
        self.rbtn_yes.setObjectName("rbtn_yes")
        self.horizontalLayout.addWidget(self.rbtn_yes)
        self.rbtn_no = QtWidgets.QRadioButton(self.fgdc_taxonomy)
        self.rbtn_no.setAutoFillBackground(True)
        self.rbtn_no.setChecked(True)
        self.rbtn_no.setObjectName("rbtn_no")
        self.horizontalLayout.addWidget(self.rbtn_no)
        self.main_layout.addLayout(self.horizontalLayout)
        self.widget_contents = QtWidgets.QWidget(self.fgdc_taxonomy)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_contents.sizePolicy().hasHeightForWidth()
        )
        self.widget_contents.setSizePolicy(sizePolicy)
        self.widget_contents.setObjectName("widget_contents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_contents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(9, -1, 9, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_search = QtWidgets.QPushButton(self.widget_contents)
        self.btn_search.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_4.addWidget(self.btn_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.keywtax_groupbox = QtWidgets.QGroupBox(self.widget_contents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.keywtax_groupbox.sizePolicy().hasHeightForWidth()
        )
        self.keywtax_groupbox.setSizePolicy(sizePolicy)
        self.keywtax_groupbox.setObjectName("keywtax_groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.keywtax_groupbox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.kws_layout = QtWidgets.QVBoxLayout()
        self.kws_layout.setObjectName("kws_layout")
        self.verticalLayout_4.addLayout(self.kws_layout)
        self.verticalLayout_3.addWidget(self.keywtax_groupbox)
        self.taxoncl_scrollarea = QtWidgets.QScrollArea(self.widget_contents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taxoncl_scrollarea.sizePolicy().hasHeightForWidth()
        )
        self.taxoncl_scrollarea.setSizePolicy(sizePolicy)
        self.taxoncl_scrollarea.setMinimumSize(QtCore.QSize(0, 0))
        self.taxoncl_scrollarea.setMaximumSize(QtCore.QSize(16777215, 350))
        self.taxoncl_scrollarea.setWidgetResizable(True)
        self.taxoncl_scrollarea.setObjectName("taxoncl_scrollarea")
        self.taxoncl_contents = QtWidgets.QWidget()
        self.taxoncl_contents.setGeometry(QtCore.QRect(0, 0, 477, 69))
        self.taxoncl_contents.setObjectName("taxoncl_contents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.taxoncl_contents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.taxoncl_scrollarea.setWidget(self.taxoncl_contents)
        self.verticalLayout_3.addWidget(self.taxoncl_scrollarea)
        self.main_layout.addWidget(self.widget_contents)
        self.verticalLayout.addLayout(self.main_layout)
        self.verticalLayout_2.addWidget(self.fgdc_taxonomy)

        self.retranslateUi(Taxonomy)
        QtCore.QMetaObject.connectSlotsByName(Taxonomy)

    def retranslateUi(self, Taxonomy):
        _translate = QtCore.QCoreApplication.translate
        Taxonomy.setWindowTitle(_translate("Taxonomy", "Form"))
        Taxonomy.setToolTip(_translate("Taxonomy", "test docstring"))
        self.fgdc_taxonomy.setTitle(_translate("Taxonomy", "Taxonomy"))
        self.label_3.setText(
            _translate(
                "Taxonomy",
                "Does this record contain biological data about particular species or other  taxons?",
            )
        )
        self.rbtn_yes.setText(_translate("Taxonomy", "Yes"))
        self.rbtn_no.setText(_translate("Taxonomy", "No"))
        self.btn_search.setText(_translate("Taxonomy", "Add Items from ITIS"))
        self.keywtax_groupbox.setTitle(_translate("Taxonomy", "Taxonomic Keywords"))
