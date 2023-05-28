# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Abc_Expoter_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Alembic_Expoter_Widget(object):
    def setupUi(self, Alembic_Expoter_Widget):
        if not Alembic_Expoter_Widget.objectName():
            Alembic_Expoter_Widget.setObjectName(u"Alembic_Expoter_Widget")
        Alembic_Expoter_Widget.resize(714, 465)
        self.verticalLayout_2 = QVBoxLayout(Alembic_Expoter_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Main_Work_Layout = QFrame(Alembic_Expoter_Widget)
        self.Main_Work_Layout.setObjectName(u"Main_Work_Layout")
        self.Main_Work_Layout.setFrameShape(QFrame.Panel)
        self.Main_Work_Layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Main_Work_Layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Model_Tv_Layout = QVBoxLayout()
        self.Model_Tv_Layout.setObjectName(u"Model_Tv_Layout")
        self.Model_Tv = QTreeView(self.Main_Work_Layout)
        self.Model_Tv.setObjectName(u"Model_Tv")

        self.Model_Tv_Layout.addWidget(self.Model_Tv)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Geo_Btn = QPushButton(self.Main_Work_Layout)
        self.Geo_Btn.setObjectName(u"Geo_Btn")
        self.Geo_Btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.Geo_Btn)

        self.Blur_Btn = QPushButton(self.Main_Work_Layout)
        self.Blur_Btn.setObjectName(u"Blur_Btn")
        self.Blur_Btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.Blur_Btn)

        self.Refresh_Btn = QPushButton(self.Main_Work_Layout)
        self.Refresh_Btn.setObjectName(u"Refresh_Btn")

        self.horizontalLayout.addWidget(self.Refresh_Btn)


        self.Model_Tv_Layout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.Model_Tv_Layout)

        self.Info_Layout = QFrame(self.Main_Work_Layout)
        self.Info_Layout.setObjectName(u"Info_Layout")
        self.Info_Layout.setFrameShape(QFrame.Box)
        self.Info_Layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Info_Layout)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.mov_version_label = QLabel(self.Info_Layout)
        self.mov_version_label.setObjectName(u"mov_version_label")
        self.mov_version_label.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.mov_version_label)

        self.mov_version_comboBox = QComboBox(self.Info_Layout)
        self.mov_version_comboBox.setObjectName(u"mov_version_comboBox")

        self.horizontalLayout_3.addWidget(self.mov_version_comboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startf_label = QLabel(self.Info_Layout)
        self.startf_label.setObjectName(u"startf_label")

        self.horizontalLayout_2.addWidget(self.startf_label)

        self.startf_lineEdit = QLineEdit(self.Info_Layout)
        self.startf_lineEdit.setObjectName(u"startf_lineEdit")
        self.startf_lineEdit.setMinimumSize(QSize(40, 0))
        self.startf_lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_2.addWidget(self.startf_lineEdit)

        self.endf_label = QLabel(self.Info_Layout)
        self.endf_label.setObjectName(u"endf_label")

        self.horizontalLayout_2.addWidget(self.endf_label)

        self.endf_lineEdit = QLineEdit(self.Info_Layout)
        self.endf_lineEdit.setObjectName(u"endf_lineEdit")
        self.endf_lineEdit.setMinimumSize(QSize(40, 0))
        self.endf_lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_2.addWidget(self.endf_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pre_roll_label = QLabel(self.Info_Layout)
        self.pre_roll_label.setObjectName(u"pre_roll_label")

        self.horizontalLayout_2.addWidget(self.pre_roll_label)

        self.pre_roll_spinBox = QSpinBox(self.Info_Layout)
        self.pre_roll_spinBox.setObjectName(u"pre_roll_spinBox")
        self.pre_roll_spinBox.setMaximum(10000)
        self.pre_roll_spinBox.setValue(5)

        self.horizontalLayout_2.addWidget(self.pre_roll_spinBox)

        self.post_roll_label = QLabel(self.Info_Layout)
        self.post_roll_label.setObjectName(u"post_roll_label")

        self.horizontalLayout_2.addWidget(self.post_roll_label)

        self.post_roll_spinBox = QSpinBox(self.Info_Layout)
        self.post_roll_spinBox.setObjectName(u"post_roll_spinBox")
        self.post_roll_spinBox.setMaximum(10000)
        self.post_roll_spinBox.setValue(5)

        self.horizontalLayout_2.addWidget(self.post_roll_spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.step_label = QLabel(self.Info_Layout)
        self.step_label.setObjectName(u"step_label")

        self.horizontalLayout_2.addWidget(self.step_label)

        self.step_comboBox = QComboBox(self.Info_Layout)
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.setObjectName(u"step_comboBox")

        self.horizontalLayout_2.addWidget(self.step_comboBox)

        self.blurstep_label = QLabel(self.Info_Layout)
        self.blurstep_label.setObjectName(u"blurstep_label")

        self.horizontalLayout_2.addWidget(self.blurstep_label)

        self.blurstep_comboBox = QComboBox(self.Info_Layout)
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.addItem("")
        self.blurstep_comboBox.setObjectName(u"blurstep_comboBox")

        self.horizontalLayout_2.addWidget(self.blurstep_comboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.sg_publish_checkBox = QCheckBox(self.Info_Layout)
        self.sg_publish_checkBox.setObjectName(u"sg_publish_checkBox")
        self.sg_publish_checkBox.setEnabled(True)
        self.sg_publish_checkBox.setMaximumSize(QSize(86, 16777215))
        self.sg_publish_checkBox.setCheckable(True)
        self.sg_publish_checkBox.setChecked(False)
        self.sg_publish_checkBox.setTristate(False)

        self.horizontalLayout_4.addWidget(self.sg_publish_checkBox)

        self.line = QFrame(self.Info_Layout)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.tractor_farm_checkBox = QCheckBox(self.Info_Layout)
        self.tractor_farm_checkBox.setObjectName(u"tractor_farm_checkBox")
        self.tractor_farm_checkBox.setMaximumSize(QSize(86, 16777215))
        self.tractor_farm_checkBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.tractor_farm_checkBox)

        self.line_2 = QFrame(self.Info_Layout)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.tractor_address_comboBox = QComboBox(self.Info_Layout)
        self.tractor_address_comboBox.setObjectName(u"tractor_address_comboBox")
        self.tractor_address_comboBox.setIconSize(QSize(1, 1))
        self.tractor_address_comboBox.setFrame(False)

        self.horizontalLayout_4.addWidget(self.tractor_address_comboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.servicekey_label = QLabel(self.Info_Layout)
        self.servicekey_label.setObjectName(u"servicekey_label")

        self.horizontalLayout_4.addWidget(self.servicekey_label)

        self.servicekey_comboBox = QComboBox(self.Info_Layout)
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.addItem("")
        self.servicekey_comboBox.setObjectName(u"servicekey_comboBox")

        self.horizontalLayout_4.addWidget(self.servicekey_comboBox)

        self.horizontalSpacer_5 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.priority_label = QLabel(self.Info_Layout)
        self.priority_label.setObjectName(u"priority_label")

        self.horizontalLayout_4.addWidget(self.priority_label)

        self.priority_lineEdit = QLineEdit(self.Info_Layout)
        self.priority_lineEdit.setObjectName(u"priority_lineEdit")
        self.priority_lineEdit.setMinimumSize(QSize(35, 0))
        self.priority_lineEdit.setMaximumSize(QSize(35, 16777215))
        self.priority_lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_4.addWidget(self.priority_lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.open_dir_pushButton = QPushButton(self.Info_Layout)
        self.open_dir_pushButton.setObjectName(u"open_dir_pushButton")
        self.open_dir_pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.open_dir_pushButton)

        self.abc_export_pushButton = QPushButton(self.Info_Layout)
        self.abc_export_pushButton.setObjectName(u"abc_export_pushButton")
        self.abc_export_pushButton.setStyleSheet(u"background-color: rgb(62, 101, 154);")

        self.horizontalLayout_5.addWidget(self.abc_export_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.Info_Layout)


        self.verticalLayout_2.addWidget(self.Main_Work_Layout)


        self.retranslateUi(Alembic_Expoter_Widget)

        QMetaObject.connectSlotsByName(Alembic_Expoter_Widget)
    # setupUi

    def retranslateUi(self, Alembic_Expoter_Widget):
        Alembic_Expoter_Widget.setWindowTitle(QCoreApplication.translate("Alembic_Expoter_Widget", u"Alembic_Expoter", None))
        self.Geo_Btn.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"GEO", None))
        self.Blur_Btn.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"BLUR", None))
        self.Refresh_Btn.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Refresh", None))
        self.mov_version_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Mov Version :", None))
        self.startf_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"startF: ", None))
        self.startf_lineEdit.setText("")
        self.endf_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"endF: ", None))
        self.endf_lineEdit.setText("")
        self.pre_roll_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"pre -", None))
        self.post_roll_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"post +", None))
        self.step_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"step: ", None))
        self.step_comboBox.setItemText(0, QCoreApplication.translate("Alembic_Expoter_Widget", u"1.00", None))
        self.step_comboBox.setItemText(1, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.50", None))
        self.step_comboBox.setItemText(2, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.25", None))
        self.step_comboBox.setItemText(3, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.10", None))
        self.step_comboBox.setItemText(4, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.05", None))
        self.step_comboBox.setItemText(5, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.01", None))

        self.blurstep_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"BLURstep: ", None))
        self.blurstep_comboBox.setItemText(0, QCoreApplication.translate("Alembic_Expoter_Widget", u"1.00", None))
        self.blurstep_comboBox.setItemText(1, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.50", None))
        self.blurstep_comboBox.setItemText(2, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.25", None))
        self.blurstep_comboBox.setItemText(3, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.10", None))
        self.blurstep_comboBox.setItemText(4, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.05", None))
        self.blurstep_comboBox.setItemText(5, QCoreApplication.translate("Alembic_Expoter_Widget", u"0.01", None))

        self.sg_publish_checkBox.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"SG_publish", None))
        self.tractor_farm_checkBox.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Tractor Farm", None))
        self.servicekey_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Service key: ", None))
        self.servicekey_comboBox.setItemText(0, QCoreApplication.translate("Alembic_Expoter_Widget", u"Cache", None))
        self.servicekey_comboBox.setItemText(1, QCoreApplication.translate("Alembic_Expoter_Widget", u"Lighting", None))
        self.servicekey_comboBox.setItemText(2, QCoreApplication.translate("Alembic_Expoter_Widget", u"Lighting01", None))
        self.servicekey_comboBox.setItemText(3, QCoreApplication.translate("Alembic_Expoter_Widget", u"Lighting02", None))
        self.servicekey_comboBox.setItemText(4, QCoreApplication.translate("Alembic_Expoter_Widget", u"User", None))
        self.servicekey_comboBox.setItemText(5, QCoreApplication.translate("Alembic_Expoter_Widget", u"User01", None))
        self.servicekey_comboBox.setItemText(6, QCoreApplication.translate("Alembic_Expoter_Widget", u"User02", None))
        self.servicekey_comboBox.setItemText(7, QCoreApplication.translate("Alembic_Expoter_Widget", u"All", None))
        self.servicekey_comboBox.setItemText(8, QCoreApplication.translate("Alembic_Expoter_Widget", u"FX", None))

        self.priority_label.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Priority:", None))
        self.priority_lineEdit.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"200", None))
        self.open_dir_pushButton.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Dir...", None))
        self.abc_export_pushButton.setText(QCoreApplication.translate("Alembic_Expoter_Widget", u"Export Alembic / Atom Cache", None))
    # retranslateUi

