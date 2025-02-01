# ch 6.6.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox) 
# QLineEdit, QComboBox 추가
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QDate, Qt #날짜와 주요 속성값을 쓰기 위해 추가

from PyQt5 import QtCore # 모듈 추가

class View(QWidget):
    
    def __init__(self):
        super().__init__()
        # self.date = QDate.currentDate() #현재 날짜를 저장하기 위해 추가
        self.initUI()
    
    def initUI(self):
        # self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self) # 추가

        

        self.te1 = QPlainTextEdit() #텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Calc',self) # 버튼 이름 바꾸기
        self.btn2 = QPushButton('Clear',self)

        self.le1 = QLineEdit('0', self) # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) ## 라인 에디트1 문자열 배치 설정
        self.le1.setFocus(True) # 포커스 설정
        self.le1.selectAll() # 텍스트 전체 선택

        self.le2 = QLineEdit('0', self) # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) ## 라인 에디트2 문자열 배치 설정

        self.cb = QComboBox(self) # 콤보박스 추가
        self.cb.addItems(['+','-','*','/','^','%']) # 콤보박스 항목추가(연산자로 쓰기) #거듭제곱 연산자 추가

        hbox_formular = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)


        hbox = QHBoxLayout()
        hbox.addStretch(1) #공백
        hbox.addWidget(self.btn1) # 버튼 1 배치
        hbox.addWidget(self.btn2) # 버튼 2 배치

        vbox = QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 추가
        vbox.addLayout(hbox_formular) # hbox_formular 배치
        vbox.addLayout(hbox) #btn1 위치에 hbox 배치
        vbox.addStretch(1)
        # vbox.addWidget(self.lbl1) # 고침

        self.setLayout(vbox) #빈 공간 - 버튼 - 빈공간 순으로 배치된 레이아웃 설정
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) #윈도 아이콘 추가
        self.resize(256,256)
        self.show()


    def setDisplay(self, text): #버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력, 메서드 이름 바꾸기
        #핸들러함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        # QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText(text)
    
    def clearMessage(self):
        self.te1.clear()
