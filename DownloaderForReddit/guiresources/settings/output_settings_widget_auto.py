# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\settings\output_settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutputSettingsWidget(object):
    def setupUi(self, OutputSettingsWidget):
        OutputSettingsWidget.setObjectName("OutputSettingsWidget")
        OutputSettingsWidget.resize(906, 709)
        self.horizontalLayout = QtWidgets.QHBoxLayout(OutputSettingsWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.output_display_groupbox = QtWidgets.QGroupBox(OutputSettingsWidget)
        self.output_display_groupbox.setObjectName("output_display_groupbox")
        self.formLayout = QtWidgets.QFormLayout(self.output_display_groupbox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.output_display_groupbox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.priority_level_combo = QtWidgets.QComboBox(self.output_display_groupbox)
        self.priority_level_combo.setObjectName("priority_level_combo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.priority_level_combo)
        self.label_2 = QtWidgets.QLabel(self.output_display_groupbox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.show_priority_level_checkbox = QtWidgets.QCheckBox(self.output_display_groupbox)
        self.show_priority_level_checkbox.setText("")
        self.show_priority_level_checkbox.setObjectName("show_priority_level_checkbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.show_priority_level_checkbox)
        self.label_3 = QtWidgets.QLabel(self.output_display_groupbox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.clear_on_run_checkbox = QtWidgets.QCheckBox(self.output_display_groupbox)
        self.clear_on_run_checkbox.setText("")
        self.clear_on_run_checkbox.setObjectName("clear_on_run_checkbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clear_on_run_checkbox)
        self.line = QtWidgets.QFrame(self.output_display_groupbox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.output_display_groupbox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.output_saved_content_full_path_checkbox = QtWidgets.QCheckBox(self.output_display_groupbox)
        self.output_saved_content_full_path_checkbox.setText("")
        self.output_saved_content_full_path_checkbox.setObjectName("output_saved_content_full_path_checkbox")
        self.horizontalLayout_2.addWidget(self.output_saved_content_full_path_checkbox)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.output_display_groupbox)
        self.use_color_output_checkbox = QtWidgets.QCheckBox(OutputSettingsWidget)
        self.use_color_output_checkbox.setObjectName("use_color_output_checkbox")
        self.verticalLayout.addWidget(self.use_color_output_checkbox)
        self.color_groupbox = QtWidgets.QGroupBox(OutputSettingsWidget)
        self.color_groupbox.setCheckable(False)
        self.color_groupbox.setObjectName("color_groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.color_groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.debug_color_label = QtWidgets.QLabel(self.color_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_color_label.sizePolicy().hasHeightForWidth())
        self.debug_color_label.setSizePolicy(sizePolicy)
        self.debug_color_label.setObjectName("debug_color_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.debug_color_label)
        self.change_debug_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_debug_color_button.setObjectName("change_debug_color_button")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.change_debug_color_button)
        self.info_color_label = QtWidgets.QLabel(self.color_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_color_label.sizePolicy().hasHeightForWidth())
        self.info_color_label.setSizePolicy(sizePolicy)
        self.info_color_label.setObjectName("info_color_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.info_color_label)
        self.change_info_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_info_color_button.setObjectName("change_info_color_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.change_info_color_button)
        self.warning_color_label = QtWidgets.QLabel(self.color_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning_color_label.sizePolicy().hasHeightForWidth())
        self.warning_color_label.setSizePolicy(sizePolicy)
        self.warning_color_label.setObjectName("warning_color_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.warning_color_label)
        self.change_warning_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_warning_color_button.setObjectName("change_warning_color_button")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.change_warning_color_button)
        self.error_color_label = QtWidgets.QLabel(self.color_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_color_label.sizePolicy().hasHeightForWidth())
        self.error_color_label.setSizePolicy(sizePolicy)
        self.error_color_label.setObjectName("error_color_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.error_color_label)
        self.change_error_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_error_color_button.setObjectName("change_error_color_button")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.change_error_color_button)
        self.critical_color_label = QtWidgets.QLabel(self.color_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.critical_color_label.sizePolicy().hasHeightForWidth())
        self.critical_color_label.setSizePolicy(sizePolicy)
        self.critical_color_label.setObjectName("critical_color_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.critical_color_label)
        self.change_critical_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_critical_color_button.setObjectName("change_critical_color_button")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.change_critical_color_button)
        self.requested_color_label = QtWidgets.QLabel(self.color_groupbox)
        self.requested_color_label.setObjectName("requested_color_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.requested_color_label)
        self.change_requested_color_button = QtWidgets.QPushButton(self.color_groupbox)
        self.change_requested_color_button.setObjectName("change_requested_color_button")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.change_requested_color_button)
        self.verticalLayout.addWidget(self.color_groupbox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(OutputSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(OutputSettingsWidget)

    def retranslateUi(self, OutputSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        OutputSettingsWidget.setWindowTitle(_translate("OutputSettingsWidget", "Output Settings"))
        self.output_display_groupbox.setTitle(_translate("OutputSettingsWidget", "Output Display"))
        self.label.setToolTip(_translate("OutputSettingsWidget", "<html><head/><body><p>The level of message that will be displayed in the output window. All levels above the selected will be displayed.</p></body></html>"))
        self.label.setText(_translate("OutputSettingsWidget", "Output priority level:"))
        self.label_2.setToolTip(_translate("OutputSettingsWidget", "<html><head/><body><p>If selected, each message shown in the output will start with the message\'s priority level</p></body></html>"))
        self.label_2.setText(_translate("OutputSettingsWidget", "Output priority level:"))
        self.label_3.setText(_translate("OutputSettingsWidget", "Clear output on run:"))
        self.label_4.setToolTip(_translate("OutputSettingsWidget", "<html><head/><body><p>If checked, when content is downloaded the full path of the content will be shown in the output window.  If not checked, it will be the user/subreddit name followed by the content title.</p></body></html>"))
        self.label_4.setText(_translate("OutputSettingsWidget", "Output saved content full path: "))
        self.use_color_output_checkbox.setToolTip(_translate("OutputSettingsWidget", "<html><head/><body><p>When selected, output messages will be shown in the colors indicated below</p></body></html>"))
        self.use_color_output_checkbox.setText(_translate("OutputSettingsWidget", "Use color outputs"))
        self.color_groupbox.setTitle(_translate("OutputSettingsWidget", "Output Colors"))
        self.debug_color_label.setText(_translate("OutputSettingsWidget", "DEBUG output color"))
        self.change_debug_color_button.setText(_translate("OutputSettingsWidget", "Change"))
        self.info_color_label.setText(_translate("OutputSettingsWidget", "INFO output color"))
        self.change_info_color_button.setText(_translate("OutputSettingsWidget", "Change"))
        self.warning_color_label.setText(_translate("OutputSettingsWidget", "WARNING output color"))
        self.change_warning_color_button.setText(_translate("OutputSettingsWidget", "Change"))
        self.error_color_label.setText(_translate("OutputSettingsWidget", "ERROR output color"))
        self.change_error_color_button.setText(_translate("OutputSettingsWidget", "Change"))
        self.critical_color_label.setText(_translate("OutputSettingsWidget", "CRITICAL output color"))
        self.change_critical_color_button.setText(_translate("OutputSettingsWidget", "Change"))
        self.requested_color_label.setText(_translate("OutputSettingsWidget", "REQUESTED output color"))
        self.change_requested_color_button.setText(_translate("OutputSettingsWidget", "Change"))
