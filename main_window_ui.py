# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Jan 22 19:48:54 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(774, 568)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(774, 568))
        MainWindow.setMaximumSize(QtCore.QSize(774, 568))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 773, 57))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.highEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.highEdit.setReadOnly(True)
        self.highEdit.setObjectName(_fromUtf8("highEdit"))
        self.gridLayout.addWidget(self.highEdit, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.lowEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lowEdit.setReadOnly(True)
        self.lowEdit.setObjectName(_fromUtf8("lowEdit"))
        self.gridLayout.addWidget(self.lowEdit, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.lastEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lastEdit.setReadOnly(True)
        self.lastEdit.setObjectName(_fromUtf8("lastEdit"))
        self.gridLayout.addWidget(self.lastEdit, 0, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.buyEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.buyEdit.setReadOnly(True)
        self.buyEdit.setObjectName(_fromUtf8("buyEdit"))
        self.gridLayout.addWidget(self.buyEdit, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 5, 1, 1)
        self.averageEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.averageEdit.setReadOnly(True)
        self.averageEdit.setObjectName(_fromUtf8("averageEdit"))
        self.gridLayout.addWidget(self.averageEdit, 2, 6, 1, 1)
        self.sellEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.sellEdit.setReadOnly(True)
        self.sellEdit.setObjectName(_fromUtf8("sellEdit"))
        self.gridLayout.addWidget(self.sellEdit, 2, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 7, 1, 1)
        self.vwapEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.vwapEdit.setReadOnly(True)
        self.vwapEdit.setObjectName(_fromUtf8("vwapEdit"))
        self.gridLayout.addWidget(self.vwapEdit, 0, 8, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)
        self.volumeEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.volumeEdit.setReadOnly(True)
        self.volumeEdit.setObjectName(_fromUtf8("volumeEdit"))
        self.gridLayout.addWidget(self.volumeEdit, 2, 8, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 60, 771, 491))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tradeList = QtGui.QTreeWidget(self.layoutWidget)
        self.tradeList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tradeList.setObjectName(_fromUtf8("tradeList"))
        self.gridLayout_2.addWidget(self.tradeList, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.depthList = QtGui.QTreeWidget(self.layoutWidget)
        self.depthList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.depthList.setObjectName(_fromUtf8("depthList"))
        self.gridLayout_3.addWidget(self.depthList, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.messageList = QtGui.QTreeWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageList.sizePolicy().hasHeightForWidth())
        self.messageList.setSizePolicy(sizePolicy)
        self.messageList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.messageList.setAutoScrollMargin(0)
        self.messageList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.messageList.setObjectName(_fromUtf8("messageList"))
        self.gridLayout_4.addWidget(self.messageList, 1, 0, 1, 2)
        self.commandEdit = QtGui.QLineEdit(self.layoutWidget)
        self.commandEdit.setObjectName(_fromUtf8("commandEdit"))
        self.gridLayout_4.addWidget(self.commandEdit, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuUpdate_2 = QtGui.QMenu(self.menuFile)
        self.menuUpdate_2.setObjectName(_fromUtf8("menuUpdate_2"))
        self.menuAccount = QtGui.QMenu(self.menubar)
        self.menuAccount.setObjectName(_fromUtf8("menuAccount"))
        self.menuUpdate = QtGui.QMenu(self.menuAccount)
        self.menuUpdate.setObjectName(_fromUtf8("menuUpdate"))
        self.menuLog = QtGui.QMenu(self.menuAccount)
        self.menuLog.setObjectName(_fromUtf8("menuLog"))
        self.menuTrade = QtGui.QMenu(self.menubar)
        self.menuTrade.setObjectName(_fromUtf8("menuTrade"))
        self.menuConnection = QtGui.QMenu(self.menubar)
        self.menuConnection.setObjectName(_fromUtf8("menuConnection"))
        self.menuReconnect = QtGui.QMenu(self.menuConnection)
        self.menuReconnect.setObjectName(_fromUtf8("menuReconnect"))
        self.menuConnect = QtGui.QMenu(self.menuConnection)
        self.menuConnect.setObjectName(_fromUtf8("menuConnect"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionClear_Messages = QtGui.QAction(MainWindow)
        self.actionClear_Messages.setObjectName(_fromUtf8("actionClear_Messages"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionOrders = QtGui.QAction(MainWindow)
        self.actionOrders.setObjectName(_fromUtf8("actionOrders"))
        self.actionHistory_2 = QtGui.QAction(MainWindow)
        self.actionHistory_2.setObjectName(_fromUtf8("actionHistory_2"))
        self.actionUpdate_AllAccount = QtGui.QAction(MainWindow)
        self.actionUpdate_AllAccount.setObjectName(_fromUtf8("actionUpdate_AllAccount"))
        self.actionUpdate_History = QtGui.QAction(MainWindow)
        self.actionUpdate_History.setObjectName(_fromUtf8("actionUpdate_History"))
        self.actionUpdateOrders = QtGui.QAction(MainWindow)
        self.actionUpdateOrders.setObjectName(_fromUtf8("actionUpdateOrders"))
        self.actionUpdate_Funds = QtGui.QAction(MainWindow)
        self.actionUpdate_Funds.setObjectName(_fromUtf8("actionUpdate_Funds"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionSave_Log = QtGui.QAction(MainWindow)
        self.actionSave_Log.setObjectName(_fromUtf8("actionSave_Log"))
        self.actionPlace_Order = QtGui.QAction(MainWindow)
        self.actionPlace_Order.setObjectName(_fromUtf8("actionPlace_Order"))
        self.actionBuy = QtGui.QAction(MainWindow)
        self.actionBuy.setObjectName(_fromUtf8("actionBuy"))
        self.actionCall = QtGui.QAction(MainWindow)
        self.actionCall.setObjectName(_fromUtf8("actionCall"))
        self.actionAuto_Trade = QtGui.QAction(MainWindow)
        self.actionAuto_Trade.setObjectName(_fromUtf8("actionAuto_Trade"))
        self.actionReconnectCurrent = QtGui.QAction(MainWindow)
        self.actionReconnectCurrent.setObjectName(_fromUtf8("actionReconnectCurrent"))
        self.actionReconnectWebSocket = QtGui.QAction(MainWindow)
        self.actionReconnectWebSocket.setObjectName(_fromUtf8("actionReconnectWebSocket"))
        self.actionReconnectSocket_IO = QtGui.QAction(MainWindow)
        self.actionReconnectSocket_IO.setObjectName(_fromUtf8("actionReconnectSocket_IO"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionConnectCurrent = QtGui.QAction(MainWindow)
        self.actionConnectCurrent.setObjectName(_fromUtf8("actionConnectCurrent"))
        self.actionConnectWebSocket = QtGui.QAction(MainWindow)
        self.actionConnectWebSocket.setObjectName(_fromUtf8("actionConnectWebSocket"))
        self.actionConnectSocket_IO = QtGui.QAction(MainWindow)
        self.actionConnectSocket_IO.setObjectName(_fromUtf8("actionConnectSocket_IO"))
        self.actionUpdateAll = QtGui.QAction(MainWindow)
        self.actionUpdateAll.setObjectName(_fromUtf8("actionUpdateAll"))
        self.actionAccount = QtGui.QAction(MainWindow)
        self.actionAccount.setObjectName(_fromUtf8("actionAccount"))
        self.actionTicker = QtGui.QAction(MainWindow)
        self.actionTicker.setObjectName(_fromUtf8("actionTicker"))
        self.actionDepth = QtGui.QAction(MainWindow)
        self.actionDepth.setObjectName(_fromUtf8("actionDepth"))
        self.actionTrades = QtGui.QAction(MainWindow)
        self.actionTrades.setObjectName(_fromUtf8("actionTrades"))
        self.actionChange_API_Key = QtGui.QAction(MainWindow)
        self.actionChange_API_Key.setObjectName(_fromUtf8("actionChange_API_Key"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionLogInfo = QtGui.QAction(MainWindow)
        self.actionLogInfo.setObjectName(_fromUtf8("actionLogInfo"))
        self.actionLogHistory = QtGui.QAction(MainWindow)
        self.actionLogHistory.setObjectName(_fromUtf8("actionLogHistory"))
        self.actionLogOrders = QtGui.QAction(MainWindow)
        self.actionLogOrders.setObjectName(_fromUtf8("actionLogOrders"))
        self.actionUpdate_Orders = QtGui.QAction(MainWindow)
        self.actionUpdate_Orders.setObjectName(_fromUtf8("actionUpdate_Orders"))
        self.actionCancel_Order = QtGui.QAction(MainWindow)
        self.actionCancel_Order.setObjectName(_fromUtf8("actionCancel_Order"))
        self.actionLogFunds = QtGui.QAction(MainWindow)
        self.actionLogFunds.setObjectName(_fromUtf8("actionLogFunds"))
        self.menuUpdate_2.addAction(self.actionUpdateAll)
        self.menuUpdate_2.addSeparator()
        self.menuUpdate_2.addAction(self.actionAccount)
        self.menuUpdate_2.addAction(self.actionTicker)
        self.menuUpdate_2.addAction(self.actionDepth)
        self.menuUpdate_2.addAction(self.actionTrades)
        self.menuFile.addAction(self.menuUpdate_2.menuAction())
        self.menuFile.addAction(self.actionClear_Messages)
        self.menuFile.addAction(self.actionSave_Log)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuUpdate.addAction(self.actionUpdate_AllAccount)
        self.menuUpdate.addSeparator()
        self.menuUpdate.addAction(self.actionUpdate_History)
        self.menuUpdate.addAction(self.actionUpdate_Funds)
        self.menuUpdate.addAction(self.actionUpdate_Orders)
        self.menuLog.addAction(self.actionLogInfo)
        self.menuLog.addAction(self.actionLogHistory)
        self.menuLog.addAction(self.actionLogOrders)
        self.menuLog.addAction(self.actionLogFunds)
        self.menuAccount.addAction(self.actionLogin)
        self.menuAccount.addAction(self.actionLogout)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionChange_API_Key)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.menuUpdate.menuAction())
        self.menuAccount.addAction(self.menuLog.menuAction())
        self.menuTrade.addAction(self.actionPlace_Order)
        self.menuTrade.addAction(self.actionCancel_Order)
        self.menuTrade.addAction(self.actionCall)
        self.menuTrade.addAction(self.actionAuto_Trade)
        self.menuReconnect.addAction(self.actionReconnectCurrent)
        self.menuReconnect.addSeparator()
        self.menuReconnect.addAction(self.actionReconnectWebSocket)
        self.menuReconnect.addAction(self.actionReconnectSocket_IO)
        self.menuConnect.addAction(self.actionConnectCurrent)
        self.menuConnect.addSeparator()
        self.menuConnect.addAction(self.actionConnectWebSocket)
        self.menuConnect.addAction(self.actionConnectSocket_IO)
        self.menuConnection.addAction(self.menuConnect.menuAction())
        self.menuConnection.addAction(self.menuReconnect.menuAction())
        self.menuConnection.addAction(self.actionDisconnect)
        self.menuSettings.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuTrade.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.label.setBuddy(self.highEdit)
        self.label_2.setBuddy(self.lowEdit)
        self.label_3.setBuddy(self.lastEdit)
        self.label_4.setBuddy(self.buyEdit)
        self.label_5.setBuddy(self.sellEdit)
        self.label_6.setBuddy(self.averageEdit)
        self.label_7.setBuddy(self.vwapEdit)
        self.label_8.setBuddy(self.volumeEdit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mt.Gox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "High:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Low:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Last:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Buy:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Sell:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Average:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "VWAP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Volume:", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Trades", None, QtGui.QApplication.UnicodeUTF8))
        self.depthList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.depthList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.depthList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.messageList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.messageList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpdate_2.setTitle(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAccount.setTitle(QtGui.QApplication.translate("MainWindow", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpdate.setTitle(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLog.setTitle(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTrade.setTitle(QtGui.QApplication.translate("MainWindow", "Trade", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConnection.setTitle(QtGui.QApplication.translate("MainWindow", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.menuReconnect.setTitle(QtGui.QApplication.translate("MainWindow", "Reconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConnect.setTitle(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Messages.setText(QtGui.QApplication.translate("MainWindow", "Clear Messages", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOrders.setText(QtGui.QApplication.translate("MainWindow", "Orders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory_2.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_AllAccount.setText(QtGui.QApplication.translate("MainWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_History.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateOrders.setText(QtGui.QApplication.translate("MainWindow", "Orders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Funds.setText(QtGui.QApplication.translate("MainWindow", "Funds", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogin.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogout.setText(QtGui.QApplication.translate("MainWindow", "Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Log.setText(QtGui.QApplication.translate("MainWindow", "Save Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlace_Order.setText(QtGui.QApplication.translate("MainWindow", "Place Order", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuy.setText(QtGui.QApplication.translate("MainWindow", "Buy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCall.setText(QtGui.QApplication.translate("MainWindow", "Call", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAuto_Trade.setText(QtGui.QApplication.translate("MainWindow", "Auto Trade", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReconnectCurrent.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReconnectWebSocket.setText(QtGui.QApplication.translate("MainWindow", "WebSocket", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReconnectSocket_IO.setText(QtGui.QApplication.translate("MainWindow", "Socket.IO", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectCurrent.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectWebSocket.setText(QtGui.QApplication.translate("MainWindow", "WebSocket", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectSocket_IO.setText(QtGui.QApplication.translate("MainWindow", "Socket.IO", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateAll.setText(QtGui.QApplication.translate("MainWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAccount.setText(QtGui.QApplication.translate("MainWindow", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTicker.setText(QtGui.QApplication.translate("MainWindow", "Ticker", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDepth.setText(QtGui.QApplication.translate("MainWindow", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrades.setText(QtGui.QApplication.translate("MainWindow", "Trades", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange_API_Key.setText(QtGui.QApplication.translate("MainWindow", "Change API Key", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogInfo.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogHistory.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogOrders.setText(QtGui.QApplication.translate("MainWindow", "Orders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Orders.setText(QtGui.QApplication.translate("MainWindow", "Orders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel_Order.setText(QtGui.QApplication.translate("MainWindow", "Cancel Order", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogFunds.setText(QtGui.QApplication.translate("MainWindow", "Funds", None, QtGui.QApplication.UnicodeUTF8))

