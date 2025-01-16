import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QCheckBox, QRadioButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

label = QLabel("пример текста")
layout.addWidget(label)

color_box = QComboBox()
color_box.addItems(["black", "red", "green", "blue"])
layout.addWidget(color_box)

bold_box = QCheckBox("жирный")
italic_box = QCheckBox("курсив")
layout.addWidget(bold_box)
layout.addWidget(italic_box)

size_small = QRadioButton("маленький")
size_large = QRadioButton("большой")
size_small.setChecked(True)
layout.addWidget(size_small)
layout.addWidget(size_large)

def update_text():
    label.setStyleSheet(f"color: {color_box.currentText()};"
                        f"{'font-weight: bold;' if bold_box.isChecked() else ''}"
                        f"{'font-style: italic;' if italic_box.isChecked() else ''}"
                        f"{'font-size: 16px;' if size_small.isChecked() else 'font-size: 24px;'}")

color_box.currentTextChanged.connect(update_text)
bold_box.stateChanged.connect(update_text)
italic_box.stateChanged.connect(update_text)
size_small.toggled.connect(update_text)
size_large.toggled.connect(update_text)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
