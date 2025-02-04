import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSpinBox, QRadioButton, QButtonGroup, QLabel

class Weather:
    def __init__(self, city, temperature, unit):
        self.city, self.temperature, self.unit = city, temperature, unit

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_objects(data):
    return [Weather(item['city'], item['temperature'], item['unit']) for item in data]

class WeatherApp(QWidget):
    def __init__(self, weather_objects):
        super().__init__()
        self.weather_objects = weather_objects
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Данные о погоде')
        layout = QVBoxLayout()

        self.spin_box = QSpinBox()
        self.spin_box.setRange(-100, 100) 
        self.spin_box.valueChanged.connect(self.update_table)

        layout.addWidget(QLabel('Порог температуры:'))
        layout.addWidget(self.spin_box)

        self.above_button = QRadioButton('Больше')
        self.below_button = QRadioButton('Меньше')
        self.above_button.setChecked(True) 

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.above_button)
        self.button_group.addButton(self.below_button)
        self.button_group.buttonClicked.connect(self.update_table)

        layout.addWidget(QLabel('Фильтер:'))
        layout.addWidget(self.above_button)
        layout.addWidget(self.below_button)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Город', 'Температура', 'Ед.измерения'])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.update_table()

    def update_table(self):
        threshold = self.spin_box.value()
        if self.above_button.isChecked():
            data = [w for w in self.weather_objects if w.temperature > threshold]
        else:
            data = [w for w in self.weather_objects if w.temperature < threshold]

        self.table.setRowCount(len(data))
        for row, weather in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(weather.city))
            self.table.setItem(row, 1, QTableWidgetItem(str(weather.temperature)))
            self.table.setItem(row, 2, QTableWidgetItem(weather.unit))

file_path = 'gyabraa.json'
data = load_data(file_path)
weather_objects = create_objects(data)

app = QApplication([])
window = WeatherApp(weather_objects)
window.show()
app.exec_()