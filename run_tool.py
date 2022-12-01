import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from websocket import create_connection
import websocket
from webSocket_function import *


class MyWindow(QWidget):
    connectButtonSignal = pyqtSignal(str)
    sendMessageButtonSignal = pyqtSignal(str)
    # clearSendButtonSignal = pyqtSignal(str)
    # clearMessageButtonSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.int_ui()
        self.messageHistory = list()  # 用来存放消息
        self.ws =None

    def int_ui(self):
        self.ui = uic.loadUi("./webSocket-test.ui")
        # 查看ui文件中有哪些控件
        # print(self.ui.__dict__)

        # 提取要操作的控件
        self.address = self.ui.lineEdit  # 地址输入框
        self.address.setText("ws://test.iot.bsphpro.com/aihm/ws/nettyPush")
        self.sendMessage = self.ui.plainTextEdit  # 发送内容输入框
        self.sendMessage.setPlainText('{"sendType":"registerChannel","iotUserId":"8121606254596784128","machineCode":"cda85993111"}')
        self.connectButton = self.ui.pushButton  # 连接按钮
        self.sendMessageButton = self.ui.pushButton_3  # 发送信息按钮
        self.receiveContent = self.ui.textEdit  # 接收内容显示区域
        self.clearSendButton = self.ui.pushButton_2  # 清空发送内容按钮
        self.clearReceiveButton = self.ui.pushButton_6  # 清空接收内容按钮


        # 绑定信号与槽函数

        self.connectButton.clicked.connect(self.connectServer)  # 连接服务器
        self.connectButtonSignal.connect(self.showReceiveContent)  # 接收内容显示

        self.sendMessageButton.clicked.connect(self.sendMessageToServer)  # 发送内容到服务器
        self.sendMessageButtonSignal.connect(self.showReceiveContent)  # 接收内容显示

        # self.clearSendButton.clicked.connect(self.clearSendContent)  # 清空发送内容
        # self.clearReceiveButton.clicked.connect(self.clearReceiveContent)  # 清空接收内容

    def connectServer(self):
        """连接服务器"""
        address = self.address.text()
        self.ws = create_connection(address)
        res = self.ws.__dict__['connected']
        if res == True:
            res = "连接成功"
        else:
            res = "连接失败"
        print(address)
        self.messageHistory.append(res)
        self.connectButtonSignal.emit(str(self.messageHistory))  # 发送信号到内容显示框

    def sendMessageToServer(self):
        """发送信息"""
        sendMessage = self.sendMessage.toPlainText()
        self.ws.send(sendMessage)

        res = self.ws.recv()
        self.messageHistory.append(res)
        self.sendMessageButtonSignal.emit(str(self.messageHistory))  # 发送信号到内容显示框

    def showReceiveContent(self, messageHistory):
        """显示接收内容"""
        self.receiveContent.setText("<br>".join(self.messageHistory))
        self.receiveContent.repaint()

    def clearSendContent(self):
        """清空发送内容"""
        self.sendContent.setText("")
        self.receiveContent.repaint()


    def clearReceiveContent(self):
        """清空接收内容"""
        self.messageHistory=list()
        self.receiveContent.setText("")
        self.receiveContent.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
