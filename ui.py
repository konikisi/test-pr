# ch 8.1.3 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox, QLabel) 
# QLabel 추가
from PyQt5.QtGui import QIcon, QFont # QFont 추가


from PyQt5 import QtCore 

class View(QWidget):
    
    def __init__(self):
        super().__init__()
        # self.date = QDate.currentDate() #현재 날짜를 저장하기 위해 추가
        self.initUI()
    
    def initUI(self):
        # self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self) # 추가

        


        self.te1 = QPlainTextEdit() #텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)

        self.lbl1 = QLabel('v2.3.0',self) # 버전 정보를 나타낼 lbl1 위젯 만들기
        self.lbl1.setFont(QFont('Consolas', 10)) # 폰트 설정 추가, Consolas, 사이즈 10
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
        hbox.addWidget(self.lbl1) # 버전 정보를 나타내기 위한 lbl1 위젯 만들기
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
