# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadSessionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadSessionDialog(object):
    def setupUi(self, DownloadSessionDialog):
        DownloadSessionDialog.setObjectName("DownloadSessionDialog")
        DownloadSessionDialog.resize(1689, 919)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(DownloadSessionDialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_reddit_objects_checkbox = QtWidgets.QCheckBox(DownloadSessionDialog)
        self.show_reddit_objects_checkbox.setObjectName("show_reddit_objects_checkbox")
        self.horizontalLayout.addWidget(self.show_reddit_objects_checkbox)
        self.show_posts_checkbox = QtWidgets.QCheckBox(DownloadSessionDialog)
        self.show_posts_checkbox.setObjectName("show_posts_checkbox")
        self.horizontalLayout.addWidget(self.show_posts_checkbox)
        self.show_content_checkbox = QtWidgets.QCheckBox(DownloadSessionDialog)
        self.show_content_checkbox.setObjectName("show_content_checkbox")
        self.horizontalLayout.addWidget(self.show_content_checkbox)
        self.show_comments_checkbox = QtWidgets.QCheckBox(DownloadSessionDialog)
        self.show_comments_checkbox.setObjectName("show_comments_checkbox")
        self.horizontalLayout.addWidget(self.show_comments_checkbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(DownloadSessionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.download_session_widget = QtWidgets.QWidget(self.splitter)
        self.download_session_widget.setObjectName("download_session_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.download_session_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.download_session_list_view = QtWidgets.QListView(self.download_session_widget)
        self.download_session_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.download_session_list_view.setObjectName("download_session_list_view")
        self.verticalLayout.addWidget(self.download_session_list_view)
        self.reddit_object_widget = QtWidgets.QWidget(self.splitter)
        self.reddit_object_widget.setObjectName("reddit_object_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.reddit_object_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reddit_object_list_view = QtWidgets.QListView(self.reddit_object_widget)
        self.reddit_object_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reddit_object_list_view.setObjectName("reddit_object_list_view")
        self.verticalLayout_2.addWidget(self.reddit_object_list_view)
        self.post_widget = QtWidgets.QWidget(self.splitter)
        self.post_widget.setObjectName("post_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.post_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.post_splitter = QtWidgets.QSplitter(self.post_widget)
        self.post_splitter.setOrientation(QtCore.Qt.Vertical)
        self.post_splitter.setObjectName("post_splitter")
        self.post_table_view = QtWidgets.QTableView(self.post_splitter)
        self.post_table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.post_table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.post_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.post_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.post_table_view.setShowGrid(False)
        self.post_table_view.setGridStyle(QtCore.Qt.NoPen)
        self.post_table_view.setObjectName("post_table_view")
        self.post_table_view.horizontalHeader().setCascadingSectionResizes(False)
        self.post_text_browser = QtWidgets.QTextBrowser(self.post_splitter)
        self.post_text_browser.setOpenExternalLinks(True)
        self.post_text_browser.setObjectName("post_text_browser")
        self.verticalLayout_3.addWidget(self.post_splitter)
        self.content_widget = QtWidgets.QWidget(self.splitter)
        self.content_widget.setObjectName("content_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.content_list_view = QtWidgets.QListView(self.content_widget)
        self.content_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.content_list_view.setIconSize(QtCore.QSize(0, 0))
        self.content_list_view.setFlow(QtWidgets.QListView.LeftToRight)
        self.content_list_view.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list_view.setLayoutMode(QtWidgets.QListView.Batched)
        self.content_list_view.setGridSize(QtCore.QSize(0, 0))
        self.content_list_view.setViewMode(QtWidgets.QListView.IconMode)
        self.content_list_view.setBatchSize(10)
        self.content_list_view.setWordWrap(True)
        self.content_list_view.setObjectName("content_list_view")
        self.verticalLayout_4.addWidget(self.content_list_view)
        self.comment_widget = QtWidgets.QWidget(self.splitter)
        self.comment_widget.setObjectName("comment_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.comment_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comment_tree_view = QtWidgets.QTreeView(self.comment_widget)
        self.comment_tree_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.comment_tree_view.setObjectName("comment_tree_view")
        self.verticalLayout_5.addWidget(self.comment_tree_view)
        self.verticalLayout_6.addWidget(self.splitter)

        self.retranslateUi(DownloadSessionDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadSessionDialog)

    def retranslateUi(self, DownloadSessionDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadSessionDialog.setWindowTitle(_translate("DownloadSessionDialog", "Download Sessions"))
        self.show_reddit_objects_checkbox.setText(_translate("DownloadSessionDialog", "Show reddit objects"))
        self.show_posts_checkbox.setText(_translate("DownloadSessionDialog", "Show posts"))
        self.show_content_checkbox.setText(_translate("DownloadSessionDialog", "Show content"))
        self.show_comments_checkbox.setText(_translate("DownloadSessionDialog", "Show comments"))

