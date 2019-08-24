import re
import sys
from PyQt5.QtWidgets import *


def tokenize(expStr):
    RE = re.compile(r'(?:(?<=[^\d\.])(?=\d)|(?=[^\d\.]))', re.MULTILINE)
    return [x for x in re.sub(RE, " ", expStr).split(" ") if x]


def parse_expr(expStr):
    tokens = tokenize(expStr)
    OP = ("*", "/", "+", "-", "(", ")")
    P = {
        "*": 50,
        "/": 50,
        "+": 40,
        "-": 40,
        "(": 0
    }
    output = []
    stack = []

    for item in tokens:
        if item not in OP:
            output.append(item)
        elif item == "(":
            stack.append(item)
        elif item == ")":
            while stack != [] and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack != [] and P[stack[-1]] >= P[item]:
                output.append(stack.pop())
            stack.append(item)

    while stack:
        output.append(stack.pop())

    return output


def calc_expr(expStr):
    tokens = expStr
    OP = ("*", "/", "+", "-",)
    FUNC = {
        "*": lambda x, y: y * x,
        "/": lambda x, y: y / x,
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
    }
    stack = []

    for item in tokens:
        if item not in OP:
            if '.' in item:
                stack.append(float(item))
            else:
                stack.append(int(item))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(FUNC[item](a, b))

    return stack.pop()


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
            self.le.setText(str(calc_expr(parse_expr(self.le.text()))))
        elif str(sending_button.objectName()) == "Bck":
            tmp = str(self.le.text())
            tmp = tmp[:-1]
            self.le.setText(tmp)
        elif str(sending_button.objectName()) == "Cls":
            tmp = str(self.le.text())
            tmp = tmp[:0]
            self.le.setText(tmp)
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
