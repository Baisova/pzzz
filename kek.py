import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

count = 0

def increment():
    global count
    count += 1
    label.setText(str(count))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("счётчик")

button = QPushButton("нажми меня")
label = QLabel("0")

button.clicked.connect(increment)

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
