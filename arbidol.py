import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")

        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '+', '='
        ]

        row, col = 0, 0
        for i, btn in enumerate(buttons):
            button = QPushButton(btn)
            button.clicked.connect(self.on_button_click)
            if btn == "=": 
                grid_layout.addWidget(button, 3,2,1,2) 
            else:
                grid_layout.addWidget(button, row, col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.current_input = ""
        self.first_number = None
        self.operator = None

    def on_button_click(self):
        sender = self.sender().text()

        if sender.isdigit():
            self.current_input += sender
            self.display.setText(self.current_input)
            return

        if sender in "+-*/": 
            if self.current_input:
                self.first_number = float(self.current_input)
                self.operator = sender
                self.current_input = ""
            return

        if sender == "=": 
            if self.first_number is not None and self.current_input:
                second_number = float(self.current_input)
                result = self.calculate(self.first_number, second_number, self.operator)
                self.display.setText(str(result))
                self.current_input = str(result)
                self.first_number = None
                self.operator = None
            return

        if sender == "C":
            self.current_input = ""
            self.first_number = None
            self.operator = None
            self.display.clear()
            return

    def calculate(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            return num1 / num2 if num2 != 0 else "Error"


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
