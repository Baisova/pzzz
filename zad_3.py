from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QLabel, QVBoxLayout

line_edit_surname = None
line_edit_name = None
line_edit_patronymic = None
combo_box_city = None
combo_box_gender = None
label_output = None

def on_button_click():
    surname = line_edit_surname.text()
    name = line_edit_name.text()
    patronymic = line_edit_patronymic.text()
    city = combo_box_city.currentText()
    gender = combo_box_gender.currentText()
    
    output_text = f"Фамилия: {surname}\nИмя: {name}\nОтчество: {patronymic}\nГород: {city}\nПол: {gender}"
    label_output.setText(output_text)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Ввод данных")

line_edit_surname = QLineEdit(window)
line_edit_name = QLineEdit(window)
line_edit_patronymic = QLineEdit(window)

combo_box_city = QComboBox(window)
combo_box_city.addItems(["Изумрудный город", "Пекин", "Чайна таун"])

combo_box_gender = QComboBox(window)
combo_box_gender.addItems(["Мужской", "Женский"])

button_submit = QPushButton("Отправить", window)

label_output = QLabel("", window)

button_submit.clicked.connect(on_button_click)

layout = QVBoxLayout()
layout.addWidget(line_edit_surname)
layout.addWidget(line_edit_name)
layout.addWidget(line_edit_patronymic)
layout.addWidget(combo_box_city)
layout.addWidget(combo_box_gender)
layout.addWidget(button_submit)
layout.addWidget(label_output)

window.setLayout(layout)
window.show()

app.exec()
