import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 숫자가 보이는 라인에딧 위젯
        leLayout = QHBoxLayout()
        le = QLineEdit(self)
        leLayout.addWidget(le)

        # button 모음 그리드 레이아웃
        grid = QGridLayout()
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        # h_layout 과 grid 를 하나로 만들어줄 v_layout
        vbox = QVBoxLayout()
        vbox.addLayout(leLayout)
        vbox.addLayout(grid)

        self.setGeometry(300, 150, 300, 250)
        self.setLayout(vbox)

        self.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("계산기")
        MainWidget = MyWidget()
        self.setCentralWidget(MainWidget)  # 반드시 필요함.

        self.setGeometry(300, 700, 350, 150)
        self.show()

        # move & resize로 대체 가능

        # 동적으로 추가한 버튼


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    app.exec_()
