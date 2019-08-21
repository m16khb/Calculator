import sys
import postfix
# import tokenize
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 숫자가 보이는 라인에딧 위젯
        leLayout = QVBoxLayout()
        self.le = QLineEdit(self)
        leLayout.addWidget(self.le)

        # button 모음 그리드 레이아웃
        grid = QGridLayout()
        names = ['Cls', 'Bck', '(', ')',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.setObjectName(name)
            button.pressed.connect(self.button_pressed)
            grid.addWidget(button, *position)

    # h_layout 과 grid 를 하나로 만들어줄 v_layout
        vbox = QVBoxLayout()
        vbox.addLayout(leLayout)
        vbox.addLayout(grid)

        self.setGeometry(300, 150, 300, 250)
        self.setLayout(vbox)

        self.show()

    def button_pressed(self):
        sending_button = self.sender()
        if str(sending_button.objectName()) == "=":
            instance = postfix.postfix()
            self.le.setText(str(instance.parse_expr(self.le.text())))
        else:
            self.le.setText(self.le.text() + str(sending_button.objectName()))


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("계산기")
        MainWidget = MyWidget()
        self.setCentralWidget(MainWidget)  # 반드시 필요함.

        self.setGeometry(300, 700, 350, 150)
        # move & resize로 대체 가능
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    app.exec_()
