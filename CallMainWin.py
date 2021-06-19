# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainWindow import Ui_MainWindow
from SettingWindow import Ui_SettingWindow
from ShowDataWindow import Ui_ShowdataWindow
import serial
import serial.tools.list_ports
import socket
from crcmod import *
from binascii import *
from PyQt5.QtWidgets import QMessageBox

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children()生成子窗口实例self.child
        self.setting = SettingForm()

        self.showdata = ShowDataForm()

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

        #设置按钮按下，加载设置界面
        self.SettingButton.clicked.connect(self.SettingShow)

        #显示按钮按下，加载数据显示界面
        self.ShowDataButton.clicked.connect(self.DataShow)
        
        self.DataShow()
        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        #self.addWinAction.triggered.connect(self.childShow)

    def SettingShow(self):
        # 添加子窗口
        self.MaingridLayout.addWidget(self.setting)
        self.showdata.hide()
        self.setting.show()
    
    def DataShow(self):
        # 添加子窗口
        self.MaingridLayout.addWidget(self.showdata)
        self.setting.hide()
        self.showdata.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)

#设置页面类
class SettingForm(QWidget, Ui_SettingWindow):
    def __init__(self):
        super(SettingForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("设置")
        self.ser = serial.Serial()
        
        #串口类初始化
        self.port_check()       #检测可用COM口
        self.bps_list = [2400,4800,9600,19200,57600,115200]
        self.get_bps_flg=0

        #网络类初始化
        self.get_local_ip()

        #信号
        self.pushButton_search_serial.clicked.connect(self.port_check)  #检测串口按钮
        self.pushButton_get_device.clicked.connect(self.connect_device)  #获取设备信息按钮

        #self.checkBox_12.stateChanged.connect()
        
        

        

    #检测串口
    def port_check(self):
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_serial_list.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.comboBox_serial_list.addItem(port[0])

    #获取设备信息
    def connect_device(self):
        #遍历波特率
        for i in self.bps_list:
            self.ser.port = self.comboBox_serial_list.currentText()
            self.ser.baudrate = int(i)
            self.ser.timeout = 0.3
            self.ser.bytesize = serial.EIGHTBITS
            self.ser.stopbits = serial.STOPBITS_ONE
            self.ser.parity = serial.PARITY_NONE
            try:
                self.ser.open()
                #print("OPEN!")
            except:
                QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
                self.ser.close()
            self.testdata = '00 03 10 00 00 02'
            self.testdata = self.Get_CRC(self.testdata)
            self.send_data = bytes.fromhex(self.testdata)

            self.ser.write(self.send_data)
            #print('发送完成')

            self.read = self.ser.read(11)
            #print(self.read)
            if self.read:
                self.str_return_data = str(self.read.hex())  # bytes(2进制)转换为hex(16进制)
                print('read data ->',self.str_return_data,'bps is ',i)
                if self.str_return_data[13] == '1':
                    self.temp_bps1 = 2400
                    self.get_bps_flg=1
                if self.str_return_data[13] == '2':
                    self.temp_bps1 = 4800
                    self.get_bps_flg=1
                if self.str_return_data[13] == '3':
                    self.temp_bps1 = 9600
                    self.get_bps_flg=1
                if self.str_return_data[13] == '4':
                    self.temp_bps1 = 19200
                    self.get_bps_flg=1
                if self.str_return_data[13] == '5':
                    self.temp_bps1 = 57600
                    self.get_bps_flg=1
                if self.str_return_data[13] == '6':
                    self.temp_bps1 = 115200
                    self.get_bps_flg=1
                
                if self.get_bps_flg:
                    self.tem_addr = self.str_return_data[8]+self.str_return_data[9]
                    self.comboBox_2_bpslist.addItem(str(self.temp_bps1))
                    self.comboBox_2_bpslist.addItems(['2400','4800','9600','19200','57600','115200'])
                    self.lineEdit_addr.setText(self.tem_addr)
                    QMessageBox.information(self, "连接成功","设备地址: %s     波特率: %s"%(self.tem_addr,self.temp_bps1))
                    break
            self.ser.close()
            #print("close")
              
    #获取本机IP
    def get_local_ip(self):
        self.comboBox_netcarlist.addItem(socket.gethostbyname(socket.gethostname()))

    #计算CRC
    def Get_CRC(self,read):
        self.crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
        self.crcdata = read.replace(" ", "")
        self.readcrcout = hex(self.crc16(unhexlify(self.crcdata))).upper()
        self.str_list = list(self.readcrcout)
        if len(self.str_list) < 6:
            self.str_list.insert(2, '0' * (6 - len(self.str_list)))  # 位数不足补0
        self.crc_datalist = "".join(self.str_list)
        # print(self.crc_datalist)
        read = read.strip() + ' ' + self.crc_datalist[4:] + ' ' + self.crc_datalist[2:4]
        # print('CRC16校验:',crc_data[4:]+' '+crc_data[2:4])
        # print('增加Modbus CRC16校验：>>>',read)
        return read


#显示类
class ShowDataForm(QWidget, Ui_ShowdataWindow):
    def __init__(self):
        super(ShowDataForm, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect()
    
    #添加窗口
    def adddatawin(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
