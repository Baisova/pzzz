from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QComboBox, QLabel, QVBoxLayout

line_edit_surname = None
line_edit_name = None
line_edit_patronymic = None
combo_box_city = None
combo_box_gender = None
label_output = None

def update_label():
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
combo_box_city.addItems(["Московия", "Донбасс", "Париж"])

combo_box_gender = QComboBox(window)
combo_box_gender.addItems(["Мужской", "Женский"])

label_output = QLabel("", window)

line_edit_surname.textChanged.connect(update_label)
line_edit_name.textChanged.connect(update_label)
line_edit_patronymic.textChanged.connect(update_label)
combo_box_city.currentTextChanged.connect(update_label)
combo_box_gender.currentTextChanged.connect(update_label)

layout = QVBoxLayout()
layout.addWidget(line_edit_surname)
layout.addWidget(line_edit_name)
layout.addWidget(line_edit_patronymic)
layout.addWidget(combo_box_city)
layout.addWidget(combo_box_gender)
layout.addWidget(label_output)

window.setLayout(layout)
window.show()

app.exec()